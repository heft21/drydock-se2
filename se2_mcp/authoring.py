"""Writing SE2 content: definitions and their .meta sidecars.

Every asset in an SE2 project needs a ``.meta`` sidecar carrying its AssetID and
a content hash. Measured against the shipped SDK data, that hash is
``base64(MD5(file bytes))`` — verified byte-for-byte on vanilla files. Because
the format is reproducible, definitions can be authored without opening the
editor; the content pipeline then validates the result.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import shutil
import time
import uuid
from pathlib import Path
from typing import Any

from .config import DEF_SUFFIXES, PATHS

# Last-resort bundle versions, used only when nothing can be read from disk.
FALLBACK_BUNDLES = {
    "Game2": "2.0.1.5507",
    "System.Runtime": "1.0.0.0",
    "VRage": "2.0.1.5507",
}

# Cache for the version scraped from the installed pipeline; the subprocess
# call behind it is slow and the answer cannot change while we run.
_SDK_VERSION: str | None = None


def new_guid() -> str:
    return str(uuid.uuid4())


def sdk_version() -> str | None:
    """The installed pipeline's version, e.g. '2.3.0.2798'."""
    global _SDK_VERSION
    if _SDK_VERSION is None:
        from . import builder
        m = re.search(r"v\.?\s*(\d+\.\d+\.\d+\.\d+)", builder.version())
        _SDK_VERSION = m.group(1) if m else ""
    return _SDK_VERSION or None


def _bundle_names(node: Any) -> set[str]:
    """The bundles a document needs, from the '<Bundle>:<Type>' names it uses."""
    names: set[str] = set()
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$Type" and isinstance(v, str) and ":" in v:
                names.add(v.split(":", 1)[0])
            else:
                names |= _bundle_names(v)
    elif isinstance(node, list):
        for v in node:
            names |= _bundle_names(v)
    return names


def detect_bundles(type_name: str, value: Any = None) -> dict[str, str]:
    """The $Bundles stamp for a definition the server is writing now.

    Measured over 400 vanilla files: the key set is always
    ``{System.Runtime, VRage}`` or ``{Game2, System.Runtime, VRage}``,
    ``System.Runtime`` is always ``1.0.0.0``, and every other bundle carries one
    shared version — the SDK build that wrote the file. The editor stamps its
    own current version, so this does the same rather than copying an older
    neighbour's stamp, which would understate the schema the file was authored
    against. Nested ``$Type`` names decide whether Game2 belongs in the set.
    """
    version = sdk_version()
    if not version:
        return dict(FALLBACK_BUNDLES)

    names = {type_name.split(":", 1)[0]} if ":" in type_name else set()
    names |= _bundle_names(value)
    names.discard("System.Runtime")

    out = {"System.Runtime": "1.0.0.0", "VRage": version}
    out.update({n: version for n in names})
    return dict(sorted(out.items()))


def file_hash(data: bytes) -> str:
    """The content hash the pipeline stores in .meta files."""
    return base64.b64encode(hashlib.md5(data).digest()).decode("ascii")


def meta_bundles() -> dict[str, str]:
    """The $Bundles stamp for a .meta sidecar — VRage only, current version."""
    return {"System.Runtime": "1.0.0.0",
            "VRage": sdk_version() or FALLBACK_BUNDLES["VRage"]}


