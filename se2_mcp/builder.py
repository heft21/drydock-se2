"""Wrapper around VRage.ContentPipeline.Builder.exe.

This is the SDK's own validator/compiler, so it — not this MCP server — is the
authority on whether a mod is correct. Exposing it closes the write/validate
loop: an agent can author a definition and immediately find out if the pipeline
accepts it.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Any

from .config import PATHS

# Lines the builder prints for problems. The pipeline tags failures with
# "fail:" and warnings with "warn:", but processors also emit free-form text,
# so matching stays loose.
_ERROR_RE = re.compile(
    r"(\bfail(ed|ure|s)?\b|\berror\b|\bexception\b|\binvalid\b|does not exist)", re.I
)
_WARN_RE = re.compile(r"\bwarn(ing)?\b", re.I)

# Digits, GUIDs and paths are the only thing that differs between the hundreds
# of near-identical lines a broken project emits; blanking them lets repeats
# collapse into one entry with a count.
_NOISE = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F-]{27}|\d+|['\"][^'\"]*['\"]")


def _summarize(lines: list[str], limit: int) -> list[str]:
    """Collapse repeated diagnostics so one broken folder cannot flood the reply."""
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


def _resolve_project(project: str) -> Path:
    p = Path(project)
    if p.is_dir():
        found = sorted(p.glob("*.vrgproj"))
        if not found:
            raise FileNotFoundError(f"No .vrgproj file inside {p}")
        return found[0]
    if not p.is_file():
        raise FileNotFoundError(f"Project file not found: {p}")
    return p


def run(
    project: str,
    *,
    dry_run: bool = False,
    generate_caches: bool = False,
    metadata: bool = False,
    prepare_for_publish: str | None = None,
    resave: str | None = None,
    verbose: bool = False,
    timeout: int = 900,
) -> dict[str, Any]:
    """Invoke the content pipeline on a project and summarise the result."""
    exe = PATHS.builder_exe
    if not exe.is_file():
        return {"ok": False, "error": f"Builder not found: {exe}"}

    proj = _resolve_project(project)
    args: list[str] = [str(exe), "-p", str(proj)]

    if dry_run:
        args.append("-d")
    if generate_caches:
        args.append("--generateCaches")
    if metadata:
        args.append("--metadata")
    if prepare_for_publish:
        args += ["--prepareForPublish", prepare_for_publish]
    if resave:
        args += ["-r", resave]
    if verbose:
        args.append("-v")

    # A mod depends on Engine/Vanilla; without these the builder cannot resolve
    # its ProjectDependencies and fails with unrelated-looking errors.
    args += ["--globalProjectDirs", str(PATHS.game_data)]
    args += ["--globalAssemblyDirs", str(PATHS.editor)]

    try:
        proc = subprocess.run(
            args,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            cwd=str(PATHS.editor),
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"Builder timed out after {timeout}s", "command": args}

    lines = [ln.rstrip() for ln in (proc.stdout + "\n" + proc.stderr).splitlines() if ln.strip()]
    errors = [ln for ln in lines if _ERROR_RE.search(ln)]
    warnings = [ln for ln in lines if _WARN_RE.search(ln) and ln not in errors]

    result: dict[str, Any] = {
        "ok": proc.returncode == 0,
        "exit_code": proc.returncode,
        "project": str(proj),
        "errors": _summarize(errors, 25),
        "warnings": _summarize(warnings, 15),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "tail": [ln[:300] for ln in lines[-12:]],
        "command": " ".join(args),
    }

    # The SDK ships ~384 ".meta" sidecars whose source file was stripped, so
    # depending on the Vanilla project makes the pipeline fail before it ever
    # looks at the mod. Naming that explicitly saves a long debugging detour.
    if not result["ok"] and any("Loose metafile" in ln for ln in errors):
        result["diagnosis"] = (
            "The failure is in the SDK's Vanilla project, not your mod: it ships "
            "~384 orphaned '.meta' files with no source asset ('Loose metafile'). "
            "This CLI has no stripped mode, so it cannot load Vanilla at all — no "
            "combination of arguments fixes it. The editor and Mod HUB do run in "
            "stripped mode and open the same project fine.\n\n"
            "Since every real mod depends on Vanilla, build through the running "
            "editor instead: editor_eval with IProjectsService."
            "GenerateCacheAndDefinitionSet(...). Use this CLI only for projects "
            "that depend on Engine alone."
        )
    if not result["ok"] and any("does not exist" in ln for ln in errors):
        result.setdefault(
            "diagnosis",
            "Outputs are missing because the Content folder has not been "
            "generated yet. Run build_project with mode='caches' first, then "
            "validate again.",
        )
    return result


def version() -> str:
    exe = PATHS.builder_exe
    if not exe.is_file():
        return "builder not found"
    try:
        proc = subprocess.run(
            [str(exe), "--version"], capture_output=True, text=True,
            errors="replace", timeout=60, cwd=str(PATHS.editor),
        )
        return (proc.stdout or proc.stderr).strip().splitlines()[0] if (proc.stdout or proc.stderr) else "?"
    except (subprocess.SubprocessError, OSError, IndexError) as exc:
        return f"unavailable ({exc})"
