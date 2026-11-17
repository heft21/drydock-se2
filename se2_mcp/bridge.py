"""Client for the in-editor HTTP bridge (SE2McpBridge plugin).

The plugin runs inside VRage.Editor.exe and exposes the live editor over
127.0.0.1. This module is the thin client side; it deliberately keeps no state
beyond the last seen event id, so the editor can be restarted at any time
without the MCP server needing to care.
"""

from __future__ import annotations

import json
import os
import shutil
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from . import toolkit

DEFAULT_PORT = 8765

def _plugin_dir() -> Path:
    """Where the built plugin is: this repository's build output."""
    return Path(__file__).resolve().parent.parent / "bridge" / "bin" / "Release" / "net9.0"


PLUGIN_BUILD_DIR = _plugin_dir()

# Folder name created inside a mod project to hold the plugin.
PLUGIN_FOLDER = "EditorExtensions"


def base_url() -> str:
    port = os.environ.get("SE2_MCP_BRIDGE_PORT", str(DEFAULT_PORT))
    return f"http://127.0.0.1:{port}"


def token_path() -> Path:
    """Where the plugin drops this editor run's bearer token."""
    from .config import PATHS
    return PATHS.cache_dir / "bridge-token.txt"


def read_token() -> str | None:
    """The current token, or None if the editor has not written one.

    The plugin regenerates it on every launch, so this is read per request
    rather than cached — a stale token would otherwise survive an editor
    restart and turn every call into a 401.
    """
    try:
        text = token_path().read_text(encoding="utf-8").strip().splitlines()
    except OSError:
        return None
    return text[-1].strip() if text else None


class BridgeDown(RuntimeError):
    """The editor is not running, or the plugin is not loaded."""


def _request(path: str, payload: dict | None = None, timeout: int = 60) -> bytes:
    url = base_url() + path
    headers = {}
    token = read_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if payload is None:
        req = urllib.request.Request(url, headers=headers)
    else:
        headers["Content-Type"] = "application/json"
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read()
        finally:
            exc.close()                   # an HTTPError holds the open response
        if exc.code == 401:
            raise BridgeDown(
                f"The bridge rejected the token. It is regenerated every time "
                f"the editor starts, and read from {token_path()} — so this "
                f"usually means the editor is not the one that wrote that file. "
                f"Restart the editor, or check that both processes agree on "
                f"SE2_MCP_CACHE."
            ) from exc
        # The bridge answers with JSON even for other error statuses; pass it
        # through so the caller sees the real message instead of "HTTP 500".
        return body
    except (urllib.error.URLError, OSError) as exc:
        raise BridgeDown(
            f"No bridge at {base_url()}: {toolkit.describe_os_error(exc)}. "
            f"Start VRage.Editor.exe on a project that has the SE2McpBridge "
            f"plugin installed — see install_bridge."
        ) from exc


def get_json(path: str, timeout: int = 60) -> Any:
    return json.loads(_request(path, timeout=timeout))


def post_json(path: str, payload: dict, timeout: int = 60) -> Any:
    return json.loads(_request(path, payload, timeout=timeout))


def get_bytes(path: str, timeout: int = 60) -> bytes:
    return _request(path, timeout=timeout)


def is_up() -> bool:
    try:
        return bool(get_json("/ping", timeout=5).get("ok"))
    except (BridgeDown, json.JSONDecodeError, AttributeError):
        return False


# ---------------------------------------------------------------------------
# Installation
# ---------------------------------------------------------------------------

def plugin_built() -> bool:
    return (PLUGIN_BUILD_DIR / "SE2McpBridge.dll").is_file()


def _project_file(project: str | Path) -> tuple[Path, Path]:
    root = Path(project)
    if root.is_file() and root.suffix == ".vrgproj":
        return root, root.parent
    candidates = sorted(root.glob("*.vrgproj"))
    if not candidates:
        raise FileNotFoundError(f"No .vrgproj found in {root}")
    return candidates[0], root


