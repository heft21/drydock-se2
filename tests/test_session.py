"""Which project the session works on: discovery, resolving, the remembered choice.

The state file lives in a temp cache dir and the project roots are temp folders;
the user's real Mod HUB projects and settings are never consulted.
"""

import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests import _support  # noqa: F401  (puts the repo on sys.path)

from se2_mcp import session


class SessionCase(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = Path(tmp.name)
        self.roots = self.dir / "mods"
        self.roots.mkdir()
        self.cache = self.dir / "cache"
        patchers = [
            mock.patch.dict(os.environ, {"SE2_MCP_CACHE": str(self.cache),
                                         "SE2_MCP_MOD_ROOTS": str(self.roots)}),
            mock.patch("se2_mcp.config.default_mod_roots", return_value=[]),
            mock.patch("se2_mcp.modhub.projects", return_value=[]),
        ]
        for p in patchers:
            p.start()
            self.addCleanup(p.stop)

    def project(self, name, age=0) -> Path:
        d = self.roots / name
        d.mkdir(exist_ok=True)
        (d / f"{name}.vrgproj").write_text("{}", encoding="utf-8")
        stamp = 1_700_000_000 - age
        os.utime(d, (stamp, stamp))
        return d


class Candidates(SessionCase):
    def test_projects_under_the_roots_are_listed(self):
        a = self.project("Alpha")
        b = self.project("Beta")
        found = {c["name"]: c["path"] for c in session.candidates()}
        self.assertEqual(found, {"Alpha": str(a), "Beta": str(b)})

    def test_the_most_recently_changed_project_comes_first(self):
        self.project("Old", age=5000)
        self.project("New", age=0)
        self.assertEqual([c["name"] for c in session.candidates()], ["New", "Old"])

    def test_folders_without_a_project_file_are_not_candidates(self):
        (self.roots / "Plain").mkdir()
        self.assertEqual(session.candidates(), [])

    def test_mod_hubs_own_listing_is_read_in_the_shape_it_has(self):
        hub = self.dir / "hub"
        mine = hub / "My Folder"
        mine.mkdir(parents=True)
        (mine / "MyMod.vrgproj").write_text("{}", encoding="utf-8")
        listing = [{"name": "My Folder", "dir": str(mine), "project_file": str(mine / "MyMod.vrgproj")},
                   {"name": "Plain", "dir": str(hub / "Plain"), "project_file": None}]
        with mock.patch("se2_mcp.modhub.projects", return_value=listing):
            found = session.candidates()
        self.assertEqual([(c["name"], c["path"], c["source"]) for c in found],
                         [("MyMod", str(mine), "modhub")])

    def test_a_project_both_sources_find_is_listed_once(self):
        a = self.project("Alpha")
        listing = [{"name": "Alpha", "dir": str(a), "project_file": str(a / "Alpha.vrgproj")}]
        with mock.patch("se2_mcp.modhub.projects", return_value=listing):
            found = session.candidates()
        self.assertEqual([(c["name"], c["source"]) for c in found], [("Alpha", "modhub")])

    def test_no_roots_means_no_candidates(self):
        with mock.patch.dict(os.environ, {"SE2_MCP_MOD_ROOTS": str(self.dir / "gone")}):
            self.assertEqual(session.candidates(), [])


class Resolve(SessionCase):
    def test_a_full_path_resolves_to_the_project_folder(self):
        d = self.project("Alpha")
        self.assertEqual(session.resolve(str(d)), str(d))

    def test_a_path_to_the_project_file_resolves_to_its_folder(self):
        d = self.project("Alpha")
        self.assertEqual(session.resolve(str(d / "Alpha.vrgproj")), str(d))

    def test_a_name_resolves_case_insensitively(self):
        d = self.project("Alpha")
        self.assertEqual(session.resolve("alpha"), str(d))

    def test_a_unique_fragment_resolves(self):
        d = self.project("SuperThruster")
        self.project("Planet")
        self.assertEqual(session.resolve("thrust"), str(d))

    def test_an_ambiguous_fragment_does_not_resolve(self):
        self.project("MyPlanet")
        self.project("MyShip")
        self.assertIsNone(session.resolve("my"))

    def test_an_exact_name_beats_a_longer_one_containing_it(self):
        d = self.project("Planet")
        self.project("PlanetTwo")
        self.assertEqual(session.resolve("planet"), str(d))

    def test_an_unknown_name_and_an_empty_one_give_none(self):
        self.project("Alpha")
        self.assertIsNone(session.resolve("zzz"))
        self.assertIsNone(session.resolve(""))


class ActiveProject(SessionCase):
    def test_nothing_is_active_at_first(self):
        self.assertIsNone(session.get_active())

    def test_the_choice_is_written_to_the_state_file_and_read_back(self):
        d = self.project("Alpha")
        session.set_active(str(d))
        self.assertTrue((self.cache / session.STATE_NAME).is_file())
        self.assertEqual(session.get_active(), str(d))

    def test_a_fresh_read_of_the_state_file_still_sees_it(self):
        d = self.project("Alpha")
        session.set_active(str(d))
        # a new process knows nothing but the file: only the cache env remains
        self.assertEqual(session._read(), {"project": str(d)})
        self.assertEqual(session.get_active(), str(d))

    def test_clear_forgets_the_choice(self):
        session.set_active(str(self.project("Alpha")))
        session.clear_active()
        self.assertIsNone(session.get_active())
        self.assertEqual(session._read(), {})

    def test_a_project_that_was_deleted_is_no_longer_active(self):
        d = self.project("Alpha")
        session.set_active(str(d))
        (d / "Alpha.vrgproj").unlink()
        d.rmdir()
        self.assertIsNone(session.get_active())

    def test_a_corrupt_state_file_means_nothing_is_active(self):
        self.cache.mkdir()
        (self.cache / session.STATE_NAME).write_text("{nope", encoding="utf-8")
        self.assertIsNone(session.get_active())


class Require(SessionCase):
    def test_with_no_projects_it_explains_there_is_none(self):
        path, problem = session.require()
        self.assertIsNone(path)
        self.assertEqual(problem["status"], "no_active_project")
        self.assertEqual(problem["projects"], [])
        self.assertIn("work_on", problem["next"])

    def test_a_single_project_is_picked_and_remembered(self):
        d = self.project("Only")
        path, problem = session.require()
        self.assertEqual(path, str(d))
        self.assertIsNone(problem)
        self.assertEqual(session.get_active(), str(d))

    def test_several_projects_are_listed_and_none_is_picked(self):
        self.project("One")
        self.project("Two")
        path, problem = session.require()
        self.assertIsNone(path)
        self.assertEqual(problem["status"], "no_active_project")
        self.assertEqual(sorted(p["name"] for p in problem["projects"]), ["One", "Two"])
        self.assertIsNone(session.get_active())

    def test_the_active_project_is_used_when_there_is_one(self):
        self.project("One")
        two = self.project("Two")
        session.set_active(str(two))
        self.assertEqual(session.require(), (str(two), None))

    def test_an_explicit_project_beats_the_active_one(self):
        one = self.project("One")
        two = self.project("Two")
        session.set_active(str(two))
        self.assertEqual(session.require("one"), (str(one), None))

    def test_an_unknown_explicit_project_lists_the_known_ones(self):
        self.project("One")
        path, problem = session.require("nope")
        self.assertIsNone(path)
        self.assertEqual(problem["status"], "unknown_project")
        self.assertEqual(problem["asked_for"], "nope")
        self.assertEqual(problem["projects"], ["One"])


if __name__ == "__main__":
    unittest.main()
