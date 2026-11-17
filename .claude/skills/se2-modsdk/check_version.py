"""Does this handbook still describe the installed SDK?

Steam updates the Mod SDK silently, and a type catalogue generated against an
older build will quietly disagree with the files on disk. Run this before
relying on anything under `types/`.

    python check_version.py

Exit codes: 0 match, 2 differ or missing, 1 error.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
sys.path.insert(0, str(REPO))


def main() -> int:
    try:
        from se2_mcp import builder, index
        from se2_mcp.config import PATHS
    except ImportError as exc:
        print(f"Cannot import the MCP server package from {REPO}: {exc}")
        return 1

    problems = PATHS.check()
    if problems:
        print("SDK not usable:")
        for p in problems:
            print(f"  - {p}")
        return 1

    m = re.search(r"v\.?\s*(\d+\.\d+\.\d+\.\d+)", builder.version())
    installed = m.group(1) if m else "unknown"

    stamp = HERE / "sdk_version.txt"
    recorded = stamp.read_text(encoding="utf-8").strip() if stamp.is_file() else None

    print(f"SDK installed          : {installed}")
    print(f"handbook generated for : {recorded or '(never generated)'}")
    print(f"SDK root               : {PATHS.sdk}")

    status = index.index_status()
    if status.get("built"):
        stats = status.get("stats") or {}
        print(f"index                  : {stats.get('definitions', '?')} definitions, "
              f"built {status.get('built_at', '?')}")
        if status.get("stale"):
            print(f"index is stale         : {status['stale']}")
    else:
        print("index                  : not built (run build_index)")

    if recorded is None:
        print("\nMISSING - run: python build_reference.py")
        return 2
    if recorded != installed:
        print("\nDIFFER - the generated types/ catalogue was built against a "
              "different SDK build.\n"
              "The hand-written pages under reference/ are measured facts and "
              "age slowly; they are\nusually still correct. Rebuild the "
              "catalogue with: python build_reference.py")
        return 2

    print("\nMATCH")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
