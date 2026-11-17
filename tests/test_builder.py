"""The content-pipeline wrapper: arguments passed, output summarised, failures reported.

subprocess.run is replaced in the module under test and the SDK is a temp folder
with an empty fake builder exe, so the real builder is never started.
"""

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests import _support  # noqa: F401  (puts the repo on sys.path)

from se2_mcp import builder
from se2_mcp.config import Paths


def completed(stdout="", stderr="", code=0):
    return mock.Mock(stdout=stdout, stderr=stderr, returncode=code)


class BuilderCase(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)
        self.sdk = self.dir / "sdk"
        (self.sdk / "Editor").mkdir(parents=True)
        (self.sdk / "GameData").mkdir()
        self.exe = self.sdk / "Editor" / "VRage.ContentPipeline.Builder.exe"
        self.exe.write_bytes(b"")
        patcher = mock.patch.object(builder, "PATHS", Paths(sdk=self.sdk))
        patcher.start()
        self.addCleanup(patcher.stop)

        self.proj_dir = self.dir / "mod"
        self.proj_dir.mkdir()
        self.proj = self.proj_dir / "Mod.vrgproj"
        self.proj.write_text("{}", encoding="utf-8")

    def patch_run(self, **kw):
        fake = mock.Mock(**kw)
        patcher = mock.patch.object(builder.subprocess, "run", fake)
        patcher.start()
        self.addCleanup(patcher.stop)
        return fake


