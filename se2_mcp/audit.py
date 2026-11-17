"""Offline consistency audit for a mod project.

The SDK's own validator (``VRage.ContentPipeline.Builder.exe``) cannot load any
project that depends on Vanilla — the shipped Vanilla project carries ~384
orphaned ``.meta`` files and the CLI has no stripped mode. Since every real mod
depends on Vanilla, that leaves the most common project shape with no offline
check at all: the only authority is the editor, which has to be running.

This module fills that gap. It reproduces the checks the pipeline performs that
can be done from the files alone, resolving cross-project references against the
search index:

* ``meta_missing``      asset file with no ``.meta`` sidecar — invisible to the pipeline
* ``meta_orphan``       ``.meta`` whose source file is gone — "Loose metafile", fatal
* ``hash_stale``        ``.meta`` FileHash does not match the file's bytes
* ``assetid_mismatch``  definition's own GUID differs from its ``.meta`` AssetID
* ``duplicate_guid``    two files claim the same GUID
* ``unresolved_ref``    a referenced GUID exists nowhere — in the project or in the index
* ``folder_meta``       directory with no ``.meta``, so its contents are not mounted
* ``project``           ``.vrgproj`` sanity: dependencies, definition sets

Reference walking covers more than ``.def``/``.partialdef``: planet cubemaps,
cubemaps and composed textures are JSON asset files that reference other assets
by GUID too, and the index does not record their edges.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Iterator

from . import index
from .authoring import file_hash
from .config import DEF_SUFFIXES, PATHS, normalize_guid

# Asset files whose *content* is JSON carrying GUID references. The index treats
# these as opaque media (GUID from the .meta only), so their outgoing edges are
# invisible to find_references and have to be walked here.
REFERENCING_CONTENT = {".planetcubemap", ".cubemap", ".comptex", ".fbxsettings"}

# GUID-valued fields that name a type, a dictionary key or a state-machine node
# rather than an asset. They have no file behind them by design, so flagging
# them as unresolved would bury the real findings.
NON_ASSET_FIELDS = (".Key", "Keys", ".Id", "Removed", "Version", "Patterns")

# Sidecars whose InternalItems are empty are markers (folders, definition sets),
# not processed assets, so they carry no hash to check.
_HASH_ITEM = "FileInfoMetaDataItem"


def _is_key_field(field: str) -> bool:
    return any(tok in field for tok in NON_ASSET_FIELDS)


def _iter_refs(node: Any, prefix: str = "") -> Iterator[tuple[str, str]]:
    yield from index._walk_guids(node, prefix)


def _meta_of(path: Path) -> Path:
    return path.with_name(path.name + ".meta")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def _meta_asset_id(doc: Any) -> str | None:
    if not isinstance(doc, dict):
        return None
    raw = doc.get("$Value", {}).get("AssetID")
    return normalize_guid(raw) if isinstance(raw, str) else None


def _meta_hash(doc: Any) -> str | None:
    """The stored content hash, or None for marker sidecars that carry none."""
    items = doc.get("$Value", {}).get("InternalItems") or []
    for item in items:
        if isinstance(item, dict) and _HASH_ITEM in str(item.get("$Type", "")):
            h = item.get("FileHash")
            if isinstance(h, str):
                return h
    return None


def _project_file(root: Path) -> Path | None:
    if root.is_file() and root.suffix == ".vrgproj":
        return root
    found = sorted(root.glob("*.vrgproj"))
    return found[0] if found else None


class Finding(dict):
    """A single audit result, ordered so the severity reads first."""

    def __init__(self, severity: str, kind: str, path: str, detail: str, **extra: Any):
        super().__init__(severity=severity, kind=kind, path=path, detail=detail, **extra)


def audit(project: str | Path, *, check_hashes: bool = True,
          max_findings: int = 200) -> dict[str, Any]:
    """Audit a mod project without opening the editor or the CLI."""
    root = Path(project)
    proj_file = _project_file(root)
    if proj_file is None:
        return {"error": f"No .vrgproj found in {root}"}
    root = proj_file.parent
    assets = root / "Assets"
    if not assets.is_dir():
        return {"error": f"No Assets/ directory in {root}"}

    findings: list[Finding] = []
    def add(sev: str, kind: str, path: Path | str, detail: str, **extra: Any) -> None:
        if len(findings) < max_findings:
            rel = str(Path(path).relative_to(root)) if isinstance(path, Path) else str(path)
            findings.append(Finding(sev, kind, rel, detail, **extra))

    # ---- inventory -------------------------------------------------------
    owned: dict[str, Path] = {}          # GUID -> file that declares it
    definitions: list[Path] = []
    media: list[Path] = []
    metas: list[Path] = []
    counts = {"definitions": 0, "media": 0, "folders": 0}

    for path in sorted(assets.rglob("*")):
        if path.is_dir():
            counts["folders"] += 1
            if not _meta_of(path).is_file():
                add("error", "folder_meta", path,
                    "Directory has no .meta sidecar, so the pipeline does not "
                    "mount its contents.")
            continue
        if path.suffix == ".meta":
            metas.append(path)
            continue
        if path.suffix in DEF_SUFFIXES:
            definitions.append(path)
            counts["definitions"] += 1
        else:
            media.append(path)
            counts["media"] += 1

    # Assets.meta itself marks the definition set; it lives beside Assets/.
    assets_meta = root / "Assets.meta"
    if not assets_meta.is_file():
        add("error", "folder_meta", assets_meta,
            "Assets.meta is missing; without it Assets/ is not a definition set.")

    # ---- .meta sidecars --------------------------------------------------
    for meta_path in metas:
        source = meta_path.with_name(meta_path.name[: -len(".meta")])
        try:
            doc = _read_json(meta_path)
        except (json.JSONDecodeError, OSError) as exc:
            add("error", "meta_unreadable", meta_path, f"Cannot parse .meta: {exc}")
            continue

        asset_id = _meta_asset_id(doc)
        if not asset_id:
            add("error", "meta_no_assetid", meta_path, ".meta has no AssetID.")
            continue

        if not source.exists():
            add("error", "meta_orphan", meta_path,
                f"Source file '{source.name}' does not exist. This is the "
                f"'Loose metafile' condition — it fails the content pipeline.")
            continue

        prior = owned.get(asset_id)
        if prior is not None and prior != source:
            add("error", "duplicate_guid", meta_path,
                f"AssetID {asset_id} is already claimed by "
                f"{prior.relative_to(root)}.", guid=asset_id)
        owned[asset_id] = source

        if check_hashes and source.is_file():
            stored = _meta_hash(doc)
            if stored is not None:
                actual = file_hash(source.read_bytes())
                if stored != actual:
                    add("error", "hash_stale", source,
                        f"FileHash in .meta is {stored}, file hashes to {actual}. "
                        f"Run refresh_meta.", guid=asset_id)

    # ---- definitions: own GUID vs .meta, and outgoing references ---------
    refs: list[tuple[str, str, Path]] = []   # (guid, field, source file)
    for path in definitions:
        try:
            doc = _read_json(path)
        except (json.JSONDecodeError, OSError) as exc:
            add("error", "def_unreadable", path, f"Cannot parse definition: {exc}")
            continue
        value = doc.get("$Value")
        if not isinstance(value, dict):
            add("error", "def_no_value", path, "Definition has no $Value object.")
            continue

        own = index._own_guid(path.suffix.lstrip("."), value)
        is_override = value.get("PartialDefinitionKind") == "Override"

        if not own and is_override:
            # An Override changes an existing definition instead of declaring a
            # new one, so it legitimately carries no Guid; its identity is the
            # sidecar's AssetID. What it does need is a resolvable base.
            own = index._meta_asset_id(path)
            base = normalize_guid(value.get("BaseDefinition") or "")
            if not base:
                add("error", "override_no_base", path,
                    "Override partialdef has no BaseDefinition, so there is "
                    "nothing for it to modify.")
            else:
                refs.append((base, "BaseDefinition", path))
            if not own:
                add("error", "meta_missing", path,
                    "Override partialdef has no .meta, and an Override carries "
                    "no Guid of its own — the sidecar is its only identity.")
        elif not own:
            add("error", "def_no_guid", path,
                "Definition declares no Guid (.def needs $Value.Guid, "
                ".partialdef needs $Value.Manipulator.Guid).")

        if own:
            meta_path = _meta_of(path)
            if not meta_path.is_file():
                add("error", "meta_missing", path,
                    "Definition has no .meta sidecar; the pipeline will not see it.")
            else:
                try:
                    mid = _meta_asset_id(_read_json(meta_path))
                    if mid and mid != own:
                        add("error", "assetid_mismatch", path,
                            f"Definition GUID is {own} but .meta AssetID is {mid}.")
                except (json.JSONDecodeError, OSError):
                    pass

        for guid, field in _iter_refs(value):
            if guid != own:
                refs.append((guid, field, path))

    # Media files that are themselves JSON reference other assets.
    for path in media:
        if path.suffix.lower() not in REFERENCING_CONTENT:
            if not _meta_of(path).is_file():
                add("error", "meta_missing", path,
                    "Asset file has no .meta sidecar; it will not be mounted.")
            continue
        if not _meta_of(path).is_file():
            add("error", "meta_missing", path, "Asset file has no .meta sidecar.")
        try:
            doc = _read_json(path)
        except (json.JSONDecodeError, OSError) as exc:
            add("error", "asset_unreadable", path, f"Cannot parse asset JSON: {exc}")
            continue
        for guid, field in _iter_refs(doc.get("$Value", doc)):
            refs.append((guid, field, path))

    # ---- reference resolution -------------------------------------------
    unknown: dict[str, tuple[str, Path]] = {}
    conn: sqlite3.Connection | None = None
    try:
        conn = index.connect(read_only=True)
    except (FileNotFoundError, sqlite3.DatabaseError):
        conn = None

    external = 0
    for guid, field, src in refs:
        if guid in owned:
            continue
        if _is_key_field(field):
            continue
        if conn is not None:
            hit = conn.execute(
                "SELECT 1 FROM assets WHERE guid=? UNION ALL "
                "SELECT 1 FROM files WHERE guid=? UNION ALL "
                "SELECT 1 FROM nested WHERE guid=? LIMIT 1",
                (guid, guid, guid),
            ).fetchone()
            if hit:
                external += 1
                continue
        unknown.setdefault(guid, (field, src))
    if conn is not None:
        conn.close()

    for guid, (field, src) in unknown.items():
        add("error", "unresolved_ref", src,
            f"References {guid} at '{field}', which is not in this project nor "
            f"in the indexed SDK content.", guid=guid, field=field)

    # ---- project file ----------------------------------------------------
    project_info: dict[str, Any] = {}
    try:
        pdoc = _read_json(proj_file)
        pv = pdoc.get("$Value", {})
        deps = [d.get("Guid") for d in pv.get("ProjectDependencies") or []]
        project_info = {
            "name": pv.get("Name"),
            "type": pv.get("Type"),
            "project_guid": (pv.get("ProjectID") or {}).get("Guid"),
            "mod_id": (pv.get("ProjectID") or {}).get("ModId"),
            "definition_sets": pv.get("DefinitionSetNames"),
            "depends_on_vanilla": "56dacb76-e25e-468a-9432-21964a9a0569" in deps,
            "depends_on_engine": "079da0f2-4755-491e-8688-b68b91b2fad3" in deps,
            "editor_extensions": pv.get("EditorExtensionAssemblies"),
        }
        if not project_info["definition_sets"]:
            add("error", "project", proj_file,
                "DefinitionSetNames is empty; the game mounts nothing.")
        if not deps:
            add("warning", "project", proj_file,
                "No ProjectDependencies. A mod that references base-game content "
                "needs the Vanilla project (56dacb76-e25e-468a-9432-21964a9a0569).")
        # The definition set named in Assets.meta must be one the project mounts.
        if assets_meta.is_file():
            try:
                items = _read_json(assets_meta).get("$Value", {}).get("InternalItems") or []
                declared = [i.get("DefinitionSetName") for i in items
                            if isinstance(i, dict) and "DefinitionSetItem" in str(i.get("$Type", ""))]
                project_info["assets_definition_set"] = declared or None
                names = project_info["definition_sets"] or []
                if not declared:
                    add("error", "definition_set", assets_meta,
                        "Assets.meta declares no DefinitionSetItem, so nothing "
                        "inside Assets/ is mounted as a definition set. The "
                        "project expects " + ", ".join(names) + ".")
                else:
                    for d in declared:
                        if d not in names:
                            add("error", "definition_set", assets_meta,
                                f"Assets.meta declares definition set '{d}', but "
                                f"the project mounts {names}.")
            except (json.JSONDecodeError, OSError):
                pass
    except (json.JSONDecodeError, OSError) as exc:
        add("error", "project", proj_file, f"Cannot parse .vrgproj: {exc}")

    errors = [f for f in findings if f["severity"] == "error"]
    warnings = [f for f in findings if f["severity"] == "warning"]
    return {
        "project": str(proj_file),
        "ok": not errors,
        "project_info": project_info,
        "inventory": {
            **counts,
            "guids_declared": len(owned),
            "references_walked": len(refs),
            "references_external": external,
        },
        "error_count": len(errors),
        "warning_count": len(warnings),
        "findings": errors + warnings,
        "note": (
            "This is the offline equivalent of the pipeline's structural checks, "
            "usable on Vanilla-dependent projects that validate_project cannot "
            "load. It does not replace editor_validation, which additionally "
            "runs per-asset processors."
        ),
    }
