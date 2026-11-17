"""Which mod project this session is working on, and the bridge's lifecycle.

Every editor tool needs a project path, and a model that has to rediscover it on
every call gets it wrong or asks the user the same question repeatedly. So the
choice is made once, written next to the index, and read back by name.

The bridge is tied to the same switch on purpose. It writes an entry into the
project's `.vrgproj` and must never ship inside a published mod, so "start work"
installs it and "getting ready to publish" removes it. Leaving that to the model
to remember is how a bridge ends up on the Workshop.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from . import config

STATE_NAME = "session.json"


def _state_path() -> Path:
    return config.load_paths().cache_dir / STATE_NAME


def _read() -> dict[str, Any]:
    try:
        return json.loads(_state_path().read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _write(data: dict[str, Any]) -> None:
    p = _state_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")


def candidates() -> list[dict[str, Any]]:
    """Every mod project we can see, newest first, with its .vrgproj path."""
    from . import modhub

    seen: dict[str, dict[str, Any]] = {}
    try:
        for entry in modhub.projects():
            # modhub.projects() lists every folder in the mods dir; only the
            # ones holding a .vrgproj are projects. Named after the project
            # file, as the scan below names them, so a name means the same
            # thing whichever source found it.
            proj = entry.get("project_file")
            if proj:
                seen[str(Path(proj).parent.resolve())] = {
                    "name": Path(proj).stem,
                    "path": str(Path(proj).parent),
                    "source": "modhub",
                }
    except Exception:
        pass

    for root in config.default_mod_roots() + config.extra_roots():
        try:
            # extra_roots() already expands a folder of projects into the
            # projects themselves, so a root may be a project or hold projects.
            for proj in (*Path(root).glob("*.vrgproj"), *Path(root).glob("*/*.vrgproj")):
                key = str(proj.parent.resolve())
                seen.setdefault(key, {"name": proj.stem, "path": str(proj.parent),
                                      "source": "scan"})
        except OSError:
            continue

    out = list(seen.values())
    for entry in out:
        try:
            entry["modified"] = os.path.getmtime(entry["path"])
        except OSError:
            entry["modified"] = 0.0
    out.sort(key=lambda e: e["modified"], reverse=True)
    return out


def resolve(name_or_path: str) -> str | None:
    """Accept a full path, a folder name, or a unique fragment of one."""
    if not name_or_path:
        return None
    p = Path(name_or_path)
    if p.exists():
        return str(p if p.is_dir() else p.parent)
    needle = name_or_path.strip().lower()
    hits = [c for c in candidates()
            if needle == c["name"].lower() or needle in c["path"].lower()]
    if len(hits) == 1:
        return hits[0]["path"]
    exact = [c for c in hits if c["name"].lower() == needle]
    return exact[0]["path"] if len(exact) == 1 else None


def get_active() -> str | None:
    path = _read().get("project")
    return path if path and Path(path).exists() else None


def set_active(project: str) -> None:
    data = _read()
    data["project"] = project
    _write(data)


def clear_active() -> None:
    data = _read()
    data.pop("project", None)
    _write(data)


def require(project: str | None = None) -> tuple[str | None, dict[str, Any] | None]:
    """The project to act on, or a result explaining how to choose one.

    Callers do `path, problem = session.require(project)` and return `problem`
    when it is not None, so every editor tool behaves the same way when nobody
    has said what to work on yet.
    """
    if project:
        resolved = resolve(project)
        if resolved:
            return resolved, None
        return None, {
            "status": "unknown_project",
            "asked_for": project,
            "next": "Call work_on with one of these, or pass a full path.",
            "projects": [c["name"] for c in candidates()],
        }

    active = get_active()
    if active:
        return active, None

    found = candidates()
    if len(found) == 1:
        set_active(found[0]["path"])
        return found[0]["path"], None
    return None, {
        "status": "no_active_project",
        "next": "Ask the user which project, then call work_on(project=...).",
        "projects": [{"name": c["name"], "path": c["path"]} for c in found],
    }
