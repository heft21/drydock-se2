"""The BlenderMCP client: one JSON command over a raw socket, and its failure modes.

A fake add-on listens on 127.0.0.1 with an ephemeral port and answers the way the
real one does (a single JSON document, socket left open). Nothing here touches
port 9876 or starts Blender.
"""

import json
import os
import socket
import tempfile
import threading
import unittest
from pathlib import Path
from unittest import mock

from tests import _support  # noqa: F401  (puts the repo on sys.path)

from se2_mcp import blender


class FakeAddon:
    """Accepts connections one at a time and answers each with `respond(request)`.

    `respond` returns a list of byte chunks to send (sent with a short pause
    between them), or None to send nothing and keep the socket open.
    """

    def __init__(self, respond, close_after=True):
        self.respond = respond
        self.close_after = close_after
        self.requests = []
        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(5)
        self.sock.settimeout(0.1)
        self.port = self.sock.getsockname()[1]
        self._stop = threading.Event()
        self.thread = threading.Thread(target=self._serve, daemon=True)
        self.thread.start()

    def _serve(self):
        while not self._stop.is_set():
            try:
                conn, _ = self.sock.accept()
            except socket.timeout:
                continue
            except OSError:
                return
            with conn:
                conn.settimeout(2)
                try:
                    request = json.loads(conn.recv(65536))
                except (OSError, ValueError):
                    continue
                self.requests.append(request)
                chunks = self.respond(request)
                if chunks is None:
                    self._stop.wait(1.0)      # stay silent until the client gives up
                    continue
                for chunk in chunks:
                    conn.sendall(chunk)
                    self._stop.wait(0.05)
                if not self.close_after:
                    self._stop.wait(0.3)

    def close(self):
        self._stop.set()
        self.sock.close()
        self.thread.join(5)


class BlenderCase(unittest.TestCase):
    def serve(self, respond, **kw):
        addon = FakeAddon(respond, **kw)
        self.addCleanup(addon.close)
        patcher = mock.patch.dict(os.environ, {"SE2_MCP_BLENDER_PORT": str(addon.port)})
        patcher.start()
        self.addCleanup(patcher.stop)
        return addon

    def closed_port(self):
        patcher = mock.patch.dict(os.environ, {"SE2_MCP_BLENDER_PORT": str(_support.closed_port(self))})
        patcher.start()
        self.addCleanup(patcher.stop)


def reply(doc):
    return lambda request: [json.dumps(doc).encode()]


class Call(BlenderCase):
    def test_call_sends_the_command_and_returns_the_parsed_reply(self):
        addon = self.serve(reply({"status": "success", "result": {"n": 2}}))
        out = blender.call("get_scene_info", {"a": 1}, timeout=5)
        self.assertEqual(out, {"status": "success", "result": {"n": 2}})
        self.assertEqual(addon.requests, [{"type": "get_scene_info", "params": {"a": 1}}])

    def test_a_reply_that_arrives_in_pieces_is_put_together(self):
        text = json.dumps({"status": "success", "result": "x" * 50}).encode()
        self.serve(lambda request: [text[:10], text[10:30], text[30:]])
        self.assertEqual(blender.call("c", timeout=5)["result"], "x" * 50)

    def test_missing_params_are_sent_as_an_empty_object(self):
        addon = self.serve(reply({"status": "success"}))
        blender.call("ping", timeout=5)
        self.assertEqual(addon.requests[0]["params"], {})

    def test_a_closed_port_raises_blender_down(self):
        self.closed_port()
        with self.assertRaises(blender.BlenderDown) as ctx:
            blender.call("get_scene_info", timeout=2)
        self.assertIn("No BlenderMCP at", str(ctx.exception))

    def test_a_silent_add_on_is_reported_as_a_timeout(self):
        self.serve(lambda request: None)
        with self.assertRaises(blender.BlenderDown) as ctx:
            blender.call("slow", timeout=0.3)
        self.assertIn("did not answer", str(ctx.exception))

    def test_a_connection_closed_before_a_full_reply_is_reported(self):
        self.serve(lambda request: [b'{"status": "succ'])
        with self.assertRaises(blender.BlenderDown) as ctx:
            blender.call("cut", timeout=3)
        self.assertIn("closed the connection", str(ctx.exception))


