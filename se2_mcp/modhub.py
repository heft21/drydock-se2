"""The Mod HUB side: status, the mod list, and launching the applications.

Mod HUB has no plugin system (unlike the editor it does not support
`IProjectPlugin`) and offers no command line for publishing — its CLI carries
only `--useSteamPaths` and `--nosplash`. So control here is limited to three
things, and those three are real: reading its settings and mod list, starting
the processes, and reading its log.

Publishing itself happens in the HUB window, over Steam UGC. But what blocks a
publish is almost always project validation, and that can be inspected through
the editor bridge — see the `editor_validation` tool.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any

from .config import PATHS

SETTINGS = Path(os.environ.get("APPDATA", Path.home() / "AppData/Roaming")) \
    / "VRAGE3.ModHUB" / "Settings" / "ApplicationSettings.json"


def _read_settings() -> dict[str, Any]:
    try:
        doc = json.loads(SETTINGS.read_text(encoding="utf-8-sig"))
        return doc.get("$Value", {})
    except (OSError, json.JSONDecodeError):
        return {}


def mods_dir() -> Path:
    """Mod HUB's mods folder; the Documents default when it has no setting."""
    d = _read_settings().get("ModsDirectory")
    if d:
        return Path(d)
    return Path.home() / "Documents" / "SpaceEngineers2" / "Mods"


def _running(exe_stem: str) -> list[int]:
    """PIDs of the named process, via the Windows tasklist command."""
    try:
        out = subprocess.run(
            ["tasklist", "/FI", f"IMAGENAME eq {exe_stem}.exe", "/FO", "CSV", "/NH"],
            capture_output=True, text=True, errors="replace", timeout=30).stdout
    except (subprocess.SubprocessError, OSError):
        return []
    pids = []
    for line in out.splitlines():
        parts = [p.strip('"') for p in line.split('","')]
        if len(parts) > 1 and parts[0].lower().startswith(exe_stem.lower()):
            try:
                pids.append(int(parts[1]))
            except ValueError:
                pass
    return pids


def status() -> dict[str, Any]:
    st = _read_settings()
    return {
        "settings_file": str(SETTINGS) if SETTINGS.exists() else None,
        "mods_directory": str(mods_dir()),
        "show_detailed_errors": st.get("ShowDetailedErrors"),
        "modhub_running_pids": _running("VRAGE3.ModHUB"),
        "editor_running_pids": _running("VRage.Editor"),
        "game_running_pids": _running("SpaceEngineers2"),
        "note": (
            "ShowDetailedErrors is false, so Mod HUB reports publish failures "
            "as one generic line. Setting it true reveals the real problem list."
        ) if st.get("ShowDetailedErrors") is False else None,
    }


def projects() -> list[dict[str, Any]]:
    """Projects in the mods folder, with the Steam id of published ones."""
    out: list[dict[str, Any]] = []
    root = mods_dir()
    if not root.is_dir():
        return out
    for d in sorted(p for p in root.iterdir() if p.is_dir()):
        proj = next(iter(sorted(d.glob("*.vrgproj"))), None)
        item: dict[str, Any] = {"name": d.name, "dir": str(d)}
        if proj is None:
            item["project_file"] = None
            out.append(item)
            continue
        item["project_file"] = str(proj)
        try:
            v = json.loads(proj.read_text(encoding="utf-8-sig")).get("$Value", {})
        except (OSError, json.JSONDecodeError) as exc:
            item["error"] = str(exc)
            out.append(item)
            continue
        pid = v.get("ProjectID") or {}
        mod_id = pid.get("ModId")
        item.update({
            "project_guid": pid.get("Guid"),
            "published": bool(mod_id),
            "service": pid.get("ServiceId") or None,
            "mod_id": (mod_id or {}).get("Id"),
            "depends_on_vanilla": any(
                (d or {}).get("Guid") == "56dacb76-e25e-468a-9432-21964a9a0569"
                for d in v.get("ProjectDependencies") or []),
            "has_content": (d / "Content").is_dir(),
        })
        out.append(item)
    return out


def _spawn(args: list[str], cwd: str | None = None) -> dict[str, Any]:
    try:
        p = subprocess.Popen(args, cwd=cwd,
                             creationflags=getattr(subprocess, "DETACHED_PROCESS", 0))
        return {"ok": True, "pid": p.pid, "command": " ".join(args)}
    except (OSError, ValueError) as exc:
        return {"ok": False, "error": str(exc), "command": " ".join(args)}


def launch_modhub(no_splash: bool = True) -> dict[str, Any]:
    exe = PATHS.editor / "VRAGE3.ModHUB.exe"
    if not exe.is_file():
        return {"ok": False, "error": f"Not found: {exe}"}
    args = [str(exe)] + (["--nosplash"] if no_splash else [])
    return _spawn(args, cwd=str(PATHS.editor))


def launch_editor(project: str) -> dict[str, Any]:
    """Open the editor on a project, with the same arguments Mod HUB uses.

    The two `globalProjectDirs` and `projectExecutableSearchPaths` were taken
    from Mod HUB's own log; without them the Vanilla dependency cannot be
    resolved and the project fails to load.
    """
    exe = PATHS.editor / "VRage.Editor.exe"
    if not exe.is_file():
        return {"ok": False, "error": f"Not found: {exe}"}

    p = Path(project)
    if p.is_dir():
        found = sorted(p.glob("*.vrgproj"))
        if not found:
            return {"ok": False, "error": f"No .vrgproj file inside {p}"}
        p = found[0]
    if not p.is_file():
        return {"ok": False, "error": f"Project file does not exist: {p}"}

    game = PATHS.sdk.parent / "SpaceEngineers2" / "Game2"
    args = [
        str(exe), "--project", str(p),
        "--globalProjectDirs", str(PATHS.game_data),
        str(PATHS.sdk / "VRage" / "GameData"),
        "--globalAssemblyDirs", str(PATHS.editor),
    ]
    if game.is_dir():
        args += ["--projectExecutableSearchPaths", str(game)]
    res = _spawn(args, cwd=str(PATHS.editor))
    res["project"] = str(p)
    res["next"] = ("Poll editor_status until the bridge answers (~10-40s). The "
                   "bridge only comes up if install_bridge was run on this project.")
    return res