def make_meta(asset_id: str, file_name: str, data: bytes, processor: str = "P_DEF") -> str:
    """Build a .meta sidecar for a definition file."""
    digest = file_hash(data)
    doc = {
        "$Bundles": meta_bundles(),
        "$Type": "VRage:Keen.VRage.ContentPipeline.Metafiles.MetaData",
        "$Value": {
            "AssetID": asset_id,
            "InternalItems": [
                {
                    "$Type": "VRage:Keen.VRage.ContentPipeline.Project.Structure."
                             "FileInfoMetaDataItem",
                    "FileHash": digest,
                },
                {
                    "$Type": "VRage:Keen.VRage.ContentPipeline.Project.Features."
                             "AssetProcessing.AssetProcessingMetaDataItem",
                    "ProcessorInfo": {"Version": 2, "Identifier": processor},
                    "ContentFiles": {
                        "MainOutput": {"FileHash": digest, "FileName": file_name},
                        "AdditionalOutputs": [],
                    },
                    "Problems": [],
                    "DependenciesHashes": [],
                    "AssetHash": digest,
                    "OverrideDetachedState": False,
                    "IgnoredErrors": "None",
                },
                {
                    "$Type": "VRage:Keen.VRage.ContentPipeline.Definitions."
                             "DefinitionFlagsMetadata",
                    "Flags": "None",
                },
            ],
        },
    }
    return json.dumps(doc, indent=2)


def serialize(doc: dict[str, Any]) -> bytes:
    """Serialize a definition the way the SDK does: 2-space indent, CRLF."""
    text = json.dumps(doc, indent=2, ensure_ascii=False)
    return text.replace("\n", "\r\n").encode("utf-8")


def backup_dir() -> Path:
    """Where replaced files are kept. Beside this repository, never in the mod."""
    return Path(__file__).resolve().parent.parent / ".backups"


def _back_up(target: Path) -> str | None:
    """Copy a file that is about to be replaced, timestamped so nothing is lost.

    Overwriting is a normal part of authoring — a definition gets rewritten
    several times before it is right — but an agent doing it has no undo, so the
    previous bytes are kept where a human can find them.
    """
    if not target.is_file():
        return None
    stamp = time.strftime("%Y%m%d-%H%M%S")
    folder = backup_dir() / f"{target.stem}-{stamp}"
    folder.mkdir(parents=True, exist_ok=True)
    saved = folder / target.name
    shutil.copy2(target, saved)
    meta = target.with_name(target.name + ".meta")
    if meta.is_file():
        shutil.copy2(meta, folder / meta.name)
    return str(saved)


def _existing_guid(target: Path) -> str | None:
    """The identity a file already has, so rewriting it does not change it.

    A definition's GUID is what every reference to it points at. Regenerating
    one on an overwrite would silently detach the file from everything that
    used it, and nothing would report the break — so an existing identity wins
    over a fresh one whenever the caller did not ask for a specific GUID.
    """
    try:
        value = json.loads(target.read_text(encoding="utf-8-sig")).get("$Value", {})
    except (json.JSONDecodeError, OSError, AttributeError):
        value = {}
    if isinstance(value, dict):
        man = value.get("Manipulator")
        if isinstance(man, dict) and isinstance(man.get("Guid"), str):
            return man["Guid"]
        if isinstance(value.get("Guid"), str):
            return value["Guid"]
    # An Override partialdef carries no Guid at all; the sidecar holds it.
    meta = target.with_name(target.name + ".meta")
    try:
        stored = json.loads(meta.read_text(encoding="utf-8-sig"))
        asset_id = stored.get("$Value", {}).get("AssetID")
        return asset_id if isinstance(asset_id, str) else None
    except (json.JSONDecodeError, OSError, AttributeError):
        return None


