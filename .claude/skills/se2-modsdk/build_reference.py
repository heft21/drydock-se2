"""Regenerate the generated half of the SE2 Mod SDK handbook.

The hand-written pages under `reference/` are measured knowledge and are never
touched by this script. What it does generate is `types/` — one page per $Type
that really occurs in SE2 content, carrying the SDK's own field documentation,
how many definitions use it, and a real vanilla file to look at.

That split matters: the prose is expensive to produce and stable, while the type
catalogue is cheap to produce and goes stale with every game update. Run this
after `build_index`; it reads the same caches the MCP server does and needs
nothing else.

    python build_reference.py            # regenerate types/ and sdk_version.txt
    python build_reference.py --check    # report drift without writing
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent          # .claude/skills/se2-modsdk -> repo root
sys.path.insert(0, str(REPO))

from se2_mcp import builder, docs, index          # noqa: E402
from se2_mcp.config import PATHS                  # noqa: E402

TYPES_DIR = HERE / "types"
VERSION_FILE = HERE / "sdk_version.txt"

# Windows file names cannot carry these, and a $Type is a dotted C# name.
_UNSAFE = re.compile(r'[<>:"/\\|?*]')


def safe(name: str) -> str:
    return _UNSAFE.sub("_", name)[:120]


def page_names(rows: list[tuple[str, int]]) -> dict[str, str]:
    """A short file name for every type's page: the type's own name.

    The full name (``Keen.Game2.Simulation.WorldObjects....ObjectBuilder``) runs
    to 120 characters, and with a repository cloned a few folders deep that
    passes Windows' 260-character path limit and the checkout fails. The page
    itself starts with the full name, so the file only has to be unique within
    its bundle; two types that share a short name get a few hex digits of their
    full name's hash to tell them apart.
    """
    import hashlib
    short: dict[tuple[str, str], list[str]] = {}
    for type_name, _ in rows:
        bundle, _, full = type_name.partition(":")
        short.setdefault((bundle, full.rsplit(".", 1)[-1]), []).append(type_name)
    names: dict[str, str] = {}
    for (_, name), owners in short.items():
        for type_name in owners:
            tag = ""
            if len(owners) > 1:
                tag = "-" + hashlib.sha1(type_name.encode()).hexdigest()[:6]
            names[type_name] = safe(name)[:80] + tag
    return names


def sdk_version() -> str:
    m = re.search(r"v\.?\s*(\d+\.\d+\.\d+\.\d+)", builder.version())
    return m.group(1) if m else "unknown"


# The catalogue is published with the repository, so it describes only what
# ships in the SDK. The index also holds the mod projects on this machine; their
# types, names and files are the user's own and must never end up in it.
SDK_PROJECTS = ("Vanilla", "Engine")
_IN_SDK = f"project IN ({', '.join('?' * len(SDK_PROJECTS))})"


def type_rows(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    return [(r["type"], r["n"]) for r in conn.execute(
        f"SELECT type, COUNT(*) n FROM assets WHERE type IS NOT NULL AND {_IN_SDK} "
        "GROUP BY type ORDER BY type", SDK_PROJECTS)]


def example_for(conn: sqlite3.Connection, type_name: str) -> dict | None:
    row = conn.execute(
        f"SELECT stem, path FROM assets WHERE type=? AND {_IN_SDK} "
        "ORDER BY LENGTH(path) LIMIT 3",
        (type_name, *SDK_PROJECTS),
    ).fetchall()
    if not row:
        return None
    first = row[0]
    out = {"name": first["stem"], "path": first["path"], "others":
           [r["stem"] for r in row[1:]]}
    full = PATHS.game_data / first["path"]
    if full.is_file() and full.stat().st_size < 20000:
        try:
            value = json.loads(full.read_text(encoding="utf-8-sig")).get("$Value", {})
            text = json.dumps(value, indent=2)
            if len(text) <= 3000:
                out["value"] = text
            else:
                out["fields"] = sorted(value) if isinstance(value, dict) else None
        except (json.JSONDecodeError, OSError):
            pass
    return out


def write_type_page(path: Path, type_name: str, used_by: int,
                    doc: dict, example: dict | None) -> None:
    bundle, _, full = type_name.partition(":")
    lines = [
        f"# {full.rsplit('.', 1)[-1]}",
        "",
        f"`{type_name}`",
        "",
        f"- bundle: **{bundle or '(none)'}**",
        f"- namespace: `{full.rsplit('.', 1)[0] if '.' in full else ''}`",
        f"- definitions using it: **{used_by}**",
        "",
    ]
    if doc.get("summary"):
        lines += ["## What it is", "", doc["summary"], ""]

    fields = doc.get("documented_fields") or {}
    if fields:
        lines += ["## Fields", "",
                  "Straight from the SDK's own XML documentation — this is the "
                  "only authoritative description of what each field means.",
                  "", "| field | meaning |", "|---|---|"]
        for name, text in sorted(fields.items()):
            lines.append(f"| `{name}` | {text.replace('|', '\\|')} |")
        lines.append("")
    else:
        lines += ["## Fields", "",
                  "No XML documentation ships for this type. Read the example "
                  "below and the vanilla files that use it.", ""]

    if example:
        lines += ["## A real one", "",
                  f"`{example['path']}`", ""]
        if example.get("value"):
            lines += ["```json", example["value"], "```", ""]
        elif example.get("fields"):
            lines += ["Too large to inline. Fields present:", "",
                      "`" + "`, `".join(example["fields"]) + "`", ""]
        if example.get("others"):
            lines += ["Others: " + ", ".join(f"`{n}`" for n in example["others"]), ""]

    lines += ["---", "",
              "Read it with the MCP server rather than by hand:",
              "",
              "```",
              f"describe_type('{full.rsplit('.', 1)[-1]}')",
              f"search_content('', type_contains='{full.rsplit('.', 1)[-1]}')",
              "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    check_only = "--check" in sys.argv
    version = sdk_version()

    try:
        conn = index.connect(read_only=True)
    except FileNotFoundError:
        print("The definition index is not built. Run build_index first.")
        return 1

    rows = type_rows(conn)
    if check_only:
        stored = VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.is_file() else "(none)"
        existing = len(list(TYPES_DIR.rglob("*.md"))) - 1 if TYPES_DIR.is_dir() else 0
        print(f"handbook built against : {stored}")
        print(f"installed SDK          : {version}")
        print(f"type pages on disk     : {existing}")
        print(f"types in content now   : {len(rows)}")
        same = stored == version and existing == len(rows)
        print("MATCH" if same else "DIFFER — rerun build_reference.py")
        return 0 if same else 2

    if TYPES_DIR.is_dir():
        for old in TYPES_DIR.rglob("*.md"):
            old.unlink()
    TYPES_DIR.mkdir(parents=True, exist_ok=True)

    by_bundle: dict[str, list[tuple[str, int, int, str]]] = {}
    names = page_names(rows)
    written = 0
    for type_name, used_by in rows:
        bundle, _, full = type_name.partition(":")
        bundle = bundle or "Unbundled"
        doc = docs.type_doc(type_name)
        example = example_for(conn, type_name)
        folder = TYPES_DIR / safe(bundle)
        folder.mkdir(parents=True, exist_ok=True)
        page = folder / f"{names[type_name]}.md"
        write_type_page(page, type_name, used_by, doc, example)
        by_bundle.setdefault(bundle, []).append(
            (full, used_by, len(doc.get("documented_fields") or {}), names[type_name]))
        written += 1

    lines = [
        "# Every type SE2 content actually uses",
        "",
        f"{written} distinct `$Type` values, taken from the {conn.execute(f'SELECT COUNT(*) n FROM assets WHERE {_IN_SDK}', SDK_PROJECTS).fetchone()['n']:,} "
        "definition files in the installed SDK (Vanilla and Engine; mods are "
        "left out). Generated — do not hand-edit.",
        "",
        "The count is what makes this list usable: a type used by 9,000 "
        "definitions is a load-bearing part of the format, and one used by a "
        "single file is a one-off. Sort your attention by it.",
        "",
    ]
    for bundle in sorted(by_bundle):
        items = sorted(by_bundle[bundle], key=lambda x: -x[1])
        lines += [f"## {bundle} ({len(items)} types)", "",
                  "| type | used by | documented fields |", "|---|---:|---:|"]
        for full, used_by, nfields, page_name in items:
            rel = f"{safe(bundle)}/{page_name}.md"
            lines.append(f"| [{full.rsplit('.', 1)[-1]}]({rel}) | {used_by} | {nfields or '—'} |")
        lines.append("")
    (TYPES_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")

    VERSION_FILE.write_text(version + "\n", encoding="utf-8")
    conn.close()
    print(f"Wrote {written} type pages for SDK {version} into {TYPES_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
