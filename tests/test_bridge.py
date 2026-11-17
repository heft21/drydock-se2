"""The editor-bridge client: JSON round trips, the token, a dead port, install/uninstall.

A throwaway http.server on 127.0.0.1 stands in for the editor plugin; the client
is pointed at it through SE2_MCP_BRIDGE_PORT. Nothing here touches port 8765.
"""

import http.server
import json
import os
import tempfile
import threading
import unittest
from pathlib import Path
from unittest import mock

from tests import _support  # noqa: F401  (puts the repo on sys.path)

from se2_mcp import bridge
from se2_mcp.config import Paths


class Handler(http.server.BaseHTTPRequestHandler):
    seen: list = []
    status = 200
    reply: bytes = b'{"ok": true}'

    def log_message(self, *args):
        pass

    def _answer(self):
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else b""
        type(self).seen.append({"method": self.command, "path": self.path,
                                "auth": self.headers.get("Authorization"),
                                "body": body})
        self.send_response(type(self).status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(type(self).reply)

    do_GET = do_POST = _answer


class BridgeCase(unittest.TestCase):
    """A cache dir, a fake bridge on an ephemeral port and the env pointing at both."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.handler = type("H", (Handler,), {"seen": [], "status": 200,
                                              "reply": b'{"ok": true}'})
        self.server = http.server.HTTPServer(("127.0.0.1", 0), self.handler)
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever,
                                       kwargs={"poll_interval": 0.01}, daemon=True)
        self.thread.start()
        # cleanups run last-in first: shut the loop down, then close, then join
        self.addCleanup(self.thread.join, 5)
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        patcher = mock.patch.dict(os.environ, {
            "SE2_MCP_CACHE": str(self.dir / "cache"),
            "SE2_MCP_BRIDGE_PORT": str(self.port)})
        patcher.start()
        self.addCleanup(patcher.stop)
        paths = mock.patch("se2_mcp.config.PATHS", Paths(sdk=self.dir / "sdk"))
        paths.start()
        self.addCleanup(paths.stop)

    def write_token(self, text):
        path = bridge.token_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


class Requests(BridgeCase):
    def test_get_json_returns_the_parsed_reply(self):
        self.handler.reply = b'{"ok": true, "n": 3}'
        self.assertEqual(bridge.get_json("/ping"), {"ok": True, "n": 3})
        self.assertEqual(self.handler.seen[0]["method"], "GET")
        self.assertEqual(self.handler.seen[0]["path"], "/ping")

    def test_post_json_sends_the_payload_as_json(self):
        self.handler.reply = b'{"echo": 1}'
        out = bridge.post_json("/eval", {"code": "1+1", "unicode": "\u00e4"})
        self.assertEqual(out, {"echo": 1})
        sent = self.handler.seen[0]
        self.assertEqual(sent["method"], "POST")
        self.assertEqual(json.loads(sent["body"]), {"code": "1+1", "unicode": "\u00e4"})

    def test_the_token_from_the_cache_dir_is_sent_as_a_bearer_header(self):
        self.write_token("old-token\nsecret-token\n")
        bridge.get_json("/ping")
        self.assertEqual(self.handler.seen[0]["auth"], "Bearer secret-token")

    def test_no_token_file_means_no_authorization_header(self):
        self.assertIsNone(bridge.read_token())
        bridge.get_json("/ping")
        self.assertIsNone(self.handler.seen[0]["auth"])

    def test_the_token_is_read_again_on_every_request(self):
        self.write_token("one")
        bridge.get_json("/ping")
        self.write_token("two")
        bridge.get_json("/ping")
        self.assertEqual([s["auth"] for s in self.handler.seen],
                         ["Bearer one", "Bearer two"])

    def test_get_bytes_returns_the_raw_body(self):
        self.handler.reply = b"\x89PNG-not-json"
        self.assertEqual(bridge.get_bytes("/shot"), b"\x89PNG-not-json")

    def test_an_error_status_with_a_json_body_comes_back_as_that_body(self):
        self.handler.status = 500
        self.handler.reply = b'{"error": "boom"}'
        self.assertEqual(bridge.get_json("/eval"), {"error": "boom"})

    def test_a_401_says_the_token_was_rejected(self):
        self.handler.status = 401
        with self.assertRaises(bridge.BridgeDown) as ctx:
            bridge.get_json("/ping")
        self.assertIn("rejected the token", str(ctx.exception))

    def test_is_up_is_true_when_ping_says_ok(self):
        self.assertTrue(bridge.is_up())

    def test_is_up_is_false_when_ping_does_not_say_ok(self):
        self.handler.reply = b'{"ok": false}'
        self.assertFalse(bridge.is_up())
        self.handler.reply = b"not json"
        self.assertFalse(bridge.is_up())


class ClosedPort(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ, {"SE2_MCP_BRIDGE_PORT": str(_support.closed_port(self))})
        patcher.start()
        self.addCleanup(patcher.stop)
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        env = mock.patch.dict(os.environ, {"SE2_MCP_CACHE": tmp.name})
        env.start()
        self.addCleanup(env.stop)

    def test_a_closed_port_raises_bridge_down(self):
        with self.assertRaises(bridge.BridgeDown) as ctx:
            bridge.get_json("/ping", timeout=2)
        self.assertIn("No bridge at", str(ctx.exception))

    def test_a_closed_port_is_reported_as_down(self):
        self.assertFalse(bridge.is_up())

    def test_the_url_follows_the_port_setting(self):
        self.assertEqual(bridge.base_url(),
                         "http://127.0.0.1:" + os.environ["SE2_MCP_BRIDGE_PORT"])


class Install(BridgeCase):
    def setUp(self):
        super().setUp()
        self.build = self.dir / "build"
        self.build.mkdir()
        (self.build / "SE2McpBridge.dll").write_bytes(b"MZ")
        (self.build / "SE2McpBridge.deps.json").write_text("{}", encoding="utf-8")
        (self.build / "notes.txt").write_text("not copied", encoding="utf-8")
        patcher = mock.patch.object(bridge, "PLUGIN_BUILD_DIR", self.build)
        patcher.start()
        self.addCleanup(patcher.stop)

        self.proj = self.dir / "mod"
        self.proj.mkdir()
        self.proj_file = self.proj / "Mod.vrgproj"
        doc = {"$Type": "T", "$Value": {"Name": "Mod",
                                        "EditorExtensionAssemblies": ["Other.dll"],
                                        "EditorExtensionAssembliesSearchPaths": ["C:/Other"],
                                        "Keep": [1, 2]}}
        self.original = json.dumps(doc, indent=2, ensure_ascii=False).replace(
            "\n", "\r\n").encode("utf-8")
        self.proj_file.write_bytes(self.original)

    def value(self):
        return json.loads(self.proj_file.read_text(encoding="utf-8"))["$Value"]

    def test_the_plugin_counts_as_built_when_the_dll_is_there(self):
        self.assertTrue(bridge.plugin_built())
        (self.build / "SE2McpBridge.dll").unlink()
        self.assertFalse(bridge.plugin_built())

    def test_install_without_a_built_plugin_says_so(self):
        (self.build / "SE2McpBridge.dll").unlink()
        with self.assertRaises(FileNotFoundError):
            bridge.install(self.proj)

    def test_install_adds_the_bridge_and_keeps_everything_else(self):
        bridge.install(self.proj)
        v = self.value()
        self.assertEqual(v["EditorExtensionAssemblies"], ["Other.dll", "SE2McpBridge.dll"])
        self.assertEqual(v["EditorExtensionAssembliesSearchPaths"],
                         ["C:/Other", str(self.build)])
        self.assertEqual(v["Keep"], [1, 2])
        self.assertFalse((self.proj / bridge.PLUGIN_FOLDER).exists())

    def test_installing_twice_adds_nothing_more(self):
        bridge.install(self.proj)
        once = self.proj_file.read_bytes()
        bridge.install(self.proj_file)
        self.assertEqual(self.proj_file.read_bytes(), once)

    def test_uninstall_removes_exactly_the_bridge_entries(self):
        bridge.install(self.proj)
        bridge.uninstall(self.proj)
        self.assertEqual(self.proj_file.read_bytes(), self.original)

    def test_uninstall_on_a_project_without_the_bridge_changes_nothing(self):
        bridge.uninstall(self.proj)
        self.assertEqual(self.proj_file.read_bytes(), self.original)

    def test_a_copied_install_puts_the_plugin_in_the_project_and_uninstall_removes_it(self):
        bridge.install(self.proj, copy_into_project=True)
        folder = self.proj / bridge.PLUGIN_FOLDER
        self.assertEqual(sorted(p.name for p in folder.iterdir()),
                         ["SE2McpBridge.deps.json", "SE2McpBridge.dll"])
        self.assertIn(".\\" + bridge.PLUGIN_FOLDER,
                      self.value()["EditorExtensionAssembliesSearchPaths"])
        out = bridge.uninstall(self.proj)
        self.assertFalse(folder.exists())
        self.assertEqual(out["removed_plugin_dir"], str(folder))
        self.assertEqual(self.proj_file.read_bytes(), self.original)

    def test_a_folder_without_a_project_file_is_an_error(self):
        empty = self.dir / "empty"
        empty.mkdir()
        with self.assertRaises(FileNotFoundError):
            bridge.install(empty)
        with self.assertRaises(FileNotFoundError):
            bridge.uninstall(empty)


if __name__ == "__main__":
    unittest.main()
