"""Check every .meta's recorded hashes against the files actually on disk.

The publish error "Asset file dependencies hashes do not match hashes saved in
metadata" comes from `ValidateProcessingFeature`, which fires when an asset's
dependencies hash differently from what its `.meta` records. Rather than guessing
which asset that is from a dialog box, this recomputes the hashes locally.

`FileHash` in a meta is base64 of the MD5 of the file's bytes — verified against
vanilla content, where every hash matches. Anything that does not match here is a
concrete, named suspect.

    python tools/verify_hashes.py "C:/Users/.../Mods/My Mod"
    python tools/verify_hashes.py --vanilla     # sanity-check the format itself
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys

def vanilla_maps() -> str:
    """Verdure's map folder in the installed SDK, found the way the server finds it."""
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from se2_mcp.config import PATHS
    return str(PATHS.game_data / "Vanilla" / "Assets" / "Procedural" / "VS2_0"
               / "Planets" / "Verdure" / "Maps")


def file_hash(path: str) -> str | None:
    try:
        h = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        return base64.b64encode(h.digest()).decode()
    except OSError:
        return None


def check(root: str, limit: int | None = None) -> int:
    metas = []
    for dirpath, _d, names in os.walk(root):
        for n in names:
            if n.endswith(".meta"):
                metas.append(os.path.join(dirpath, n))
    metas.sort()
    if limit:
        metas = metas[:limit]

    print(f"{len(metas)} .meta files under {root}\n")
    checked = mismatched = missing = 0
    problems: list[str] = []

    for meta in metas:
        asset = meta[: -len(".meta")]
        try:
            with open(meta, encoding="utf-8-sig") as f:
                doc = json.load(f)
        except Exception as exc:
            problems.append(f"unreadable meta: {os.path.relpath(meta, root)}  ({exc})")
            continue

        items = (doc.get("$Value") or {}).get("InternalItems") or []
        for it in items:
            t = str(it.get("$Type", "")).split(".")[-1]

            # The asset's own file hash.
            if t == "FileInfoMetaDataItem" and it.get("FileHash"):
                if not os.path.exists(asset):
                    missing += 1
                    problems.append(f"asset missing for meta: {os.path.relpath(meta, root)}")
                    continue
                checked += 1
                actual = file_hash(asset)
                if actual != it["FileHash"]:
                    mismatched += 1
                    problems.append(
                        f"SOURCE HASH MISMATCH  {os.path.relpath(asset, root)}\n"
                        f"    meta says {it['FileHash']}\n"
                        f"    file is   {actual}"
                    )

            # The processed output(s) in Content/.
            if t == "AssetProcessingMetaDataItem":
                cf = it.get("ContentFiles") or {}
                outs = [cf.get("MainOutput")] + list(cf.get("AdditionalOutputs") or [])
                for o in outs:
                    if not o or not o.get("FileName") or not o.get("FileHash"):
                        continue
                    # Content mirrors the Assets tree.
                    rel = os.path.relpath(os.path.dirname(asset), root)
                    parts = rel.replace("\\", "/").split("/")
                    if parts and parts[0] == "Assets":
                        parts[0] = "Content"
                    out_path = os.path.join(root, *parts, o["FileName"])
                    if not os.path.exists(out_path):
                        missing += 1
                        problems.append(
                            f"output missing: {os.path.relpath(out_path, root)} "
                            f"(expected by {os.path.relpath(meta, root)})"
                        )
                        continue
                    checked += 1
                    actual = file_hash(out_path)
                    if actual != o["FileHash"]:
                        mismatched += 1
                        problems.append(
                            f"OUTPUT HASH MISMATCH  {os.path.relpath(out_path, root)}\n"
                            f"    meta says {o['FileHash']}\n"
                            f"    file is   {actual}"
                        )

    print(f"{checked} hashes checked, {mismatched} mismatched, {missing} files missing\n")
    for p in problems[:60]:
        print("  " + p)
    if len(problems) > 60:
        print(f"  … and {len(problems) - 60} more")
    if not problems:
        print("  everything matches")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", help="mod project folder")
    ap.add_argument("--vanilla", action="store_true",
                    help="check shipped content instead, to confirm the hash format")
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    root = vanilla_maps() if args.vanilla else args.root
    if not root:
        ap.print_help()
        return 2
    if not os.path.isdir(root):
        print(f"not a folder: {root}", file=sys.stderr)
        return 2
    return check(root, args.limit)


if __name__ == "__main__":
    raise SystemExit(main())
