"""Reading the Editor's and Mod HUB's own log files.

Both apps write timestamped logs under %APPDATA%\\<AppName>\\Temp\\Logs. This is
the only way to see what Mod HUB did — publishing runs inside the HUB, and a
failure there often leaves no trace in the editor. Reading the log needs no
plugin and works after the fact, including for a run that already crashed.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

APPS = {
    "editor": "VRAGE3.ModEditor",
    "modhub": "VRAGE3.ModHUB",
    # The game writes here too, and it is the only place that says what a mod
    # actually did once loaded: which local mods were discovered, which
    # subsystems initialised, and — in the *_Stats.log beside it — whether a
    # thing was really drawn. Neither the editor nor the HUB can answer that.
    "game": "SpaceEngineers2",
}

# The logger prefixes problems with "fail:" / "Warning:"; processors and Steam
# calls add free-form text, so matching stays broad.
_ERROR_RE = re.compile(
    r"(\bfail(ed|ure|s)?\b|\berror\b|\bexception\b|\binvalid\b|\bdenied\b|"
    r"\brejected\b|does not exist|Loose metafile)", re.I
)
_WARN_RE = re.compile(r"\bwarn(ing)?\b", re.I)

# Volatile parts of otherwise identical lines, blanked so repeats collapse.
_NOISE = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F-]{27}|\d+")


def log_dir(app: str) -> Path:
    name = APPS.get(app)
    if not name:
        raise ValueError(f"app must be one of {sorted(APPS)}")
    roaming = Path(os.environ.get("APPDATA", Path.home() / "AppData/Roaming"))
    return roaming / name / "Temp" / "Logs"


def list_runs(app: str, limit: int = 10) -> list[dict[str, Any]]:
    """Recent log files, newest first. One run can write several files."""
    d = log_dir(app)
    if not d.is_dir():
        return []
    files = sorted(d.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    return [
        {
            "file": p.name,
            "path": str(p),
            "size": p.stat().st_size,
            "modified": __import__("time").strftime(
                "%Y-%m-%d %H:%M", __import__("time").localtime(p.stat().st_mtime)
            ),
        }
        for p in files[:limit]
    ]


def _summarize(lines: list[str], limit: int) -> list[str]:
    groups: dict[str, tuple[str, int]] = {}
    for ln in lines:
        key = _NOISE.sub("#", ln)[:160]
        first, n = groups.get(key, (ln, 0))
        groups[key] = (first, n + 1)
    out = []
    for first, n in list(groups.values())[:limit]:
        text = first if len(first) <= 400 else first[:400] + " …"
        out.append(f"{text}   (x{n})" if n > 1 else text)
    return out


def read(
    app: str,
    file_name: str = "",
    contains: str = "",
    errors_only: bool = True,
    tail: int = 40,
) -> dict[str, Any]:
    """Read a log run and pull out what went wrong."""
    d = log_dir(app)
    if not d.is_dir():
        return {"error": f"No log directory for {app}: {d}"}

    if file_name:
        target = d / file_name
        if not target.is_file():
            return {"error": f"No such log file: {target}"}
        candidates = [target]
    else:
        # The newest run may span a main log plus per-subsystem ones; the main
        # log (shortest name) carries the application-level story.
        files = sorted(d.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not files:
            return {"error": f"No log files in {d}"}
        newest_mtime = files[0].stat().st_mtime
        candidates = [p for p in files if newest_mtime - p.stat().st_mtime < 120]
        candidates.sort(key=lambda p: len(p.name))

    all_lines: list[str] = []
    used: list[str] = []
    for p in candidates[:4]:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            return {"error": f"Could not read {p}: {exc}"}
        used.append(p.name)
        all_lines.extend(ln.rstrip() for ln in text.splitlines() if ln.strip())

    if contains:
        needle = contains.lower()
        hits = [ln for ln in all_lines if needle in ln.lower()]
        return {
            "app": app,
            "files": used,
            "filter": contains,
            "matches": len(hits),
            "lines": _summarize(hits, 40),
        }

    errors = [ln for ln in all_lines if _ERROR_RE.search(ln)]
    warnings = [ln for ln in all_lines if _WARN_RE.search(ln) and ln not in errors]

    result: dict[str, Any] = {
        "app": app,
        "files": used,
        "total_lines": len(all_lines),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "errors": _summarize(errors, 25),
    }
    if not errors_only:
        result["warnings"] = _summarize(warnings, 15)
        result["tail"] = [ln[:300] for ln in all_lines[-max(1, tail):]]

    if any("Loose metafile" in ln for ln in errors):
        result["diagnosis"] = (
            "'Loose metafile' means a '.meta' sidecar has no source file. The "
            "SDK's Vanilla project ships ~384 of these, so this appears whenever "
            "a tool loads Vanilla without stripped mode. The editor and Mod HUB "
            "handle it; the standalone content-pipeline CLI does not."
        )
    return result