def write_definition(
    path: str | Path,
    type_name: str,
    value: dict[str, Any],
    *,
    bundles: dict[str, str] | None = None,
    guid: str | None = None,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Write a ``.def``/``.partialdef`` plus a matching ``.meta`` sidecar."""
    target = Path(path)
    if target.suffix not in DEF_SUFFIXES:
        raise ValueError(f"Path must end in {' or '.join(DEF_SUFFIXES)}: {target}")
    if target.exists() and not overwrite:
        raise FileExistsError(f"{target} exists; pass overwrite=true to replace it")
    kept = _existing_guid(target) if target.is_file() else None
    backup = _back_up(target) if overwrite else None

    value = dict(value)
    asset_id = (guid or value.get("Guid") or kept or new_guid()).lower()

    # A partialdef identifies itself through Manipulator.Guid; a plain def
    # through $Value.Guid. Matching the right one keeps the .meta AssetID
    # consistent with how the pipeline reads the file.
    if target.suffix == ".partialdef" and isinstance(value.get("Manipulator"), dict):
        man = dict(value["Manipulator"])
        asset_id = (guid or man.get("Guid") or kept or asset_id).lower()
        # Vanilla writes Guid first inside Manipulator; keep diffs readable.
        value["Manipulator"] = {"Guid": asset_id,
                                **{k: v for k, v in man.items() if k != "Guid"}}
    else:
        # Every vanilla definition leads with Guid, so authored files should too.
        value = {"Guid": asset_id,
                 **{k: v for k, v in value.items() if k != "Guid"}}

    doc = {
        "$Bundles": bundles or detect_bundles(type_name, value),
        "$Type": type_name,
        "$Value": value,
    }
    data = serialize(doc)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    meta_path = target.with_name(target.name + ".meta")
    meta_path.write_bytes(make_meta(asset_id, target.name, data).replace("\n", "\r\n").encode("utf-8"))

    out = {
        "written": str(target),
        "meta": str(meta_path),
        "guid": asset_id,
        "bytes": len(data),
        "file_hash": file_hash(data),
        "next_step": (
            "Run audit_project on the mod to confirm every GUID it references "
            "resolves, then reload the project in the editor — asset processors "
            "run at project load, not at build."
        ),
    }
    if backup:
        out["previous_version"] = backup
    return out


# Project GUIDs of the SDK's own projects, read from their .vrgproj files.
ENGINE_PROJECT_GUID = "079da0f2-4755-491e-8688-b68b91b2fad3"
VANILLA_PROJECT_GUID = "56dacb76-e25e-468a-9432-21964a9a0569"


def scaffold_mod(
    directory: str | Path,
    name: str,
    *,
    depend_on_vanilla: bool = True,
    summary: str = "",
) -> dict[str, Any]:
    """Create a mod project: .vrgproj, an Assets definition set, publish metadata.

    Vanilla is a dependency by default because every real published mod has it —
    without it nothing from the base game can be referenced. The trade-off is
    that the standalone content-pipeline CLI cannot load such a project: it has
    no stripped mode, so the ~384 orphaned '.meta' files the SDK ships make
    Vanilla unreadable to it. The editor and Mod HUB do run in stripped mode and
    handle it, so build these projects through the editor bridge.

    Pass depend_on_vanilla=False for a project that must build from the CLI and
    references nothing from the base game.
    """
    root = Path(directory)
    if (root / f"{name}.vrgproj").exists():
        raise FileExistsError(f"{name}.vrgproj already exists in {root}")
    (root / "Assets").mkdir(parents=True, exist_ok=True)

    deps = [{"Guid": ENGINE_PROJECT_GUID, "ModId": None, "ServiceId": ""}]
    if depend_on_vanilla:
        deps.append({"Guid": VANILLA_PROJECT_GUID, "ModId": None, "ServiceId": ""})

    project_id = new_guid()
    proj = {
        "$Bundles": meta_bundles(),
        "$Type": "VRage:Keen.VRage.Core.Project.VRageProjectData",
        "$Value": {
            "Name": name,
            "Version": None,
            "Type": "Mod",
            "ProjectID": {"Guid": project_id, "ModId": None, "ServiceId": ""},
            "ModSetup": None,
            "ProjectDependencies": deps,
            "ProjectDirectories": [],
            "UsedBuildStream": "",
            "DefinitionSetNames": ["World", "Core"],
            "GameExecutable": "SpaceEngineers2.exe",
            "GameExecutableSearchPaths": [],
            "ReferencedAssemblies": [
                "Game2.Client.dll", "Game2.Game.dll", "Game2.Simulation.dll",
            ],
            "ReferencedAssembliesSearchPaths": [],
            "EditorExtensionAssemblies": [],
            "EditorExtensionAssembliesSearchPaths": [],
            "SkipContentMounting": False,
            "EnableIgnoreProcessingErrorFlags": False,
        },
    }
    proj_path = root / f"{name}.vrgproj"
    proj_path.write_bytes(serialize(proj))

    # Marks Assets/ as a definition set, the way Vanilla does.
    assets_meta = {
        "$Bundles": meta_bundles(),
        "$Type": "VRage:Keen.VRage.ContentPipeline.Metafiles.MetaData",
        "$Value": {
            "AssetID": new_guid(),
            "InternalItems": [
                {"$Type": "VRage:Keen.VRage.ContentPipeline.Definitions."
                          "DefinitionSetItem", "DefinitionSetName": "World"},
                {"$Type": "VRage:Keen.VRage.ContentPipeline.Publishing."
                          "AssetsStrippingMetaDataItem", "Strip": False},
            ],
        },
    }
    (root / "Assets.meta").write_bytes(serialize(assets_meta))

    # Mod HUB reads this to fill in the Workshop page. Writing it now costs
    # nothing and means the project is publishable without a hand-made file;
    # the zero GUIDs are what an unpublished project carries, and the HUB
    # replaces them on first publish.
    blank_id = "00000000-0000-0000-0000-000000000000"
    metadata = {
        "$Bundles": meta_bundles(),
        "$Type": "VRage:Keen.VRage.ModHUB.Models.ModProject",
        "$Value": {
            "Id": {"Id": blank_id, "ServiceName": ""},
            "ProjectID": {"Guid": blank_id, "ModId": None, "ServiceId": None},
            "Version": "0.0",
            "BaseMetadata": None,
            "Name": name,
            "Summary": summary,
            "Tags": [],
            "ProjectFile": f"{name}.vrgproj",
        },
    }
    metadata_path = root / "ModProject.modhub-metadata"
    if not metadata_path.exists():
        metadata_path.write_bytes(serialize(metadata))

    return {
        "project_file": str(proj_path),
        "assets_dir": str(root / "Assets"),
        "publish_metadata": str(metadata_path),
        "project_guid": project_id,
        "depends_on": ["Engine"] + (["Vanilla"] if depend_on_vanilla else []),
        "next_steps": [
            "Author definitions into Assets/ with write_definition. Every "
            "subfolder you create under Assets/ needs its own .meta, or the "
            "pipeline does not mount what is inside it.",
            "Run audit_project to confirm the project is consistent.",
            ("Build it through the editor: launch_editor then editor_build. The "
             "standalone CLI cannot load a Vanilla-dependent project."
             if depend_on_vanilla else
             "Run build_project(mode='full'), then validate_project."),
            "Before publishing, add a thumb.jpg at the project root and fill in "
            "Summary and Tags in ModProject.modhub-metadata.",
        ],
    }


def refresh_meta(def_path: str | Path) -> dict[str, Any]:
    """Recompute the .meta hash after a definition was edited by hand."""
    target = Path(def_path)
    if not target.is_file():
        raise FileNotFoundError(target)
    data = target.read_bytes()
    meta_path = target.with_name(target.name + ".meta")

    asset_id = None
    if meta_path.is_file():
        try:
            existing = json.loads(meta_path.read_text(encoding="utf-8-sig"))
            asset_id = existing.get("$Value", {}).get("AssetID")
        except (json.JSONDecodeError, OSError):
            asset_id = None
    if not asset_id:
        doc = json.loads(target.read_text(encoding="utf-8-sig"))
        v = doc.get("$Value", {})
        man = v.get("Manipulator")
        asset_id = (man or {}).get("Guid") if isinstance(man, dict) else None
        asset_id = asset_id or v.get("Guid") or new_guid()

    meta_path.write_bytes(
        make_meta(asset_id, target.name, data).replace("\n", "\r\n").encode("utf-8")
    )
    return {"meta": str(meta_path), "guid": asset_id, "file_hash": file_hash(data)}
