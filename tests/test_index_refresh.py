"""The index refreshes itself in the background; none of this ever builds for real."""

import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from se2_mcp import docs, index  # noqa: E402

_STATE = ("_build_thread", "_stale_checked", "_refresh_failed_for", "_refresh_reason",
          "_build_error", "_build_started")


class _Paths:
    """Stands in for config.Paths, which is frozen and resolves db_path itself."""

    def __init__(self, db: Path):
        self.db_path = db
        self.sdk = Path("sdk")

    def check(self):
        return []


class Refresh(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        db = Path(self._tmp.name) / "db.sqlite3"
        db.write_bytes(b"x")
        self.saved = {k: getattr(index, k) for k in _STATE}
        self.saved.update(PATHS=index.PATHS, build=index.build,
                          stale_reason=index.stale_reason, _meta_rows=index._meta_rows)
        self.addCleanup(self._restore)
        index.PATHS = _Paths(db)
        index._build_thread = None
        index._stale_checked = 0.0
        index._refresh_failed_for = None
        index._refresh_reason = None
        index._build_error = None
        self.calls = 0
        self.gate = None
        self.fail = False
        index.build = self._fake_build
        index.stale_reason = lambda rows=None: "reason-1"
        patcher = mock.patch.object(docs, "is_built", return_value=True)
        patcher.start()
        self.addCleanup(patcher.stop)
        patcher = mock.patch("sys.stderr")
        patcher.start()
        self.addCleanup(patcher.stop)

    def _restore(self):
        thread = index._build_thread
        if self.gate is not None:
            self.gate.set()
        if thread is not None:
            thread.join(5)
        for k, v in self.saved.items():
            setattr(index, k, v)

    def _fake_build(self):
        self.calls += 1
        if self.gate is not None:
            self.gate.wait(5)
        if self.fail:
            raise RuntimeError("boom")
        return index.IndexStats()

    def _join(self):
        index._build_thread.join(5)

    def test_stale_index_is_rebuilt_once(self):
        self.assertEqual(index.refresh_if_stale(force_check=True), "reason-1")
        self._join()
        self.assertEqual(self.calls, 1)
        self.assertIsNone(index._refresh_reason)

    def test_fresh_index_is_left_alone(self):
        index.stale_reason = lambda rows=None: None
        self.assertIsNone(index.refresh_if_stale(force_check=True))
        self.assertEqual(self.calls, 0)

    def test_the_check_is_throttled(self):
        seen = []
        index.stale_reason = lambda rows=None: seen.append(1)
        index.refresh_if_stale()
        index.refresh_if_stale()
        self.assertEqual(len(seen), 1)

    def test_a_failing_refresh_is_not_retried_until_cleared(self):
        self.fail = True
        index.refresh_if_stale(force_check=True)
        self._join()
        self.assertEqual(index._refresh_failed_for, "reason-1")
        self.assertIsNone(index.refresh_if_stale(force_check=True))
        self.assertEqual(self.calls, 1)
        index.clear_refresh_failure()
        self.assertEqual(index.refresh_if_stale(force_check=True), "reason-1")
        self._join()
        self.assertEqual(self.calls, 2)

    def test_ensure_does_not_wait_for_the_refresh(self):
        self.gate = threading.Event()
        index.stale_reason = lambda rows=None: "reason-1"
        index._stale_checked = -1e9               # make the throttle window open
        index.ensure()
        self.assertTrue(index.building())
        self.gate.set()
        self._join()
        self.assertEqual(self.calls, 1)

    def test_status_reports_refreshing(self):
        self.gate = threading.Event()
        index._meta_rows = lambda: {"built_at": "0"}
        index.refresh_if_stale(force_check=True)
        status = index.index_status()
        self.assertTrue(status["refreshing"])
        self.assertIn("Being refreshed", status["hint"])
        self.gate.set()
        self._join()

    def test_swap_retries_on_permission_error(self):
        tmp, db = Path(self._tmp.name) / "t", Path(self._tmp.name) / "d"
        tmp.write_bytes(b"y")
        real = index.os.replace
        calls = []

        def flaky(a, b):
            calls.append(1)
            if len(calls) < 3:
                raise PermissionError("in use")
            real(a, b)

        with mock.patch.object(index, "SWAP_RETRY_EVERY", 0.01), \
                mock.patch.object(index.os, "replace", flaky):
            index._swap_in(tmp, db)
        self.assertEqual(len(calls), 3)
        self.assertTrue(db.exists())

    def test_swap_gives_up_and_removes_the_temp_file(self):
        tmp, db = Path(self._tmp.name) / "t", Path(self._tmp.name) / "d"
        tmp.write_bytes(b"y")
        with mock.patch.object(index, "SWAP_RETRY_EVERY", 0.01), \
                mock.patch.object(index, "SWAP_RETRY_FOR", 0.05), \
                mock.patch.object(index.os, "replace", side_effect=PermissionError("x")):
            with self.assertRaises(PermissionError):
                index._swap_in(tmp, db)
        self.assertFalse(tmp.exists())

    def test_a_failing_staleness_check_is_swallowed(self):
        def broken(rows=None):
            raise RuntimeError("nope")
        index.stale_reason = broken
        self.assertIsNone(index.refresh_if_stale(force_check=True))
        self.assertEqual(self.calls, 0)


if __name__ == "__main__":
    unittest.main()