def install(project: str | Path, *, copy_into_project: bool = False) -> dict[str, Any]:
    """Register the plugin with a mod project so the editor loads it.

    The editor loads extension assemblies listed in the project's
    ``EditorExtensionAssemblies``, resolved against
    ``EditorExtensionAssembliesSearchPaths``. Adding both is what makes the
    editor pick the bridge up on the next launch.

    By default the search path points at this repository's build output, so
    nothing is copied into the mod. That matters because the mod folder is what
    gets published: the bridge runs arbitrary C# over an HTTP listener, and it
    has no business inside a Steam Workshop upload. Pass
    ``copy_into_project=True`` only when the editor must run somewhere this
    repository is not reachable — and call ``uninstall`` before publishing.
    """
    if not plugin_built():
        raise FileNotFoundError(
            f"Plugin not built. Run: dotnet build -c Release "
            f"in {PLUGIN_BUILD_DIR.parent.parent.parent}"
        )

    proj_file, root = _project_file(project)

    copied: list[str] = []
    if copy_into_project:
        target = root / PLUGIN_FOLDER
        target.mkdir(parents=True, exist_ok=True)
        for item in PLUGIN_BUILD_DIR.iterdir():
            if item.is_file() and item.suffix in (".dll", ".json"):
                shutil.copy2(item, target / item.name)
                copied.append(item.name)
        search_path = f".\\{PLUGIN_FOLDER}"
    else:
        target = PLUGIN_BUILD_DIR
        search_path = str(PLUGIN_BUILD_DIR)

    doc = json.loads(proj_file.read_text(encoding="utf-8-sig"))
    value = doc.setdefault("$Value", {})

    assemblies = value.setdefault("EditorExtensionAssemblies", [])
    if "SE2McpBridge.dll" not in assemblies:
        assemblies.append("SE2McpBridge.dll")

    paths = value.setdefault("EditorExtensionAssembliesSearchPaths", [])
    if search_path not in paths:
        paths.append(search_path)

    proj_file.write_bytes(
        json.dumps(doc, indent=2, ensure_ascii=False).replace("\n", "\r\n").encode("utf-8")
    )

    return {
        "project_file": str(proj_file),
        "plugin_dir": str(target),
        "copied_into_project": copy_into_project,
        "files_copied": len(copied),
        "editor_extension_assemblies": assemblies,
        "search_paths": paths,
        "next_step": (
            "Launch VRage.Editor.exe and open this project. The bridge starts "
            "with the plugin; check it with editor_status. Run uninstall_bridge "
            "before publishing."
        ),
    }


def uninstall(project: str | Path) -> dict[str, Any]:
    """Remove every trace of the bridge from a project, ready to publish."""
    proj_file, root = _project_file(project)
    doc = json.loads(proj_file.read_text(encoding="utf-8-sig"))
    value = doc.setdefault("$Value", {})

    assemblies = [a for a in value.get("EditorExtensionAssemblies") or []
                  if a != "SE2McpBridge.dll"]
    paths = [p for p in value.get("EditorExtensionAssembliesSearchPaths") or []
             if PLUGIN_FOLDER not in p and "SE2McpBridge" not in p
             and Path(p) != PLUGIN_BUILD_DIR]
    value["EditorExtensionAssemblies"] = assemblies
    value["EditorExtensionAssembliesSearchPaths"] = paths

    proj_file.write_bytes(
        json.dumps(doc, indent=2, ensure_ascii=False).replace("\n", "\r\n").encode("utf-8")
    )

    removed_dir = None
    plugin_dir = root / PLUGIN_FOLDER
    if plugin_dir.is_dir() and (plugin_dir / "SE2McpBridge.dll").is_file():
        shutil.rmtree(plugin_dir, ignore_errors=True)
        removed_dir = str(plugin_dir)

    return {
        "project_file": str(proj_file),
        "removed_plugin_dir": removed_dir,
        "editor_extension_assemblies": assemblies,
        "search_paths": paths,
        "note": "Restart the editor for the change to take effect.",
    }