class Run(BuilderCase):
    def test_the_project_and_the_global_dirs_are_passed(self):
        fake = self.patch_run(return_value=completed("all good"))
        out = builder.run(str(self.proj_dir))
        args = fake.call_args.args[0]
        self.assertEqual(args[:3], [str(self.exe), "-p", str(self.proj)])
        self.assertEqual(args[args.index("--globalProjectDirs") + 1], str(self.sdk / "GameData"))
        self.assertEqual(args[args.index("--globalAssemblyDirs") + 1], str(self.sdk / "Editor"))
        self.assertEqual(fake.call_args.kwargs["cwd"], str(self.sdk / "Editor"))
        self.assertTrue(out["ok"])
        self.assertEqual(out["exit_code"], 0)
        self.assertEqual(out["project"], str(self.proj))

    def test_a_project_file_path_is_accepted_as_well_as_a_folder(self):
        fake = self.patch_run(return_value=completed())
        builder.run(str(self.proj))
        self.assertEqual(fake.call_args.args[0][2], str(self.proj))

    def test_each_option_adds_its_flag(self):
        fake = self.patch_run(return_value=completed())
        builder.run(str(self.proj), dry_run=True, generate_caches=True, metadata=True,
                    prepare_for_publish="Out", resave="Everything", verbose=True)
        args = fake.call_args.args[0]
        for flag in ("-d", "--generateCaches", "--metadata", "-v"):
            self.assertIn(flag, args)
        self.assertEqual(args[args.index("--prepareForPublish") + 1], "Out")
        self.assertEqual(args[args.index("-r") + 1], "Everything")

    def test_no_options_means_no_optional_flags(self):
        fake = self.patch_run(return_value=completed())
        builder.run(str(self.proj))
        args = fake.call_args.args[0]
        for flag in ("-d", "--generateCaches", "--metadata", "-v", "-r", "--prepareForPublish"):
            self.assertNotIn(flag, args)

    def test_errors_and_warnings_are_summarised_from_both_streams(self):
        self.patch_run(return_value=completed(
            stdout="info: start\nfail: bad thing\n",
            stderr="Warning: odd thing\nexception: crashed\n", code=1))
        out = builder.run(str(self.proj))
        self.assertFalse(out["ok"])
        self.assertEqual(out["exit_code"], 1)
        self.assertEqual(out["error_count"], 2)
        self.assertEqual(out["errors"], ["fail: bad thing", "exception: crashed"])
        self.assertEqual(out["warning_count"], 1)
        self.assertEqual(out["warnings"], ["Warning: odd thing"])
        self.assertNotIn("diagnosis", out)

    def test_repeats_differing_only_in_numbers_and_quoted_names_are_folded(self):
        lines = "".join(f"fail: asset 'Name{i}' step {i} is invalid\n" for i in range(6))
        self.patch_run(return_value=completed(stdout=lines + "fail: other\n", code=1))
        out = builder.run(str(self.proj))
        self.assertEqual(out["error_count"], 7)
        self.assertEqual(len(out["errors"]), 2)
        self.assertTrue(out["errors"][0].endswith("(x6)"))

    def test_the_tail_is_the_last_twelve_lines(self):
        self.patch_run(return_value=completed(stdout="".join(f"line {i}\n" for i in range(30))))
        out = builder.run(str(self.proj))
        self.assertEqual(len(out["tail"]), 12)
        self.assertEqual(out["tail"][-1], "line 29")

    def test_loose_metafiles_get_the_vanilla_diagnosis(self):
        self.patch_run(return_value=completed(stdout="fail: Loose metafile X.meta\n", code=1))
        self.assertIn("Vanilla", builder.run(str(self.proj))["diagnosis"])

    def test_missing_outputs_get_the_caches_hint(self):
        self.patch_run(return_value=completed(stdout="fail: output does not exist\n", code=1))
        self.assertIn("caches", builder.run(str(self.proj))["diagnosis"])

    def test_a_timeout_is_reported_as_a_result(self):
        self.patch_run(side_effect=subprocess.TimeoutExpired("builder", 5))
        out = builder.run(str(self.proj), timeout=5)
        self.assertFalse(out["ok"])
        self.assertIn("timed out after 5s", out["error"])

    def test_the_timeout_is_handed_to_subprocess(self):
        fake = self.patch_run(return_value=completed())
        builder.run(str(self.proj), timeout=77)
        self.assertEqual(fake.call_args.kwargs["timeout"], 77)

    def test_a_missing_builder_exe_is_a_result_and_nothing_is_started(self):
        fake = self.patch_run(return_value=completed())
        self.exe.unlink()
        out = builder.run(str(self.proj))
        self.assertFalse(out["ok"])
        self.assertIn("Builder not found", out["error"])
        fake.assert_not_called()

    def test_a_project_that_does_not_exist_raises_file_not_found(self):
        self.patch_run(return_value=completed())
        with self.assertRaises(FileNotFoundError):
            builder.run(str(self.dir / "nope"))
        with self.assertRaises(FileNotFoundError):
            builder.run(str(self.dir))


class Version(BuilderCase):
    def test_the_first_line_of_output_is_the_version(self):
        fake = self.patch_run(return_value=completed(stdout="VRage Builder v.1.2.3\nmore\n"))
        self.assertEqual(builder.version(), "VRage Builder v.1.2.3")
        self.assertEqual(fake.call_args.args[0], [str(self.exe), "--version"])

    def test_stderr_is_used_when_stdout_is_empty(self):
        self.patch_run(return_value=completed(stderr="v.9\n"))
        self.assertEqual(builder.version(), "v.9")

    def test_no_output_at_all_gives_a_question_mark(self):
        self.patch_run(return_value=completed())
        self.assertEqual(builder.version(), "?")

    def test_a_missing_exe_is_reported_not_raised(self):
        self.exe.unlink()
        self.patch_run(return_value=completed())
        self.assertEqual(builder.version(), "builder not found")

    def test_a_failure_to_run_is_reported_not_raised(self):
        for error in (OSError("blocked"), subprocess.TimeoutExpired("builder", 60)):
            with self.subTest(error=type(error).__name__):
                self.patch_run(side_effect=error)
                self.assertTrue(builder.version().startswith("unavailable ("))


if __name__ == "__main__":
    unittest.main()
