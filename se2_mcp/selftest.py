"""End-to-end check that this server actually works on this machine.

Most of what can go wrong with an MCP server goes wrong silently: the SDK is
somewhere else, the index was built against a different install, the field
documentation never got extracted. Each of those surfaces later as one tool
returning something odd, which is a poor place to start debugging from.

So this runs the real paths once and says which step broke. The write check
scaffolds a project in a temporary directory, authors a definition into it and
audits the result — the whole authoring loop, on disposable files, touching
nothing the user owns.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import time
from pathlib import Path
from typing import Any, Callable

from . import (audit, authoring, blender, bridge, builder, docs, index, knowledge,
               modhub, recipes)
from .config import PATHS


class Check(dict):
    def __init__(self, name: str, ok: bool, detail: Any, advice: str = ""):
        super().__init__(check=name, ok=ok, detail=detail)
        if advice and not ok:
            self["fix"] = advice


def _timed(fn: Callable[[], Any]) -> tuple[Any, float]:
    started = time.time()
    return fn(), round(time.time() - started, 2)


def _check_paths() -> Check:
    problems = PATHS.check()
    return Check(
        "sdk_paths", not problems,
        problems or {"sdk_root": str(PATHS.sdk), "game_data": str(PATHS.game_data)},
        "Set SE2_MODSDK to the 'Space Engineers 2 - Mod SDK' folder Steam "
        "installed, the one containing GameData and Editor.",
    )


def _check_pipeline() -> Check:
    version = builder.version()
    ok = "v." in version
    return Check(
        "content_pipeline", ok, version,
        "VRage.ContentPipeline.Builder.exe did not answer. Verify the SDK "
        "install through Steam.",
    )


def _check_index() -> Check:
    missing = not PATHS.db_path.exists()
    # Unlike a tool call, the self test is allowed to sit and wait: the whole
    # point of running it is to find out whether the slow parts work.
    index.ensure(wait=900)
    status = index.index_status()
    stats = status.get("stats") or {}
    ok = bool(status.get("built")) and stats.get("definitions", 0) > 0
    detail: dict[str, Any] = {
        "definitions": stats.get("definitions"),
        "media_assets": stats.get("media_assets"),
        "reference_edges": stats.get("reference_edges"),
        "parse_errors": stats.get("parse_errors"),
        "projects": [Path(p).name for p in status.get("roots", [])],
    }
    if missing:
        detail["built_during_this_check"] = True
    if status.get("stale"):
        detail["stale"] = status["stale"]
    return Check("definition_index", ok, detail,
                 "Call build_index, or check that GameData/Vanilla exists.")


def _check_field_docs() -> Check:
    if not docs.is_built():
        docs.build()
    built = docs.is_built()
    sample = docs.type_doc(
        "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.PlacementDefinitionObjectBuilder"
    )
    n = len(sample["documented_fields"])
    return Check("field_documentation", built and n > 0,
                 {"cache_built": built, "fields_for_sample_type": n},
                 "Call build_index; the SDK's *.xml files sit next to Editor/.")


def _check_lookup() -> Check:
    """Resolve a real GUID and read the file behind it, index to disk."""
    conn = index.connect(read_only=True)
    try:
        row = conn.execute(
            "SELECT guid, path, stem FROM assets WHERE project='Vanilla' "
            "AND kind='def' ORDER BY LENGTH(path) LIMIT 1"
        ).fetchone()
        if row is None:
            return Check("read_definition", False, "No vanilla definitions indexed.",
                         "Call build_index.")
        path = PATHS.game_data / row["path"]
        if not path.is_file():
            return Check("read_definition", False,
                         {"indexed_path": row["path"], "resolved": str(path)},
                         "The index points at a file that is gone. Call build_index.")
        doc = json.loads(path.read_text(encoding="utf-8-sig"))
        refs = {g for g, _ in index._walk_guids(doc.get("$Value", {}))}
        return Check("read_definition", "$Type" in doc, {
            "example": row["stem"],
            "type": doc.get("$Type"),
            "outgoing_guid_references": len(refs),
        })
    finally:
        conn.close()


def _check_knowledge() -> Check:
    topics = knowledge.get("index").get("topics") or {}
    procedures = recipes.get("index").get("topics") or {}
    ok = len(topics) >= 5 and len(procedures) >= 5
    return Check("knowledge_base", ok,
                 {"explain_topics": sorted(topics), "recipes": sorted(procedures)})


def _check_authoring() -> Check:
    """Scaffold, write and audit a throwaway project — the whole write loop."""
    tmp = Path(tempfile.mkdtemp(prefix="se2-mcp-selftest-"))
    try:
        project = authoring.scaffold_mod(tmp, "SelfTestMod", depend_on_vanilla=True)
        guid = authoring.new_guid()
        target = tmp / "Assets" / "SelfTestMaterial.def"
        written = authoring.write_definition(
            target,
            "VRage:Keen.VRage.Voxels.Definitions.VoxelMaterialDefinition",
            {"Guid": guid, "Name": "SelfTestMaterial"},
        )
        # A folder without its own .meta is not mounted, so the audit would
        # rightly complain; Assets/ itself is covered by Assets.meta.
        report = audit.audit(tmp)
        stored = json.loads(
            (target.with_name(target.name + ".meta")).read_text(encoding="utf-8-sig")
        )
        hashed = authoring.file_hash(target.read_bytes())
        hash_matches = any(
            item.get("FileHash") == hashed
            for item in stored["$Value"]["InternalItems"]
            if isinstance(item, dict)
        )
        ok = report.get("ok", False) and hash_matches and written["guid"] == guid
        return Check("authoring_round_trip", ok, {
            "scaffolded": Path(project["project_file"]).name,
            "publish_metadata_written": Path(project["publish_metadata"]).is_file(),
            "definition_bytes": written["bytes"],
            "meta_hash_matches_file": hash_matches,
            "audit_ok": report.get("ok"),
            "audit_findings": report.get("findings", [])[:5],
        }, "write_definition or audit_project disagree about what a valid "
           "project looks like; this is a bug in the server, not in your mod.")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _live_apps() -> dict[str, Any]:
    """Optional companions. Absent ones are reported, never counted as failures."""
    out: dict[str, Any] = {}

    out["editor_bridge"] = {
        "plugin_built": bridge.plugin_built(),
        "connected": bridge.is_up(),
        "url": bridge.base_url(),
    }
    out["blender"] = {"connected": blender.is_up(), "address": blender.address()}
    try:
        status = modhub.status()
        out["modhub"] = {
            "mods_directory": status.get("mods_directory"),
            "running": bool(status.get("modhub_running_pids")),
            "editor_running": bool(status.get("editor_running_pids")),
        }
    except OSError as exc:
        out["modhub"] = {"error": str(exc)}
    return out


REQUIRED: tuple[Callable[[], Check], ...] = (
    _check_paths,
    _check_pipeline,
    _check_index,
    _check_field_docs,
    _check_lookup,
    _check_knowledge,
    _check_authoring,
)


def run(include_live_apps: bool = True) -> dict[str, Any]:
    checks: list[Check] = []
    for fn in REQUIRED:
        try:
            check, seconds = _timed(fn)
        except Exception as exc:                 # a broken check is a failure
            check = Check(fn.__name__.removeprefix("_check_"), False,
                          f"{type(exc).__name__}: {exc}")
            seconds = 0.0
        check["seconds"] = seconds
        checks.append(check)
        # Everything after a missing SDK would fail for the same reason.
        if check["check"] == "sdk_paths" and not check["ok"]:
            break

    failed = [c["check"] for c in checks if not c["ok"]]
    result: dict[str, Any] = {
        "ok": not failed,
        "checks": checks,
        "failed": failed or None,
        "summary": (
            f"{len(checks) - len(failed)}/{len(checks)} checks passed."
            if failed else
            f"All {len(checks)} checks passed: reading, authoring and auditing "
            f"all work on this install."
        ),
    }
    if include_live_apps:
        result["live_apps"] = _live_apps()
        result["live_apps_note"] = (
            "These are optional. The editor bridge is needed only for editor_* "
            "tools, Blender only for blender_* tools; neither being present "
            "affects reading or authoring content."
        )
    return result


def main() -> int:
    """CLI entry point: python -m se2_mcp --selftest"""
    report = run()
    for check in report["checks"]:
        mark = "PASS" if check["ok"] else "FAIL"
        print(f"[{mark}] {check['check']} ({check['seconds']}s)")
        if not check["ok"]:
            print(f"       {check['detail']}")
            if "fix" in check:
                print(f"       fix: {check['fix']}")
    print()
    print(report["summary"])
    for name, info in (report.get("live_apps") or {}).items():
        print(f"  {name}: {info}")
    return 0 if report["ok"] else 1