class IsUp(BlenderCase):
    def test_is_up_is_true_when_the_add_on_answers(self):
        self.serve(reply({"status": "success", "result": {}}))
        self.assertTrue(blender.is_up())

    def test_is_up_is_false_on_a_closed_port(self):
        self.closed_port()
        self.assertFalse(blender.is_up())


class RunPython(BlenderCase):
    def test_printed_output_comes_back_as_a_result(self):
        self.serve(reply({"status": "success", "result": {"result": "hello\n"}}))
        self.assertEqual(blender.run_python("print('hello')", timeout=5),
                         {"ok": True, "output": "hello\n"})

    def test_an_error_reply_is_reported_with_its_reason(self):
        self.serve(reply({"status": "error", "message": "NameError: bpy"}))
        out = blender.run_python("boom()", timeout=5)
        self.assertEqual(out, {"ok": False, "error": "NameError: bpy"})

    def test_run_json_parses_the_last_document_after_progress_text(self):
        self.serve(reply({"status": "success",
                          "result": {"result": 'working...\n{"a": [1, 2]}\n'}}))
        self.assertEqual(blender.run_json("x", timeout=5), {"a": [1, 2]})

    def test_run_json_reports_output_without_json(self):
        self.serve(reply({"status": "success", "result": {"result": "just text"}}))
        out = blender.run_json("x", timeout=5)
        self.assertFalse(out["ok"])
        self.assertEqual(out["output"], "just text")

    def test_run_json_passes_an_error_reply_through(self):
        self.serve(reply({"status": "error", "message": "bad"}))
        self.assertEqual(blender.run_json("x", timeout=5), {"ok": False, "error": "bad"})


class ExportModel(BlenderCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)

    def test_an_unknown_variant_is_rejected_before_anything_is_sent(self):
        addon = self.serve(reply({"status": "success"}))
        out = blender.export_model("Block", self.dir, variant="SHATTERED")
        self.assertFalse(out["ok"])
        self.assertIn("variant must be one of", out["error"])
        self.assertEqual(addon.requests, [])
        self.assertEqual(list(self.dir.iterdir()), [])

    def test_an_unknown_limit_is_rejected_before_anything_is_sent(self):
        addon = self.serve(reply({"status": "success"}))
        out = blender.export_model("Block", self.dir, limit="EVERYTHING")
        self.assertFalse(out["ok"])
        self.assertIn("limit must be one of", out["error"])
        self.assertEqual(addon.requests, [])

    def test_every_documented_variant_and_limit_is_accepted(self):
        payload = {"status": "success",
                   "result": {"result": '{"exported": [], "errors": [], "directory": "x"}'}}
        addon = self.serve(reply(payload))
        for variant in blender.EXPORT_VARIANTS:
            for limit in blender.EXPORT_LIMITS:
                with self.subTest(variant=variant, limit=limit):
                    out = blender.export_model("Block", self.dir, variant=variant, limit=limit)
                    self.assertNotIn("variant must", str(out.get("error", "")))
                    self.assertNotIn("limit must", str(out.get("error", "")))
        self.assertEqual(len(addon.requests),
                         len(blender.EXPORT_VARIANTS) * len(blender.EXPORT_LIMITS))

    def test_nothing_on_disk_is_reported_as_not_ok_with_a_hint(self):
        payload = {"status": "success",
                   "result": {"result": '{"exported": [], "errors": [], "directory": "x"}'}}
        self.serve(reply(payload))
        out = blender.export_model("Block", self.dir)
        self.assertFalse(out["ok"])
        self.assertEqual(out["files_on_disk"], [])
        self.assertIn("select the mesh", out["hint"])

    def test_files_that_landed_are_listed(self):
        (self.dir / "NonFractured").mkdir()
        (self.dir / "NonFractured" / "Block.fbx").write_bytes(b"x")
        (self.dir / "NonFractured" / "notes.txt").write_bytes(b"x")
        payload = {"status": "success",
                   "result": {"result": '{"exported": [{"lod": 0}], "errors": [], "directory": "x"}'}}
        self.serve(reply(payload))
        out = blender.export_model("Block", self.dir)
        self.assertTrue(out["ok"])
        self.assertEqual(out["files_on_disk"], [str(Path("NonFractured") / "Block.fbx")])


if __name__ == "__main__":
    unittest.main()
