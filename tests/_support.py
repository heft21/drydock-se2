"""Shared helpers: skip tests that need the SDK index, keep backups out of the repo."""

import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from se2_mcp import authoring, index  # noqa: E402


# index.ensure() would otherwise start a real background rebuild of the user's
# index when it is out of date; an infinite "last check" keeps the throttle shut.
index._stale_checked = float("inf")


def index_ready() -> bool:
    try:
        return bool(index.index_status().get("built"))
    except Exception:
        return False


def closed_port(testcase: unittest.TestCase) -> int:
    """A port nothing listens on, held for the length of the test.

    Picking a free port, closing it and connecting later leaves a gap in which
    another program can be given that port. A socket that stays bound but never
    listens refuses every connection, and no one else can take the port meanwhile.
    """
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    testcase.addCleanup(sock.close)
    return sock.getsockname()[1]


needs_index =unittest.skipUnless(index_ready(), "the SDK search index is not built")


class TempProject(unittest.TestCase):
    """A scratch directory; replaced files are backed up inside it, not the repo."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)
        self._real_backup = authoring.backup_dir
        authoring.backup_dir = lambda: self.dir / ".backups"

    def tearDown(self):
        authoring.backup_dir = self._real_backup
        self._tmp.cleanup()

    def put(self, name: str, doc: dict) -> Path:
        path = self.dir / name
        data = authoring.serialize(doc)
        path.write_bytes(data)
        asset = doc["$Value"].get("Guid") or doc["$Value"].get("Manipulator", {}).get("Guid") \
            or "00000000-0000-4000-8000-000000000001"
        path.with_name(path.name + ".meta").write_bytes(
            authoring.make_meta(asset, path.name, data).replace("\n", "\r\n").encode("utf-8"))
        return path

    def load(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8-sig"))
