"""Reading the editor's and Mod HUB's logs: newest first, errors pulled out, repeats folded.

The log folders are faked under a temp APPDATA; the real ones are never read.
"""

import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests import _support  # noqa: F401  (puts the repo on sys.path)

from se2_mcp import logs


class LogCase(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.appdata = Path(tmp.name)
        patcher = mock.patch.dict(os.environ, {"APPDATA": str(self.appdata)})
        patcher.start()
        self.addCleanup(patcher.stop)

    def folder(self, app="editor") -> Path:
        d = self.appdata / logs.APPS[app] / "Temp" / "Logs"
        d.mkdir(parents=True, exist_ok=True)
        return d

    def log(self, name, lines, age=0, app="editor") -> Path:
        """Write a log file; `age` is how many seconds older than the base time it is."""
        path = self.folder(app) / name
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        stamp = 1_700_000_000 - age
        os.utime(path, (stamp, stamp))
        return path


class ListRuns(LogCase):
    def test_runs_are_listed_newest_first(self):
        self.log("old.log", ["a"], age=5000)
        self.log("new.log", ["a"], age=0)
        self.log("mid.log", ["a"], age=1000)
        self.assertEqual([r["file"] for r in logs.list_runs("editor")],
                         ["new.log", "mid.log", "old.log"])

    def test_limit_keeps_only_the_newest(self):
        for i in range(5):
            self.log(f"run{i}.log", ["a"], age=i * 100)
        runs = logs.list_runs("editor", limit=2)
        self.assertEqual([r["file"] for r in runs], ["run0.log", "run1.log"])

    def test_a_run_reports_its_size_and_path(self):
        path = self.log("a.log", ["hello"])
        run = logs.list_runs("editor")[0]
        self.assertEqual(run["size"], path.stat().st_size)
        self.assertEqual(run["path"], str(path))

    def test_files_that_are_not_logs_are_ignored(self):
        self.log("a.log", ["x"])
        (self.folder() / "a.txt").write_text("x", encoding="utf-8")
        self.assertEqual([r["file"] for r in logs.list_runs("editor")], ["a.log"])

    def test_a_missing_folder_gives_an_empty_list(self):
        self.assertEqual(logs.list_runs("modhub"), [])

    def test_an_unknown_app_is_a_value_error(self):
        with self.assertRaises(ValueError):
            logs.list_runs("notepad")


class Read(LogCase):
    def test_errors_are_picked_out_and_ordinary_lines_are_not(self):
        self.log("main.log", [
            "info: started",
            "fail: could not load Foo",
            "Warning: something odd",
            "info: done",
        ])
        out = logs.read("editor")
        self.assertEqual(out["error_count"], 1)
        self.assertEqual(out["errors"], ["fail: could not load Foo"])
        self.assertEqual(out["warning_count"], 1)
        self.assertNotIn("warnings", out)

    def test_warnings_and_the_tail_come_with_errors_only_off(self):
        self.log("main.log", ["info: one", "Warning: careful", "info: three"])
        out = logs.read("editor", errors_only=False, tail=2)
        self.assertEqual(out["warnings"], ["Warning: careful"])
        self.assertEqual(out["tail"], ["Warning: careful", "info: three"])

    def test_repeats_that_differ_only_in_guids_and_numbers_fold_into_one_line(self):
        self.log("main.log", [
            "fail: asset 11111111-2222-3333-4444-555555555555 line 1 is invalid",
            "fail: asset aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee line 27 is invalid",
            "fail: asset 99999999-8888-7777-6666-555555555555 line 3 is invalid",
            "fail: a different problem",
        ])
        out = logs.read("editor")
        self.assertEqual(out["error_count"], 4)
        self.assertEqual(len(out["errors"]), 2)
        self.assertTrue(out["errors"][0].endswith("(x3)"))
        self.assertEqual(out["errors"][1], "fail: a different problem")

    def test_the_loose_metafile_error_gets_a_diagnosis(self):
        self.log("main.log", ["fail: Loose metafile Foo.def.meta"])
        self.assertIn("Loose metafile", logs.read("editor")["diagnosis"])

    def test_contains_filters_case_insensitively(self):
        self.log("main.log", ["alpha one", "Beta two", "alpha three"])
        out = logs.read("editor", contains="ALPHA")
        self.assertEqual(out["matches"], 2)
        self.assertEqual(out["lines"], ["alpha one", "alpha three"])

    def test_the_newest_run_is_read_not_an_old_one(self):
        self.log("old.log", ["fail: old problem"], age=10_000)
        self.log("new.log", ["fail: new problem"], age=0)
        out = logs.read("editor")
        self.assertEqual(out["files"], ["new.log"])
        self.assertEqual(out["errors"], ["fail: new problem"])

    def test_files_written_together_are_read_together_shortest_name_first(self):
        self.log("Editor_Stats.log", ["fail: from stats"], age=0)
        self.log("Editor.log", ["fail: from main"], age=10)
        self.assertEqual(logs.read("editor")["files"], ["Editor.log", "Editor_Stats.log"])

    def test_a_named_file_is_read(self):
        self.log("old.log", ["fail: in old"], age=10_000)
        self.log("new.log", ["fail: in new"])
        self.assertEqual(logs.read("editor", file_name="old.log")["errors"], ["fail: in old"])

    def test_an_unknown_file_is_a_result_not_an_exception(self):
        self.log("a.log", ["x"])
        self.assertIn("No such log file", logs.read("editor", file_name="nope.log")["error"])

    def test_a_missing_folder_is_a_result_not_an_exception(self):
        self.assertIn("No log directory", logs.read("modhub")["error"])

    def test_an_empty_folder_is_a_result_not_an_exception(self):
        self.folder()
        self.assertIn("No log files", logs.read("editor")["error"])

    def test_an_unknown_app_raises_value_error(self):
        with self.assertRaises(ValueError):
            logs.read("notepad")


if __name__ == "__main__":
    unittest.main()
