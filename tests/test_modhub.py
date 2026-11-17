"""Mod HUB glue: its settings, the mod list, tasklist parsing and the launch arguments.

SETTINGS is patched to a temp file, subprocess.run / Popen are replaced in the
module under test, and the SDK is a temp folder holding empty fake executables.
Nothing real is read, listed or started.
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests import _support  # noqa: F401  (puts the repo on sys.path)

from se2_mcp import modhub
from se2_mcp.config import Paths

VANILLA = "56dacb76-e25e-468a-9432-21964a9a0569"


class ModhubCase(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)
        self.settings = self.dir / "ApplicationSettings.json"
        patcher = mock.patch.object(modhub, "SETTINGS", self.settings)
        patcher.start()
        self.addCleanup(patcher.stop)

    def set_mods_dir(self, path):
        self.settings.write_text(
            json.dumps({"$Value": {"ModsDirectory": str(path)}}), encoding="utf-8")

    def make_project(self, mods, name, *, published=False, vanilla=True, content=False):
        d = Path(mods) / name
        d.mkdir(parents=True)
        value = {"ProjectID": {"Guid": "g-" + name,
                               "ModId": {"Id": 42} if published else None,
                               "ServiceId": "steam" if published else ""},
                 "ProjectDependencies": [{"Guid": VANILLA}] if vanilla else []}
        (d / f"{name}.vrgproj").write_text(json.dumps({"$Value": value}), encoding="utf-8")
        if content:
            (d / "Content").mkdir()
        return d


class ModsDir(ModhubCase):
    def test_the_setting_wins(self):
        self.set_mods_dir(self.dir / "mine")
        self.assertEqual(modhub.mods_dir(), self.dir / "mine")

    def test_without_a_settings_file_it_falls_back_to_documents(self):
        self.assertEqual(modhub.mods_dir(),
                         Path.home() / "Documents" / "SpaceEngineers2" / "Mods")

    def test_a_settings_file_without_the_field_falls_back_too(self):
        self.settings.write_text(json.dumps({"$Value": {}}), encoding="utf-8")
        self.assertEqual(modhub.mods_dir(),
                         Path.home() / "Documents" / "SpaceEngineers2" / "Mods")

    def test_a_broken_settings_file_falls_back_too(self):
        self.settings.write_text("{nope", encoding="utf-8")
        self.assertEqual(modhub.mods_dir().name, "Mods")

    def test_a_bom_in_the_settings_file_is_tolerated(self):
        self.settings.write_text(json.dumps({"$Value": {"ModsDirectory": "X:/m"}}),
                                 encoding="utf-8-sig")
        self.assertEqual(modhub.mods_dir(), Path("X:/m"))


class Projects(ModhubCase):
    def setUp(self):
        super().setUp()
        self.mods = self.dir / "Mods"
        self.mods.mkdir()
        self.set_mods_dir(self.mods)

    def test_projects_are_listed_by_name(self):
        self.make_project(self.mods, "Beta")
        self.make_project(self.mods, "Alpha")
        self.assertEqual([p["name"] for p in modhub.projects()], ["Alpha", "Beta"])

    def test_a_published_project_carries_its_steam_id(self):
        self.make_project(self.mods, "Pub", published=True, content=True)
        item = modhub.projects()[0]
        self.assertTrue(item["published"])
        self.assertEqual(item["mod_id"], 42)
        self.assertEqual(item["service"], "steam")
        self.assertTrue(item["has_content"])
        self.assertTrue(item["depends_on_vanilla"])

    def test_an_unpublished_project_without_vanilla_says_so(self):
        self.make_project(self.mods, "Draft", vanilla=False)
        item = modhub.projects()[0]
        self.assertFalse(item["published"])
        self.assertFalse(item["depends_on_vanilla"])
        self.assertFalse(item["has_content"])

    def test_a_folder_without_a_project_file_is_listed_without_one(self):
        (self.mods / "Plain").mkdir()
        item = modhub.projects()[0]
        self.assertEqual(item["name"], "Plain")
        self.assertIsNone(item["project_file"])

    def test_loose_files_in_the_mods_folder_are_ignored(self):
        (self.mods / "readme.txt").write_text("x", encoding="utf-8")
        self.assertEqual(modhub.projects(), [])

    def test_an_unreadable_project_file_is_reported_not_raised(self):
        d = self.make_project(self.mods, "Bad")
        (d / "Bad.vrgproj").write_text("{nope", encoding="utf-8")
        self.assertIn("error", modhub.projects()[0])

    def test_a_missing_mods_folder_gives_an_empty_list(self):
        self.set_mods_dir(self.dir / "gone")
        self.assertEqual(modhub.projects(), [])


class Running(ModhubCase):
    def run_with(self, stdout=None, error=None):
        fake = mock.Mock(side_effect=error) if error else mock.Mock(
            return_value=mock.Mock(stdout=stdout))
        with mock.patch.object(modhub.subprocess, "run", fake):
            result = modhub._running("VRage.Editor")
        return result, fake

    def test_pids_are_parsed_from_csv_output(self):
        out = ('"VRage.Editor.exe","1234","Console","1","200,000 K"\n'
               '"VRage.Editor.exe","5678","Console","1","90,000 K"\n')
        result, fake = self.run_with(out)
        self.assertEqual(result, [1234, 5678])
        args = fake.call_args.args[0]
        self.assertEqual(args[0], "tasklist")
        self.assertIn("IMAGENAME eq VRage.Editor.exe", args)

    def test_the_no_tasks_message_gives_an_empty_list(self):
        result, _ = self.run_with("INFO: No tasks are running which match the specified criteria.\n")
        self.assertEqual(result, [])

    def test_other_processes_are_not_counted(self):
        result, _ = self.run_with('"notepad.exe","99","Console","1","1 K"\n')
        self.assertEqual(result, [])

    def test_a_non_numeric_pid_is_skipped(self):
        result, _ = self.run_with('"VRage.Editor.exe","abc","Console","1","1 K"\n')
        self.assertEqual(result, [])

    def test_a_failing_command_gives_an_empty_list(self):
        for error in (OSError("no tasklist"), modhub.subprocess.TimeoutExpired("tasklist", 30)):
            with self.subTest(error=type(error).__name__):
                result, _ = self.run_with(error=error)
                self.assertEqual(result, [])


class Launch(ModhubCase):
    def setUp(self):
        super().setUp()
        self.sdk = self.dir / "sdk"
        (self.sdk / "Editor").mkdir(parents=True)
        (self.sdk / "GameData").mkdir()
        patcher = mock.patch.object(modhub, "PATHS", Paths(sdk=self.sdk))
        patcher.start()
        self.addCleanup(patcher.stop)
        self.popen = mock.Mock(return_value=mock.Mock(pid=4321))
        popen = mock.patch.object(modhub.subprocess, "Popen", self.popen)
        popen.start()
        self.addCleanup(popen.stop)

        self.proj = self.dir / "mod"
        self.proj.mkdir()
        (self.proj / "Mod.vrgproj").write_text("{}", encoding="utf-8")

    def exe(self, name):
        path = self.sdk / "Editor" / name
        path.write_bytes(b"")
        return path

    def test_modhub_is_started_without_its_splash_screen(self):
        exe = self.exe("VRAGE3.ModHUB.exe")
        out = modhub.launch_modhub()
        self.assertTrue(out["ok"])
        self.assertEqual(out["pid"], 4321)
        self.assertEqual(self.popen.call_args.args[0], [str(exe), "--nosplash"])
        self.assertEqual(self.popen.call_args.kwargs["cwd"], str(self.sdk / "Editor"))

    def test_the_splash_screen_can_be_kept(self):
        exe = self.exe("VRAGE3.ModHUB.exe")
        modhub.launch_modhub(no_splash=False)
        self.assertEqual(self.popen.call_args.args[0], [str(exe)])

    def test_a_missing_modhub_exe_is_reported_not_raised(self):
        out = modhub.launch_modhub()
        self.assertFalse(out["ok"])
        self.assertIn("Not found", out["error"])
        self.popen.assert_not_called()

    def test_the_editor_gets_the_documented_arguments(self):
        exe = self.exe("VRage.Editor.exe")
        out = modhub.launch_editor(str(self.proj))
        self.assertTrue(out["ok"])
        args = self.popen.call_args.args[0]
        self.assertEqual(args, [
            str(exe), "--project", str(self.proj / "Mod.vrgproj"),
            "--globalProjectDirs", str(self.sdk / "GameData"),
            str(self.sdk / "VRage" / "GameData"),
            "--globalAssemblyDirs", str(self.sdk / "Editor"),
        ])
        self.assertEqual(out["project"], str(self.proj / "Mod.vrgproj"))

    def test_the_game_folder_is_added_when_it_exists(self):
        self.exe("VRage.Editor.exe")
        game = self.dir / "SpaceEngineers2" / "Game2"
        game.mkdir(parents=True)
        modhub.launch_editor(str(self.proj / "Mod.vrgproj"))
        args = self.popen.call_args.args[0]
        self.assertEqual(args[-2:], ["--projectExecutableSearchPaths", str(game)])

    def test_a_missing_editor_exe_is_reported_not_raised(self):
        out = modhub.launch_editor(str(self.proj))
        self.assertFalse(out["ok"])
        self.assertIn("Not found", out["error"])
        self.popen.assert_not_called()

    def test_a_folder_without_a_project_file_is_reported(self):
        self.exe("VRage.Editor.exe")
        empty = self.dir / "empty"
        empty.mkdir()
        out = modhub.launch_editor(str(empty))
        self.assertFalse(out["ok"])
        self.assertIn("No .vrgproj", out["error"])
        self.popen.assert_not_called()

    def test_a_project_path_that_does_not_exist_is_reported(self):
        self.exe("VRage.Editor.exe")
        out = modhub.launch_editor(str(self.dir / "nope.vrgproj"))
        self.assertFalse(out["ok"])
        self.assertIn("does not exist", out["error"])

    def test_a_process_that_cannot_start_is_reported_not_raised(self):
        self.exe("VRAGE3.ModHUB.exe")
        self.popen.side_effect = OSError("blocked")
        out = modhub.launch_modhub()
        self.assertFalse(out["ok"])
        self.assertIn("blocked", out["error"])


if __name__ == "__main__":
    unittest.main()
