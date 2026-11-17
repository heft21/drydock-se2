"""Prepare a planet mod for Mod HUB publishing. RUN WITH MOD HUB AND THE EDITOR CLOSED.

Why it has to be run with them closed: Mod HUB and VRage.Editor hold the project
in memory and write their own copy of the `.vrgproj` back over yours. Measured on
2026-08-14 — the file was edited at 22:17 and overwritten at 22:19, silently
reverting `EnableIgnoreProcessingErrorFlags` to false and putting the editor
bridge back. The `.meta` edits survived; the project-level ones did not.

What it does:

1. Removes the editor bridge. It writes an absolute path into the `.vrgproj`;
   a subscriber has neither the DLL nor the path, and a dead bridge path stops
   the editor opening at all.
2. Turns on `EnableIgnoreProcessingErrorFlags` and marks the `.planetcubemap`
   assets to ignore two specific errors.

   This is not papering over a mod bug. `P_PLANETCUBEMAP`, the processor for
   `.planetcubemap`, lives in `VRage.ContentPipeline.PlanetTextures.dll`, and
   **`VRAGE3.ModHUB.dll` does not reference that assembly** — only Builder,
   Editor and Voxels do. Publish validation runs inside Mod HUB, so the lookup
   misses, falls back to `DefaultAssetProcessor`, and reports both
   `ProcessorNotActual` (the stored `{1, "P_PLANETCUBEMAP"}` cannot match a
   default) and `FilesDependenciesHashMismatching` (no processor, no resolved
   dependencies). Every `.cubemap` asset validates fine, because `P_CUBEMAP`
   lives in the assembly Mod HUB *does* load. It is a Mod HUB bug and no mod can
   fix it from the content side.

   Only the `.planetcubemap` assets are marked, so every other asset in the
   project is still fully validated.
3. Fixes folder/`.meta` name-case mismatches, which the pipeline matches
   ordinally even though Windows does not.

Usage:  python tools/prepare_publish.py "<mod folder>"
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

IGNORE = "FilesDependenciesHashMismatching, ProcessorNotActual"
BLOCKERS = ("VRAGE3.ModHUB.exe", "VRage.Editor.exe")


def running() -> list[str]:
    try:
        out = subprocess.run(["tasklist"], capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return []
    return [b for b in BLOCKERS if b.lower() in out.lower()]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def save(path: Path, doc) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(doc, f, indent=2)
        f.write("\n")


def main(root: Path) -> int:
    busy = running()
    if busy:
        print(f"REFUSING: {', '.join(busy)} still running.")
        print("Close Mod HUB and the editor completely, then run this again —")
        print("they overwrite the .vrgproj with their cached copy.")
        return 1

    proj_files = list(root.glob("*.vrgproj"))
    if not proj_files:
        print(f"No .vrgproj in {root}")
        return 1
    proj = proj_files[0]

    doc = load(proj)
    v = doc["$Value"]
    print(f"{proj.name}")
    print(f"   bridge  {v.get('EditorExtensionAssemblies')} -> []")
    v["EditorExtensionAssemblies"] = []
    v["EditorExtensionAssembliesSearchPaths"] = []
    print(f"   ignore-flags  {v.get('EnableIgnoreProcessingErrorFlags')} -> True")
    v["EnableIgnoreProcessingErrorFlags"] = True
    save(proj, doc)

    n = 0
    for meta in sorted((root / "Assets").rglob("*.planetcubemap.meta")):
        d = load(meta)
        for item in d["$Value"]["InternalItems"]:
            if "AssetProcessing" in item.get("$Type", ""):
                item["IgnoredErrors"] = IGNORE
                n += 1
        save(meta, d)
        print(f"   {meta.name[:-5]:34s} IgnoredErrors set")

    fixed = 0
    for dirpath, dirnames, _ in os.walk(root / "Assets"):
        for d in dirnames:
            want = d + ".meta"
            actual = [e for e in os.listdir(dirpath) if e.lower() == want.lower()]
            if actual and actual[0] != want:
                src = Path(dirpath) / actual[0]
                tmp = Path(dirpath) / (want + ".tmpcase")
                src.rename(tmp)
                tmp.rename(Path(dirpath) / want)
                print(f"   case fix: {actual[0]} -> {want}")
                fixed += 1

    print(f"\n{n} planetcubemap metas marked, {fixed} folder-meta case fixes.")
    print("thumb.jpg:", "present" if (root / "thumb.jpg").exists() else "MISSING")
    print("\nNow open Mod HUB and press Publish. Do not open the editor first —")
    print("it puts the bridge back and clears the flag.")
    return 0


if __name__ == "__main__":
    # No default folder: this rewrites a mod's project and .meta files, so it
    # only ever runs on the folder it is given.
    if len(sys.argv) != 2:
        print("usage: python tools/prepare_publish.py <mod project folder>")
        raise SystemExit(2)
    raise SystemExit(main(Path(sys.argv[1])))
