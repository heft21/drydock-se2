"""The offline project audit: each defect it knows is reported, a clean project is not.

Every project here is scaffolded in a temp dir; the vanilla index is never needed
because no test references shipped content (an unknown GUID is unknown either way).
"""

import json
import unittest

from tests._support import TempProject

from se2_mcp import audit, authoring

TYPE = "VRage:Keen.VRage.Voxels.Definitions.VoxelMaterialDefinition"
GUID_A = "aaaaaaaa-0000-4000-8000-000000000001"
GUID_B = "bbbbbbbb-0000-4000-8000-000000000002"
GUID_GONE = "cccccccc-0000-4000-8000-000000000003"


class Audit(TempProject):
    def setUp(self):
        super().setUp()
        self.proj = self.dir / "mod"
        authoring.scaffold_mod(self.proj, "AuditMod")

    def add_def(self, name="Thing.def", guid=GUID_A, **fields):
        value = {"Guid": guid, "Name": name, **fields}
        authoring.write_definition(self.proj / "Assets" / name, TYPE, value)
        return self.proj / "Assets" / name

    def kinds(self, **kw):
        return {f["kind"] for f in audit.audit(self.proj, **kw)["findings"]}

    def test_a_clean_scaffolded_project_audits_ok(self):
        self.add_def()
        report = audit.audit(self.proj)
        self.assertTrue(report["ok"], report["findings"])
        self.assertEqual(report["error_count"], 0)
        self.assertEqual(report["inventory"]["definitions"], 1)

    def test_a_missing_meta_is_reported(self):
        path = self.add_def()
        path.with_name(path.name + ".meta").unlink()
        self.assertIn("meta_missing", self.kinds())

    def test_a_stale_hash_is_reported_only_when_hashes_are_checked(self):
        path = self.add_def()
        path.write_bytes(path.read_bytes() + b"\r\n")
        self.assertIn("hash_stale", self.kinds(check_hashes=True))
        self.assertNotIn("hash_stale", self.kinds(check_hashes=False))

    def test_a_reference_to_nothing_is_reported(self):
        self.add_def(Other=GUID_GONE)
        report = audit.audit(self.proj)
        hits = [f for f in report["findings"] if f["kind"] == "unresolved_ref"]
        self.assertEqual([h["guid"] for h in hits], [GUID_GONE])
        self.assertFalse(report["ok"])

    def test_a_reference_to_another_file_of_the_project_resolves(self):
        self.add_def("A.def", GUID_A, Other=GUID_B)
        self.add_def("B.def", GUID_B)
        self.assertNotIn("unresolved_ref", self.kinds())

    def test_two_files_claiming_one_guid_are_reported(self):
        self.add_def("A.def", GUID_A)
        self.add_def("B.def", GUID_A)
        self.assertIn("duplicate_guid", self.kinds())

    def test_a_meta_without_its_source_file_is_reported(self):
        path = self.add_def()
        path.unlink()
        self.assertIn("meta_orphan", self.kinds())

    def test_a_meta_assetid_that_differs_from_the_definition_is_reported(self):
        path = self.add_def()
        meta = path.with_name(path.name + ".meta")
        meta.write_bytes(meta.read_bytes().replace(GUID_A.encode(), GUID_B.encode()))
        self.assertIn("assetid_mismatch", self.kinds())

    def test_a_folder_without_a_meta_is_reported(self):
        (self.proj / "Assets" / "Sub").mkdir()
        self.assertIn("folder_meta", self.kinds())

    def test_a_missing_assets_meta_is_reported(self):
        (self.proj / "Assets.meta").unlink()
        self.assertIn("folder_meta", self.kinds())

    def test_a_definition_without_a_guid_is_reported(self):
        path = self.proj / "Assets" / "NoGuid.def"
        path.write_bytes(authoring.serialize({"$Type": TYPE, "$Value": {"Name": "x"}}))
        self.assertIn("def_no_guid", self.kinds())

    def test_a_definition_that_is_not_json_is_reported(self):
        (self.proj / "Assets" / "Broken.def").write_text("{nope", encoding="utf-8")
        self.assertIn("def_unreadable", self.kinds())

    def test_an_empty_definition_set_list_is_reported(self):
        proj_file = self.proj / "AuditMod.vrgproj"
        doc = json.loads(proj_file.read_text(encoding="utf-8"))
        doc["$Value"]["DefinitionSetNames"] = []
        proj_file.write_bytes(authoring.serialize(doc))
        self.assertIn("project", self.kinds())

    def test_the_editor_bridge_in_the_project_is_listed_not_flagged(self):
        # The audit does not call the bridge an error; finish_and_publish does.
        proj_file = self.proj / "AuditMod.vrgproj"
        doc = json.loads(proj_file.read_text(encoding="utf-8"))
        doc["$Value"]["EditorExtensionAssemblies"] = ["SE2McpBridge.dll"]
        proj_file.write_bytes(authoring.serialize(doc))
        report = audit.audit(self.proj)
        self.assertEqual(report["project_info"]["editor_extensions"], ["SE2McpBridge.dll"])
        self.assertTrue(report["ok"])

    def test_a_path_that_is_not_a_project_gives_an_error_not_an_exception(self):
        report = audit.audit(self.dir / "does-not-exist")
        self.assertIn("error", report)
        empty = self.dir / "empty"
        empty.mkdir()
        self.assertIn("error", audit.audit(empty))

    def test_a_project_without_assets_gives_an_error(self):
        (self.dir / "bare").mkdir()
        (self.dir / "bare" / "X.vrgproj").write_text("{}", encoding="utf-8")
        self.assertIn("No Assets/", audit.audit(self.dir / "bare")["error"])


if __name__ == "__main__":
    unittest.main()
