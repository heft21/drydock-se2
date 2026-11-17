"""MCP server for the Space Engineers 2 Mod SDK.

SE2 content is GUID-addressed JSON spread over ~17k definition files and ~32k
media assets. The tools here turn that into something an agent can actually work
in: resolve a GUID to a file, search vanilla content, look up what a field means,
write a definition with a valid .meta sidecar, and run the real content pipeline
to check the result.

Every optional parameter accepts ``null``, no tool raises, and the search index
builds itself on first use — so the server behaves the same whether it is driven
by a large model or by a small local one that skips the setup step. See
``toolkit.py`` for how that is arranged and how to shrink the tool list.
"""

from __future__ import annotations

import json
import sqlite3
import urllib.parse
from pathlib import Path
from typing import Any

from mcp.server.mcpserver import Image, MCPServer

from . import (audit, authoring, blender, bridge, builder, docs, editor_api,
               index, knowledge, logs, modhub, recipes, selftest, session, toolkit)
from .config import PATHS, normalize_guid

server = MCPServer(
    name="se2-modsdk",
    instructions=(
        "Space Engineers 2 Mod SDK. Content is GUID-addressed JSON: every "
        "'.def'/'.partialdef' has a $Type and $Value, and references other assets "
        "by bare GUID (sometimes '{G}'-prefixed).\n\n"
        "AT THE START OF A SESSION: work_on(). It picks the mod project "
        "to work on and installs the editor bridge. If it answers "
        "'no_active_project' it will list the projects — ASK THE USER which one "
        "and call work_on(project=<name>). Never guess, and never ask twice: "
        "the choice is remembered across sessions.\n"
        "WHEN THE USER SAYS THEY ARE DONE / READY TO PUBLISH / UPLOADING: call "
        "finish_and_publish(). It removes the bridge, which must never ship "
        "inside a mod, and tells you what still blocks publishing.\n\n"
        "The search index every lookup depends on builds itself on first use, "
        "so nothing has to be set up by hand. sdk_info reports where the SDK is "
        "and whether the index is ready.\n\n"
        "Typical workflow: search_content to find how vanilla does something -> "
        "read_definition to see it -> describe_type for what the fields mean -> "
        "write_definition to author yours -> audit_project to check it.\n\n"
        "Two knowledge tools carry things that cannot be inferred from the "
        "files: 'explain' holds measured reference facts (planet map formats, "
        "the cube-face basis, ColorKey rules, the publish-hash error, why the "
        "editor refuses to open), and 'mod_recipes' holds the build procedures. "
        "Consult them before answering a how-does-this-work question.\n\n"
        "BEFORE WRITING ANY ASSET, read explain('rules'). It is twelve short "
        "numbered rules, each measured against shipped data — cube-face slot "
        "wiring, which texture preset to use, why you must never invent a GUID "
        "for a .png/.comptex/.cubemap, and why the project has to be reloaded "
        "after an edit. Following them is the difference between a planet that "
        "works and one that is subtly wrong in a way nothing warns you about."
    ),
)

tool = toolkit.registrar(server)

# Dictionary keys and state-machine ids are GUIDs too, but they name types and
# nodes rather than assets, so they are noise in a reference listing.
_KEY_FIELD_SQL = (
    "(field LIKE '%.Key' OR field LIKE '%Keys' OR field LIKE '%Keys[%' "
    "OR field LIKE '%.Id' OR field LIKE '%Removed[%')"
)


def _as_guid(token: str, kinds: tuple[str, ...] = ("def", "partialdef", "media")) -> tuple[str | None, dict[str, Any] | None]:
    """A normalised GUID, or an error dict the tool can return as is."""
    g = normalize_guid(token.strip()) if isinstance(token, str) else None
    if g:
        return g, None
    return None, {"error": f"Not a GUID: {token!r}.",
                  "hint": "Find the asset with search_content; it reports the GUID."}


def _db() -> sqlite3.Connection:
    """A read connection, building the index first if this is a cold start."""
    index.ensure()
    return index.connect(read_only=True)


def _abs_path(rel: str) -> Path:
    """Index paths are project-relative; map one back to a real file."""
    rel_path = Path(rel)
    for base in (PATHS.game_data, *(d.parent for _, d in index.roots())):
        candidate = base / rel_path
        if candidate.exists():
            return candidate
    return PATHS.game_data / rel_path


def _pick(doc: Any, dotted: str) -> tuple[Any, str | None]:
    """Walk a dotted/indexed path into a parsed definition.

    Accepts 'Manipulator.Dummies', '$Value.Components', 'Items[0].Definition'.
    A leading '$Value.' is optional — callers usually mean the value body.
    """
    node: Any = doc
    steps: list[str] = []
    for raw in dotted.replace("[", ".[").split("."):
        tok = raw.strip()
        if not tok:
            continue
        steps.append(tok)
        if tok.startswith("[") and tok.endswith("]"):
            if not isinstance(node, list):
                return None, f"'{'.'.join(steps)}' is not a list"
            try:
                node = node[int(tok[1:-1])]
            except (ValueError, IndexError):
                return None, f"index out of range at '{'.'.join(steps)}'"
            continue
        if not isinstance(node, dict):
            return None, f"'{'.'.join(steps[:-1]) or '<root>'}' is not an object"
        if tok not in node:
            # Tolerate omitting the $Value wrapper at the first step.
            if len(steps) == 1 and isinstance(node.get("$Value"), dict) \
                    and tok in node["$Value"]:
                node = node["$Value"][tok]
                continue
            keys = list(node)[:12]
            return None, f"no field '{tok}'; available: {keys}"
        node = node[tok]
    return node, None


def _shape(node: Any) -> Any:
    """One-line stand-in describing a value that was too big to include."""
    if isinstance(node, dict):
        t = node.get("$Type")
        return {"$summary": f"object, {len(node)} fields",
                **({"$Type": t} if t else {}),
                "fields": list(node)[:24]}
    if isinstance(node, list):
        return {"$summary": f"list, {len(node)} items"}
    return node


def _fit(doc: Any, max_bytes: int) -> tuple[Any, bool]:
    """Shrink a document until it serialises under `max_bytes`.

    Collapses the deepest levels first, so the outer structure — which is what
    tells a reader where to look next — survives.
    """
    max_bytes = max(1000, max_bytes)
    if len(json.dumps(doc, default=str)) <= max_bytes:
        return doc, False

    def prune(node: Any, depth: int) -> Any:
        if depth <= 0:
            return _shape(node)
        if isinstance(node, dict):
            return {k: prune(v, depth - 1) for k, v in node.items()}
        if isinstance(node, list):
            if len(node) > 8:
                return [prune(v, depth - 1) for v in node[:8]] + \
                       [{"$summary": f"... {len(node) - 8} more items"}]
            return [prune(v, depth - 1) for v in node]
        return node

    # Deepest first, so a larger max_bytes really does buy more detail.
    for depth in range(14, 0, -1):
        candidate = prune(doc, depth)
        if len(json.dumps(candidate, default=str)) <= max_bytes:
            return candidate, True
    return prune(doc, 1), True


def _row_to_asset(r: sqlite3.Row) -> dict[str, Any]:
    out = {
        "guid": r["guid"],
        "name": r["name"] or r["stem"],
        "kind": r["kind"],
        "type": r["type"],
        "path": r["path"],
        "project": r["project"],
    }
    if r["kind"] == "partialdef":
        out["patches_base"] = r["base_guid"]
        out["produces_type"] = r["def_type"]
        out["diff_kind"] = r["diff_kind"]
    return {k: v for k, v in out.items() if v is not None}


def _clamp(value: int, low: int, high: int) -> int:
    return max(low, min(int(value), high))


def _match(query: str, columns: tuple[str, ...]) -> tuple[str, list[str]]:
    """A WHERE fragment matching every word of `query` across `columns`.

    SE2 file names are PascalCase with no separators — 'IonThruster500' — so a
    plain substring search finds nothing for the way a person (or a model) says
    it: "ion thruster 500". Requiring each word to appear somewhere in the row
    bridges that without any fuzzy matching, and keeps precision, because every
    word still has to be present.
    """
    tokens = [t for t in query.split() if t] or [query]
    clauses, params = [], []
    for token in tokens:
        clauses.append("(" + " OR ".join(f"{c} LIKE ?" for c in columns) + ")")
        params += [f"%{token}%"] * len(columns)
    return " AND ".join(clauses), params


# --------------------------------------------------------------------------
# Discovery
# --------------------------------------------------------------------------

@tool(
    group="checking",
    description=(
        "START HERE, before any other tool that touches a mod. Says which mod "
        "project this session is working on and gets it ready.\n\n"
        "Call it with no arguments: if exactly one project exists it is picked "
        "automatically, otherwise you get the list and must ask the user which "
        "one — do not guess. Call it again with project=<name> to switch.\n\n"
        "It also installs the editor bridge, so editor_* tools work afterwards. "
        "When the user says they are done and want to publish, call "
        "finish_and_publish — that removes the bridge again, which is required."
        " Example: work_on()"
    ),
)
def work_on(project: str | None = None, install_editor_bridge: bool | None = True) -> dict[str, Any]:
    path, problem = session.require(project)
    if problem is not None:
        return problem
    session.set_active(path)

    out: dict[str, Any] = {
        "status": "ready",
        "project": path,
        "name": Path(path).name,
        "next": "Author with write_definition, then check with audit_project.",
    }
    try:
        out["audit"] = {k: v for k, v in audit.audit(path).items()
                        if k in ("ok", "error_count", "warning_count")}
    except Exception as exc:
        out["audit"] = {"error": str(exc)}

    if install_editor_bridge is None or install_editor_bridge:
        try:
            out["bridge"] = bridge.install(path, copy_into_project=False)
            out["bridge_reminder"] = (
                "The bridge is installed. It must NOT ship in a published mod — "
                "call finish_and_publish before publishing."
            )
        except Exception as exc:
            out["bridge"] = {"error": str(exc),
                             "note": "Content tools still work; editor_* will not."}
    return out


@tool(
    group="checking",
    description=(
        "Call this when the user says the mod is finished, ready, or that they "
        "want to publish or upload it.\n\n"
        "Removes the editor bridge (which must never ship), then audits the "
        "project and reports whether it is publishable. Read the returned "
        "'blocking' list — if it is empty the project is ready for Mod HUB."
        " Example: finish_and_publish()"
    ),
)
def finish_and_publish(project: str | None = None) -> dict[str, Any]:
    path, problem = session.require(project)
    if problem is not None:
        return problem

    out: dict[str, Any] = {"project": path, "name": Path(path).name}
    blocking: list[str] = []

    try:
        out["bridge_removed"] = bridge.uninstall(path)
    except Exception as exc:
        out["bridge_removed"] = {"error": str(exc)}
        blocking.append(f"Could not remove the editor bridge: {exc}")

    try:
        report = audit.audit(path)
        out["audit"] = {k: v for k, v in report.items()
                        if k in ("ok", "error_count", "warning_count")}
        if report.get("error_count"):
            blocking.append(
                f"{report['error_count']} audit errors — call audit_project for detail.")
    except Exception as exc:
        blocking.append(f"Audit failed: {exc}")

    root = Path(path)
    if not (root / "thumb.jpg").exists():
        blocking.append("thumb.jpg is missing from the project root.")
    try:
        proj = json.loads(next(root.glob("*.vrgproj")).read_text(encoding="utf-8-sig"))
        if proj.get("$Value", {}).get("EditorExtensionAssemblies"):
            blocking.append("EditorExtensionAssemblies is still populated in the .vrgproj.")
    except (StopIteration, OSError, ValueError):
        pass

    out["blocking"] = blocking
    out["status"] = "ready_to_publish" if not blocking else "not_ready"
    out["next"] = ("Open Mod HUB and press Publish — it has no command line."
                   if not blocking else "Fix everything in 'blocking', then call this again.")
    return out


@tool(
    group="lookup",
    description=(
        "Where the SDK lives, which tools are available, and whether the search "
        "index is built. Use it when a lookup cannot find the SDK."
        " Takes no arguments: sdk_info()"
    ),
)
def sdk_info() -> dict[str, Any]:
    status = index.index_status()
    out: dict[str, Any] = {
        "sdk_root": str(PATHS.sdk),
        "game_data": str(PATHS.game_data),
        "problems": PATHS.check() or None,
        "content_pipeline": builder.version(),
        "index": status,
        "field_docs_built": docs.is_built(),
    }
    if not status.get("built"):
        index.start_background_build()
        out["note"] = (
            "The index is being built in the background — it scans ~50,000 SDK "
            "files and takes a couple of minutes the first time on a machine. "
            "Nothing needs doing; lookups start working once it finishes."
        )
    elif status.get("stale"):
        index.refresh_if_stale(force_check=True)
        status = index.index_status()
        out["index"] = status
        if status.get("refreshing"):
            out["note"] = (
                f"Index was out of date ({status.get('stale') or 'changed since it was built'}). "
                f"It is being refreshed in the background; nothing needs doing, "
                f"lookups keep working on the previous index meanwhile.")
        else:
            out["note"] = f"Index is out of date: {status.get('stale')}. Call build_index."
    else:
        out["note"] = (
            "Set SE2_MCP_MOD_ROOTS to index mod projects from somewhere other "
            "than Mod HUB's own mods directory."
        )
    limits = toolkit.selection_note()
    if limits:
        out["tool_selection"] = limits
    # The SDK's own two projects are always there; what is worth reporting is
    # whether the user's mods were found, since that is what detection can miss.
    out["mod_projects_detected"] = [
        name for name, _ in index.roots() if name not in ("Vanilla", "Engine")
    ]
    return out


@tool(
    group="lookup",
    description=(
        "Rebuild the definition index and the field-documentation cache. Scans "
        "~50k SDK files (measured: 17,633 definitions, 32,297 media assets, "
        "170,096 reference edges). A rebuild takes ~15 seconds once the files "
        "are in the OS cache, a couple of minutes the first time on a machine — "
        "long enough that the call may hit a client timeout while the work "
        "continues and completes anyway.\n\n"
        "The index builds itself at startup when missing, so this is only "
        "needed after a game update; a new or removed mod project is picked up by itself."
        " Takes no arguments: build_index()"
    ),
)
def build_index(include_field_docs: bool | None = True) -> dict[str, Any]:
    result: dict[str, Any] = {"index": index.build().as_dict()}
    index.clear_refresh_failure()
    if include_field_docs:
        result["field_docs"] = docs.build()
    return result


@tool(
    group="checking",
    description=(
        "Prove the whole server works, end to end: paths, index, field docs, a "
        "real definition read, and a scaffold/write/audit round trip in a "
        "temporary folder that is deleted afterwards. Also reports whether the "
        "editor, Mod HUB and Blender are reachable.\n\n"
        "Run this when something behaves unexpectedly, or once after install to "
        "confirm the setup — it names the specific broken step instead of "
        "leaving a tool call to fail later."
        " Takes no arguments: self_test()"
    ),
)
def self_test(include_live_apps: bool | None = True) -> dict[str, Any]:
    return selftest.run(include_live_apps=bool(include_live_apps))


# --------------------------------------------------------------------------
# Search and resolution
# --------------------------------------------------------------------------

@tool(
    group="lookup",
    description=(
        "Search vanilla and indexed mod content by name, file path or $Type. "
        "This is the main way to find how the base game does something — e.g. "
        "query='Thruster', or query='Battery' with kind='partialdef'. "
        "kind: def | partialdef | media | any."
        " Example: search_content(query='ion thruster')"
    ),
)
def search_content(
    query: str,
    kind: str | None = "any",
    type_contains: str | None = "",
    project: str | None = "",
    limit: int | None = 25,
) -> dict[str, Any]:
    limit = _clamp(limit, 1, 200)
    kind = (kind or "any").strip().lower()
    if kind not in ("any", "def", "partialdef", "media"):
        return {"error": f"kind must be any, def, partialdef or media (got {kind!r})"}
    conn = _db()

    def look(term: str) -> list[dict[str, Any]]:
        found: list[dict[str, Any]] = []
        if kind in ("any", "def", "partialdef"):
            where, params = _match(term, ("stem", "subject", "name", "path"))
            sql = f"SELECT * FROM assets WHERE {where}"
            if kind != "any":
                sql += " AND kind=?"
                params.append(kind)
            if type_contains:
                sql += " AND type LIKE ?"
                params.append(f"%{type_contains}%")
            if project:
                sql += " AND project=?"
                params.append(project)
            # Prefer exact-ish name matches over deep path matches.
            sql += " ORDER BY (stem=?) DESC, LENGTH(stem) LIMIT ?"
            params += [term, limit]
            found += [_row_to_asset(r) for r in conn.execute(sql, params)]

        if kind in ("any", "media") and len(found) < limit:
            where, params = _match(term, ("stem", "path"))
            sql = f"SELECT * FROM files WHERE {where}"
            if project:
                sql += " AND project=?"
                params.append(project)
            sql += " ORDER BY LENGTH(stem) LIMIT ?"
            params.append(limit - len(found))
            found += [
                {"guid": r["guid"], "name": r["stem"], "kind": "media",
                 "ext": r["ext"], "processor": r["processor"], "path": r["path"],
                 "project": r["project"]}
                for r in conn.execute(sql, params)
            ]
        return found

    results = look(query)
    out: dict[str, Any] = {"query": query, "count": len(results), "results": results}

    # A multi-word query that matches nothing usually has one word too many
    # ("large ion thruster"). Retrying on the most specific word finds the
    # neighbourhood, which is what the caller needed anyway.
    if not results:
        words = sorted((w for w in query.split() if len(w) > 2), key=len, reverse=True)
        if len(words) > 1:
            results = look(words[0])
            if results:
                out.update(count=len(results), results=results,
                           relaxed_to=words[0],
                           note=f"No row matched every word, so this is a search "
                                f"for '{words[0]}' alone.")

    conn.close()
    if not out["results"]:
        out["hint"] = (
            "Nothing matched. Search looks for every word of the query inside "
            "the file name, path or $Type, so try fewer or shorter words "
            "('thruster' rather than 'large ion thruster block'), or call "
            "list_types to see what kinds of definition exist."
        )
    return out


@tool(
    group="lookup",
    description=(
        "Resolve a GUID to the asset it identifies — the single most useful "
        "operation when reading SE2 content, since definitions reference each "
        "other by bare GUID. Accepts '{G}'-prefixed GUIDs. Also reports how many "
        "other definitions point at it."
        " Example: resolve_guid(guid='11223344-5566-7788-99aa-bbccddeeff00')"
    ),
)
def resolve_guid(guid: str) -> dict[str, Any]:
    g, err = _as_guid(guid)
    if err:
        return err
    conn = _db()

    row = conn.execute("SELECT * FROM assets WHERE guid=?", (g,)).fetchone()
    if row:
        out = _row_to_asset(row)
        out["found_in"] = "definition"
        if row["base_guid"]:
            base = conn.execute(
                "SELECT stem, path, type FROM assets WHERE guid=?", (row["base_guid"],)
            ).fetchone()
            if base:
                out["base"] = {"name": base["stem"], "path": base["path"],
                               "type": base["type"]}
    else:
        row = conn.execute("SELECT * FROM files WHERE guid=?", (g,)).fetchone()
        if row:
            out = {"guid": g, "found_in": "media", "name": row["stem"],
                   "ext": row["ext"], "processor": row["processor"],
                   "path": row["path"], "project": row["project"]}
        else:
            nested = conn.execute(
                "SELECT * FROM nested WHERE guid=? LIMIT 1", (g,)
            ).fetchone()
            if nested:
                out = {"guid": g, "found_in": "nested_object",
                       "type": nested["type"], "inside": nested["path"],
                       "at_field": nested["field"], "owner_guid": nested["owner"]}
            else:
                n = conn.execute(
                    "SELECT COUNT(*) n FROM refs WHERE dst=?", (g,)
                ).fetchone()["n"]
                conn.close()
                return {
                    "guid": g,
                    "found_in": None,
                    "referenced_by_count": n,
                    "note": (
                        "Not an asset. SE2 also uses GUIDs as dictionary keys "
                        "(component types, mesh parts) and as animation node ids; "
                        "those have no file behind them."
                    ) if n else "Unknown GUID — not present anywhere in the index.",
                }

    out["referenced_by_count"] = conn.execute(
        f"SELECT COUNT(*) n FROM refs WHERE dst=? AND NOT {_KEY_FIELD_SQL}", (g,)
    ).fetchone()["n"]
    conn.close()
    return out


@tool(
    group="lookup",
    description=(
        "List the definitions that reference a GUID (reverse dependency lookup). "
        "Use it to answer 'what breaks if I change this?' or 'which blocks use "
        "this model?'. Dictionary-key GUIDs are excluded unless include_keys."
        " Example: find_references(guid='11223344-5566-7788-99aa-bbccddeeff00')"
    ),
)
def find_references(
    guid: str,
    include_keys: bool | None = False,
    limit: int | None = 40,
) -> dict[str, Any]:
    g, err = _as_guid(guid)
    if err:
        return err
    conn = _db()
    sql = (
        "SELECT r.src, r.field, a.stem, a.path, a.type, a.kind "
        "FROM refs r LEFT JOIN assets a ON a.guid = r.src WHERE r.dst = ?"
    )
    if not include_keys:
        sql += f" AND NOT {_KEY_FIELD_SQL}"
    total = conn.execute(
        sql.replace(
            "SELECT r.src, r.field, a.stem, a.path, a.type, a.kind",
            "SELECT COUNT(*) n", 1), (g,)
    ).fetchone()["n"]
    rows = conn.execute(sql + " LIMIT ?", (g, _clamp(limit, 1, 200))).fetchall()
    conn.close()
    return {
        "guid": g,
        "total": total,
        "shown": len(rows),
        "referenced_by": [
            {"name": r["stem"], "path": r["path"], "type": r["type"],
             "kind": r["kind"], "at_field": r["field"], "guid": r["src"]}
            for r in rows
        ],
    }


@tool(
    group="lookup",
    description=(
        "Read a definition, by GUID or path, with a resolution table naming "
        "every GUID it references so the content is readable without further "
        "lookups.\n\n"
        "Composite definitions reach hundreds of KB, so the content is shape-"
        "summarised once it exceeds max_bytes. Use `at` with a dotted path "
        "(e.g. '$Value.Manipulator.Dummies' or 'Manipulator.Model') to read one "
        "subtree in full instead of raising max_bytes."
        " Example: read_definition(target='11223344-5566-7788-99aa-bbccddeeff00')"
    ),
)
def read_definition(
    target: str,
    resolve_references: bool | None = True,
    at: str | None = "",
    max_bytes: int | None = 12000,
) -> dict[str, Any]:
    g = normalize_guid(target.strip())
    conn = _db()
    if g:
        row = conn.execute("SELECT path FROM assets WHERE guid=?", (g,)).fetchone()
        if not row:
            conn.close()
            return {"error": f"No definition with GUID {g}. Try resolve_guid."}
        path = _abs_path(row["path"])
    else:
        path = Path(target)
        if not path.is_absolute():
            path = _abs_path(target)
    if not path.is_file():
        conn.close()
        return {"error": f"File not found: {path}",
                "hint": "Pass a GUID, or a path as search_content reports it."}

    try:
        doc = json.loads(path.read_text(encoding="utf-8-sig"))
    except (json.JSONDecodeError, OSError) as exc:
        conn.close()
        return {"error": f"Could not read {path}: {exc}"}

    full = doc                    # the reference table always uses the whole file
    if at:
        picked, err = _pick(doc, at)
        if err:
            conn.close()
            return {"error": err, "path": str(path)}
        doc = picked

    out: dict[str, Any] = {"path": str(path)}
    if at:
        out["at"] = at
    shown, trimmed = _fit(doc, max_bytes)
    out["content"] = shown
    if trimmed:
        out["truncated"] = True
        out["hint"] = (
            "Content was shape-summarised to fit max_bytes. Pass `at` with a "
            "dotted path to read one subtree in full, e.g. "
            "at='$Value.Manipulator'."
        )

    if resolve_references:
        value = full.get("$Value", {}) if isinstance(full, dict) else {}
        own = index._own_guid(path.suffix.lstrip("."), value) if isinstance(value, dict) else None
        seen: dict[str, str] = {}
        for dst, fld in index._walk_guids(value):
            if dst != own:
                seen.setdefault(dst, fld)
        table = {}
        for dst, fld in list(seen.items())[:120]:
            a = conn.execute(
                "SELECT stem, type, kind FROM assets WHERE guid=?", (dst,)
            ).fetchone()
            if a:
                table[dst] = {"name": a["stem"], "type": a["type"], "kind": a["kind"],
                              "at_field": fld}
                continue
            f = conn.execute("SELECT stem, ext FROM files WHERE guid=?", (dst,)).fetchone()
            if f:
                table[dst] = {"name": f["stem"] + (f["ext"] or ""), "kind": "media",
                              "at_field": fld}
        out["referenced_assets"] = table
        out["unresolved_guids"] = len(seen) - len(table)
    conn.close()
    return out


@tool(
    group="lookup",
    description=(
        "Every file belonging to one content subject, e.g. subject='Battery50' or "
        "'ArmorCornerHeavy250'. SE2 splits a single block across many files "
        "(model, placement, server/client composition, inventory...); this shows "
        "the whole set, which is the fastest way to learn a block's structure."
        " Example: subject_files(subject='IonThruster500')"
    ),
)
def subject_files(subject: str, limit: int | None = 60) -> dict[str, Any]:
    limit = _clamp(limit, 1, 200)
    conn = _db()
    rows = conn.execute(
        "SELECT * FROM assets WHERE subject=? OR stem LIKE ? ORDER BY kind, stem LIMIT ?",
        (subject, f"{subject}\\_%", limit),
    ).fetchall()
    # Media was previously unbounded, so a block with many textures returned
    # kilobytes regardless of `limit`.
    media_cap = min(limit, 60)
    media = conn.execute(
        "SELECT guid, stem, ext FROM files WHERE stem LIKE ? ORDER BY stem LIMIT ?",
        (f"{subject}%", media_cap),
    ).fetchall()
    media_total = conn.execute(
        "SELECT COUNT(*) n FROM files WHERE stem LIKE ?", (f"{subject}%",)
    ).fetchone()["n"]
    conn.close()
    out = {
        "subject": subject,
        "definitions": [_row_to_asset(r) for r in rows],
        "media": [dict(r) for r in media],
        "media_total": media_total,
    }
    if not rows and not media:
        out["hint"] = (
            "No such subject. A subject is the leading token of a file name — "
            "'IonThruster500', not 'Ion Thruster'. Find one with search_content."
        )
    return out


# --------------------------------------------------------------------------
# Schema
# --------------------------------------------------------------------------

@tool(
    group="lookup",
    description=(
        "List the $Type values that exist in SE2 content, with how many "
        "definitions use each. Filter with `contains`, e.g. 'Thruster' or "
        "'CubeBlock'. Use this to discover what kinds of things are definable."
        " Example: list_types(contains='Thruster')"
    ),
)
def list_types(contains: str | None = "", limit: int | None = 40) -> dict[str, Any]:
    limit = _clamp(limit, 1, 300)
    conn = _db()
    if contains:
        rows = conn.execute(
            "SELECT type, n FROM types WHERE type LIKE ? ORDER BY n DESC LIMIT ?",
            (f"%{contains}%", limit),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT type, n FROM types ORDER BY n DESC LIMIT ?", (limit,),
        ).fetchall()
    total = conn.execute("SELECT COUNT(*) n FROM types").fetchone()["n"]
    conn.close()
    return {"distinct_types": total,
            "types": [{"type": r["type"], "used_by": r["n"]} for r in rows]}


@tool(
    group="lookup",
    description=(
        "What a definition type's fields mean. Combines the SDK's own XML "
        "documentation (authoritative per-field summaries) with real values taken "
        "from vanilla files. Accepts a bundle-qualified name "
        "('Game2:Keen.Game2...X') or any unique fragment of it."
        " Example: describe_type(type_name='MyObjectBuilder_CubeBlock')"
    ),
)
def describe_type(type_name: str, with_example: bool | None = True) -> dict[str, Any]:
    conn = _db()
    row = conn.execute(
        "SELECT type FROM types WHERE type = ? OR type LIKE ? ORDER BY LENGTH(type) LIMIT 1",
        (type_name, f"%{type_name}%"),
    ).fetchone()
    resolved = row["type"] if row else type_name

    doc = docs.type_doc(resolved)
    out: dict[str, Any] = {
        "type": resolved,
        "summary": doc["summary"],
        "documented_fields": doc["documented_fields"],
    }
    if not doc["documented_fields"]:
        near = docs.search_types(type_name.split(".")[-1].split(":")[-1], 8)
        if near:
            out["did_you_mean"] = near
        elif not docs.is_built():
            out["hint"] = ("The field-documentation cache is empty. Call "
                           "build_index to extract it from the SDK's XML files.")

    if with_example and row:
        ex = conn.execute(
            "SELECT guid, stem, path FROM assets WHERE type=? ORDER BY LENGTH(path) LIMIT 1",
            (resolved,),
        ).fetchone()
        if ex:
            try:
                content = json.loads(
                    _abs_path(ex["path"]).read_text(encoding="utf-8-sig")
                )
                value = content.get("$Value", {})
                out["example"] = {"path": ex["path"], "name": ex["stem"]}
                # Whole composites can be megabytes; show shape, not bulk.
                dumped = json.dumps(value, indent=2)
                out["example"]["value"] = (
                    value if len(dumped) < 6000
                    else {"$truncated": True, "fields": sorted(value.keys())}
                )
            except (json.JSONDecodeError, OSError):
                pass
        out["also_used_by"] = conn.execute(
            "SELECT COUNT(*) n FROM assets WHERE type=?", (resolved,)
        ).fetchone()["n"]
    conn.close()
    return out


# --------------------------------------------------------------------------
# Authoring
# --------------------------------------------------------------------------

@tool(
    group="authoring",
    description=(
        "Create a new, buildable mod project (.vrgproj, Assets definition set and "
        "Mod HUB publish metadata) in an empty directory. Uses the project layout "
        "measured to load and publish correctly.\n\n"
        "Leave depend_on_vanilla on: without the Vanilla dependency nothing from "
        "the base game can be referenced and every partialdef fails to resolve "
        "its base. The one cost is that validate_project (the standalone CLI) "
        "cannot load such a project — use audit_project and editor_validation "
        "instead, which is what real mods do anyway."
        " Example: scaffold_mod(directory='C:/Mods/MyMod', name='MyMod')"
    ),
)
def scaffold_mod(
    directory: str,
    name: str,
    depend_on_vanilla: bool | None = True,
    summary: str | None = "",
) -> dict[str, Any]:
    try:
        return authoring.scaffold_mod(
            directory, name,
            depend_on_vanilla=bool(depend_on_vanilla),
            summary=summary or "",
        )
    except (FileExistsError, OSError, ValueError) as exc:
        return {"error": str(exc)}


@tool(group="authoring", description="Generate fresh GUIDs for new definitions. Example: new_guids(count=1)")
def new_guids(count: int | None = 1) -> dict[str, Any]:
    return {"guids": [authoring.new_guid() for _ in range(_clamp(count, 1, 50))]}


@tool(
    group="authoring",
    description=(
        "Write a .def or .partialdef together with a correct .meta sidecar "
        "(AssetID + MD5 content hash, the format the content pipeline expects). "
        "`value` is the $Value object. `path` must be absolute, inside your own "
        "mod project — never inside the SDK's GameData. Refuses to overwrite "
        "unless overwrite=true, and keeps a copy in .backups/ when it does.\n"
        " Example: write_definition(path='C:/Mods/MyMod/Content/my.partialdef', type_name='MyObjectBuilder_CubeBlock', value={'Id': 'x'})"
    ),
)
def write_definition(
    path: str,
    type_name: str,
    value: dict[str, Any],
    guid: str | None = "",
    overwrite: bool | None = False,
) -> dict[str, Any]:
    target = Path(path)
    if not target.is_absolute():
        return {
            "error": f"path must be absolute, got {path!r}.",
            "hint": ("A relative path would land wherever the server process "
                     "happens to run. Use the full path to the file inside your "
                     "mod project — modhub_projects lists their directories."),
        }
    try:
        if target.resolve().is_relative_to(PATHS.game_data.resolve()):
            return {
                "error": "Refusing to write inside the SDK's GameData. "
                         "Create the file in your own mod project instead.",
                "sdk_game_data": str(PATHS.game_data),
            }
    except OSError:
        pass
    try:
        out = authoring.write_definition(
            path, type_name, value, guid=guid or None, overwrite=bool(overwrite)
        )
    except (ValueError, FileExistsError, OSError) as exc:
        return {"error": str(exc)}
    return out


@tool(
    group="authoring",
    description=(
        "Recompute a definition's .meta sidecar after editing the file by hand. "
        "The pipeline compares the stored hash against the file, so a stale .meta "
        "makes the asset look corrupt."
        " Example: refresh_meta(def_path='C:/Mods/MyMod/Content/my.partialdef')"
    ),
)
def refresh_meta(def_path: str) -> dict[str, Any]:
    target = Path(def_path)
    try:
        if target.is_absolute() and target.resolve().is_relative_to(PATHS.game_data.resolve()):
            return {"error": "Refusing to rewrite a sidecar inside the SDK's "
                             "GameData; the shipped tree is reference material."}
    except OSError:
        pass
    try:
        return authoring.refresh_meta(def_path)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as exc:
        return {"error": str(exc)}


# --------------------------------------------------------------------------
# Content pipeline
# --------------------------------------------------------------------------

@tool(
    group="checking",
    description=(
        "Check a mod project for structural errors without the editor or the "
        "CLI. Use this on any Vanilla-dependent project — that is, every real "
        "mod — because validate_project physically cannot load one.\n\n"
        "Finds: definitions the game will never mount (an Assets.meta with no "
        "DefinitionSetItem silently disables the whole mod), '.meta' sidecars "
        "whose source file is gone, stale content hashes, GUID collisions, "
        "definition/'.meta' AssetID mismatches, and references to GUIDs that "
        "exist nowhere. Cross-project references are resolved against the index, "
        "so pointing at vanilla content is not reported as an error."
        " Example: audit_project(project='MyMod')"
    ),
)
def audit_project(project: str, check_hashes: bool | None = True) -> dict[str, Any]:
    # Every check except cross-project reference resolution works without the
    # index, so a build still in progress must not block the audit — it only
    # means a reference into vanilla content cannot be confirmed yet.
    indexed = True
    try:
        index.ensure(wait=10)
    except (index.IndexBuilding, FileNotFoundError, RuntimeError):
        indexed = False
    try:
        report = audit.audit(project, check_hashes=bool(check_hashes))
    except (OSError, ValueError) as exc:
        return {"error": str(exc)}
    if not indexed and isinstance(report, dict):
        report["index_unavailable"] = (
            "The search index is not ready, so references into vanilla content "
            "could not be resolved and may appear as unresolved_ref. Re-run "
            "this once sdk_info reports the index as built."
        )
    return report


@tool(
    group="checking",
    description=(
        "Validate a mod project with the SDK's own content pipeline (dry run — "
        "writes nothing). Only works for projects that depend on Engine alone; "
        "for anything depending on Vanilla use audit_project and "
        "editor_validation instead. Pass the .vrgproj file or its folder."
        " Example: validate_project(project='MyMod')"
    ),
)
def validate_project(project: str, verbose: bool | None = False) -> dict[str, Any]:
    try:
        return builder.run(project, dry_run=True, verbose=bool(verbose))
    except FileNotFoundError as exc:
        return {"ok": False, "error": str(exc)}


@tool(
    group="checking",
    description=(
        "Run the content pipeline for real. Modes: 'full' (default) processes "
        "assets into Content/ and then generates the cache blobs the game loads — "
        "this is what you normally want; 'process' only converts assets; 'caches' "
        "only rebuilds the blobs; 'publish' stages a release into output_dir. "
        "Writes to disk."
        " Example: build_project(project='MyMod')"
    ),
)
def build_project(
    project: str,
    mode: str | None = "full",
    output_dir: str | None = "",
    verbose: bool | None = False,
) -> dict[str, Any]:
    mode = (mode or "full").strip().lower()
    verbose = bool(verbose)
    if mode not in ("full", "process", "caches", "publish"):
        return {"ok": False, "error": "mode must be full, process, caches or publish"}
    if mode == "publish" and not output_dir:
        return {"ok": False, "error": "publish mode needs output_dir"}
    try:
        if mode == "publish":
            return builder.run(project, prepare_for_publish=output_dir, verbose=verbose)
        if mode == "caches":
            return builder.run(project, generate_caches=True, metadata=True, verbose=verbose)

        # Assets must be converted into Content/ before the cache blobs are
        # built; a caches-only run leaves the per-file outputs missing and the
        # next validation fails on them.
        processed = builder.run(project, verbose=verbose)
        if mode == "process" or not processed["ok"]:
            return processed
        cached = builder.run(project, generate_caches=True, metadata=True, verbose=verbose)
        cached["process_step"] = {"ok": processed["ok"], "exit_code": processed["exit_code"]}
        return cached
    except FileNotFoundError as exc:
        return {"ok": False, "error": str(exc)}


@tool(
    group="logs",
    description=(
        "Read what the Editor, Mod HUB or the game itself logged. "
        "app: 'modhub' | 'editor' | 'game'.\n\n"
        "'modhub' is the only way to see a publish failure, since publishing "
        "runs inside the HUB and leaves no trace in the editor. 'game' is the "
        "only way to see what a mod did once loaded — which local mods were "
        "discovered, which subsystems initialised, and whether a feature "
        "actually ran. Defaults to the most recent run; use `contains` to grep "
        "(e.g. 'publish', 'Discovered local mod', 'Water', a mod name). Works "
        "after the fact, including for a run that already exited."
        " Example: read_app_log(app='modhub', errors_only=True)"
    ),
)
def read_app_log(
    app: str | None = "modhub",
    file_name: str | None = "",
    contains: str | None = "",
    errors_only: bool | None = True,
    tail: int | None = 40,
) -> dict[str, Any]:
    try:
        return logs.read(app or "modhub", file_name or "", contains or "",
                         bool(errors_only), _clamp(tail, 1, 500))
    except (ValueError, OSError) as exc:
        return {"error": str(exc)}


@tool(
    group="logs",
    description=(
        "List recent Editor, Mod HUB or game log runs, newest first, so a "
        "specific session can be picked out and read with read_app_log. "
        "app: 'modhub' | 'editor' | 'game'."
        " Example: list_app_logs(app='modhub', limit=10)"
    ),
)
def list_app_logs(app: str | None = "modhub", limit: int | None = 10) -> dict[str, Any]:
    app = app or "modhub"
    try:
        return {"app": app, "runs": logs.list_runs(app, _clamp(limit, 1, 100))}
    except (ValueError, OSError) as exc:
        return {"error": str(exc)}


# --------------------------------------------------------------------------
# Live editor bridge
# --------------------------------------------------------------------------

@tool(
    group="editor",
    description=(
        "Is the running editor reachable? Reports whether VRage.Editor.exe is up "
        "with the SE2McpBridge plugin loaded, and whether the plugin is built. "
        "Call this before any other editor_* tool."
        " Takes no arguments: editor_status()"
    ),
)
def editor_status() -> dict[str, Any]:
    out: dict[str, Any] = {
        "bridge_url": bridge.base_url(),
        "plugin_built": bridge.plugin_built(),
        "plugin_build_dir": str(bridge.PLUGIN_BUILD_DIR),
        "token_file": str(bridge.token_path()),
        "token_present": bridge.read_token() is not None,
    }
    try:
        out["editor"] = bridge.get_json("/ping", timeout=5)
        out["connected"] = True
    except bridge.BridgeDown as exc:
        out["connected"] = False
        out["reason"] = str(exc)
        if not bridge.plugin_built():
            out["next_step"] = (
                "The plugin is not built. Run 'dotnet build -c Release' in the "
                "bridge/ folder of this repository, then install_bridge(project)."
            )
        else:
            out["next_step"] = (
                "Run install_bridge(project) once, then launch_editor(project) "
                "and poll editor_status until connected is true (~10-40s)."
            )
    return out


@tool(
    group="editor",
    description=(
        "Register the bridge plugin with a mod project so the editor loads it on "
        "next launch. Run once per project; the plugin must be built first "
        "(dotnet build -c Release in bridge/).\n\n"
        "By default nothing is copied into the mod — the project just points at "
        "this repository's build output, which keeps the bridge out of anything "
        "published to the Workshop. Set copy_into_project=true only if the editor "
        "runs where this repository is not reachable."
        " Example: install_bridge(project='MyMod')"
    ),
)
def install_bridge(project: str, copy_into_project: bool | None = False) -> dict[str, Any]:
    try:
        return bridge.install(project, copy_into_project=bool(copy_into_project))
    except (FileNotFoundError, OSError, json.JSONDecodeError) as exc:
        return {"error": str(exc)}


@tool(
    group="editor",
    description=(
        "Remove the bridge from a mod project — drops it from the .vrgproj and "
        "deletes any copied plugin folder. Do this before publishing: the bridge "
        "runs arbitrary C# over an HTTP listener and must not ship inside a mod."
        " Example: uninstall_bridge(project='MyMod')"
    ),
)
def uninstall_bridge(project: str) -> dict[str, Any]:
    try:
        return bridge.uninstall(project)
    except (FileNotFoundError, OSError, json.JSONDecodeError) as exc:
        return {"error": str(exc)}


@tool(
    group="editor",
    description=(
        "What the editor is doing right now: loaded project, and the selected / "
        "opened / inspected asset. A snapshot — use editor_events to watch changes."
        " Takes no arguments: editor_state()"
    ),
)
def editor_state() -> dict[str, Any]:
    try:
        return bridge.get_json("/state")
    except bridge.BridgeDown as exc:
        return {"error": str(exc)}


@tool(
    group="editor",
    description=(
        "Watch the editor moment to moment. Returns events newer than `since` — "
        "selection changes, project loads, executed code, errors. Each reply "
        "carries latest_event_id; pass it back as `since` next time to get only "
        "what is new. Start with since=0."
        " Example: editor_events(since=0, limit=100)"
    ),
)
def editor_events(since: int | None = 0, limit: int | None = 100) -> dict[str, Any]:
    try:
        return bridge.get_json(f"/events?since={int(since or 0)}&limit={_clamp(limit, 1, 500)}")
    except bridge.BridgeDown as exc:
        return {"error": str(exc)}


@tool(
    group="editor",
    description=(
        "Run C# inside the running editor process — the way to actually do "
        "things in the editor. Variables persist between calls, so state can be "
        "built up. Runs on the Avalonia UI thread by default, which is required "
        "for anything touching windows, view models or the render view; set "
        "ui_thread=false for pure computation.\n\n"
        "The editor's services are `internal`, so reach them by reflection: "
        "`EditorApi.GetService(\"Keen.VRage.Editor.Services.Selection.ISelectionService\")`. "
        "EditorApi.FindType(name) resolves any loaded type.\n\n"
        "**Call `EditorApi.Watchdog()` inside any loop.** A script on the UI "
        "thread cannot be aborted from outside, so an unbounded loop freezes the "
        "editor until it is killed; Watchdog() throws once timeout_ms is spent. "
        "This executes arbitrary code in the editor — read it before you run it."
        " Example: editor_eval(code='return 1 + 1;')"
    ),
)
def editor_eval(
    code: str,
    ui_thread: bool | None = True,
    timeout_ms: int | None = 30000,
) -> dict[str, Any]:
    timeout_ms = _clamp(timeout_ms, 1000, 600000)
    try:
        return bridge.post_json(
            "/eval",
            {"code": code, "ui_thread": bool(ui_thread), "timeout_ms": timeout_ms},
            timeout=max(10, int(timeout_ms / 1000) + 15),
        )
    except bridge.BridgeDown as exc:
        return {"error": str(exc)}


@tool(
    group="editor",
    description=(
        "Forget variables defined by earlier editor_eval calls and start a fresh "
        "script session."
        " Takes no arguments: editor_eval_reset()"
    ),
)
def editor_eval_reset() -> dict[str, Any]:
    try:
        return bridge.get_json("/eval/reset")
    except bridge.BridgeDown as exc:
        return {"error": str(exc)}


@tool(
    group="editor",
    description=(
        "Look up one of the editor's registered services by type name, to check "
        "it exists and see its runtime type before driving it with editor_eval. "
        "Example: editor_service(type_name='Keen.VRage.Editor.Services.Project."
        "IProjectsService')"
    ),
)
def editor_service(type_name: str) -> dict[str, Any]:
    try:
        return bridge.get_json(f"/service?type={urllib.parse.quote(type_name)}")
    except bridge.BridgeDown as exc:
        return {"error": str(exc)}


@tool(
    group="editor",
    description=(
        "See inside the editor: capture its window as a PNG image. A minimized "
        "editor is restored first. The window must not be covered by another "
        "one — the 3D viewport is a native GPU surface, so this is a window "
        "copy rather than an offscreen render."
        " Takes no arguments: editor_screenshot()"
    ),
)
def editor_screenshot(restore_window: bool | None = True) -> Any:
    # Windows parks a minimized window at -32000,-32000 with a title-bar-sized
    # rect, and the capture of that is a valid PNG a few hundred pixels wide.
    # Raising the window is cheaper than explaining the sliver afterwards.
    if restore_window:
        _run_snippet(editor_api.SHOW_WINDOW, timeout_ms=15000)
    try:
        png = bridge.get_bytes("/screenshot", timeout=30)
    except bridge.BridgeDown as exc:
        return {"error": str(exc)}
    if png[:8] != b"\x89PNG\r\n\x1a\n":
        # The bridge reports failures as JSON on the same endpoint.
        try:
            return json.loads(png)
        except json.JSONDecodeError:
            return {"error": "Screenshot endpoint returned unexpected data"}
    return Image(data=png, format="png")


def _run_snippet(code: str, timeout_ms: int = 60000) -> dict[str, Any]:
    """Run one C# snippet in the editor and parse the JSON it returns."""
    try:
        r = bridge.post_json(
            "/eval", {"code": code, "ui_thread": True, "timeout_ms": timeout_ms},
            timeout=int(timeout_ms / 1000) + 20)
    except bridge.BridgeDown as exc:
        return {"error": str(exc)}
    if not r.get("ok"):
        return {"error": r.get("error"), "error_type": r.get("error_type")}
    raw = r.get("result")
    if not raw:
        return {"error": "The snippet returned no result", "raw": r}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"result": raw}


@tool(
    group="editor",
    description=(
        "Read the editor's Asset Validation results — the errors that block "
        "publishing. Mod HUB refuses to publish while any Error remains and only "
        "says 'open the project in the editor to see the validation problems'; "
        "this is that list, without leaving the agent."
        " Takes no arguments: editor_validation()"
    ),
)
def editor_validation() -> dict[str, Any]:
    return _run_snippet(editor_api.VALIDATION)


@tool(
    group="editor",
    description=(
        "Build the loaded project from inside the editor (generates the Content "
        "cache and definition sets). Use this instead of build_project for any "
        "mod that depends on Vanilla — the standalone CLI cannot load Vanilla, "
        "the editor can."
        " Takes no arguments: editor_build()"
    ),
)
def editor_build(
    with_blobs: bool | None = True,
    with_dependencies: bool | None = False,
) -> dict[str, Any]:
    code = (editor_api.BUILD
            .replace("WITH_BLOBS", "true" if with_blobs else "false")
            .replace("WITH_DEPS", "true" if with_dependencies else "false"))
    return _run_snippet(code, timeout_ms=600000)


@tool(
    group="editor",
    description="Which project the editor currently has loaded, and its type. Takes no arguments: editor_project()",
)
def editor_project() -> dict[str, Any]:
    return _run_snippet(editor_api.PROJECT_INFO)


@tool(
    group="editor",
    description=(
        "List the editor's live window view-models with their properties. This is "
        "the discovery map for driving the UI: pick a view-model here, then act on "
        "it with editor_eval."
        " Takes no arguments: editor_viewmodels()"
    ),
)
def editor_viewmodels() -> dict[str, Any]:
    return _run_snippet(editor_api.VIEWMODELS)


@tool(
    group="editor",
    description="What is selected / opened / inspected in the editor right now. Takes no arguments: editor_selection()",
)
def editor_selection() -> dict[str, Any]:
    return _run_snippet(editor_api.SELECTION)


@tool(
    group="editor",
    description=(
        "Browse the editor's Project Explorer: which project and folder are shown "
        "and what is listed in them. Use it to see what a project actually "
        "contains before acting on it."
        " Takes no arguments: editor_explorer()"
    ),
)
def editor_explorer() -> dict[str, Any]:
    return _run_snippet(editor_api.EXPLORER)


@tool(
    group="editor",
    description=(
        "List what the Project Explorer can create in the current folder: the "
        "Create Asset and Create Prefab template menus. There are ~330 entries, "
        "so filter with `contains` (e.g. 'Thruster', 'Armor'). Creating a block "
        "from a template is how SE2 expects new blocks to be made — a template "
        "generates all ~14 definitions at once, so this is the menu to consult "
        "before authoring anything by hand."
        " Example: editor_generators(contains='planet')"
    ),
)
def editor_generators(contains: str | None = "") -> dict[str, Any]:
    code = editor_api.GENERATORS.replace(
        "FILTER", '"%s"' % (contains or "").replace('"', '\\"'))
    return _run_snippet(code)


@tool(
    group="editor",
    description=(
        "Create a block (or other asset) from an editor template — the supported "
        "way to make a new SE2 block, because one template generates all of its "
        "definitions at once instead of authoring ~14 files by hand.\n\n"
        "`path` is a menu path from editor_generators, e.g. "
        "'Blocks/Breakable/Ion Thrusters'. It is created in the folder the "
        "Project Explorer currently shows, so select that folder first. "
        "menu='prefab_generators' (default) or 'asset_generators'. "
        "The editor may then prompt for a name in its own window."
        " Example: editor_create_from_template(path='C:/Mods/MyMod/x.prefab')"
    ),
)
def editor_create_from_template(
    path: str, menu: str | None = "prefab_generators"
) -> dict[str, Any]:
    which = {"prefab_generators": "PrefabGenerators",
             "asset_generators": "AssetGenerators"}.get((menu or "").strip().lower())
    if not which:
        return {"error": "menu must be 'prefab_generators' or 'asset_generators'"}
    code = (editor_api.CREATE_FROM_TEMPLATE
            .replace("MENU_PATH", path.replace('"', '\\"'))
            .replace("WHICH_MENU", which))
    return _run_snippet(code, timeout_ms=120000)


@tool(
    group="editor",
    description=(
        "Select an asset in the Project Explorer by name (exact first, then "
        "substring), which also drives the Property Inspector. Set open=true to "
        "additionally open it in the main scene view."
        " Example: editor_open_asset(name='IonThruster500')"
    ),
)
def editor_open_asset(name: str, open: bool | None = False) -> dict[str, Any]:
    safe = name.replace('"', '\\"')
    code = (editor_api.OPEN_ASSET
            .replace("TARGET_NAME", safe)
            .replace("SET_OPEN", "true" if open else "false"))
    return _run_snippet(code)


# --------------------------------------------------------------------------
# Mod HUB
# --------------------------------------------------------------------------

@tool(
    group="modhub",
    description=(
        "Mod HUB status: its settings, the mods directory, and which of Mod HUB / "
        "editor / game are running. Also reports ShowDetailedErrors, which decides "
        "whether Mod HUB shows real publish problems or a one-line message."
        " Takes no arguments: modhub_status()"
    ),
)
def modhub_status() -> dict[str, Any]:
    return modhub.status()


@tool(
    group="modhub",
    description=(
        "List the mod projects in the Mod HUB mods directory, with whether each is "
        "already published to Steam, its mod id, and whether it depends on Vanilla."
        " Takes no arguments: modhub_projects()"
    ),
)
def modhub_projects() -> dict[str, Any]:
    items = modhub.projects()
    return {"mods_directory": str(modhub.mods_dir()), "count": len(items),
            "projects": items}


@tool(
    group="modhub",
    description=(
        "Launch VRAGE3 Mod HUB. Publishing itself happens in its window — Mod HUB "
        "has no publish command line — but everything that blocks a publish can be "
        "checked first with editor_validation."
        " Takes no arguments: launch_modhub()"
    ),
)
def launch_modhub(no_splash: bool | None = True) -> dict[str, Any]:
    return modhub.launch_modhub(bool(no_splash))


@tool(
    group="modhub",
    description=(
        "Launch the editor on a project with the argument set Mod HUB itself uses "
        "(both global project dirs plus the game executable path). Without those "
        "the Vanilla dependency fails to resolve. Then poll editor_status until "
        "the bridge answers."
        " Example: launch_editor(project='MyMod')"
    ),
)
def launch_editor(project: str) -> dict[str, Any]:
    return modhub.launch_editor(project)


# --------------------------------------------------------------------------
# Blender (models and textures)
# --------------------------------------------------------------------------

@tool(
    group="blender",
    description=(
        "Is Blender reachable, and is it set up for SE2 work? Reports the "
        "BlenderMCP connection, whether Keen's official VRAGE Tools add-on is "
        "enabled (without it there is no SE2-correct export), the scene's "
        "geometry and materials, and where the shared material library lives. "
        "Call this before any other blender_* tool."
        " Takes no arguments: blender_status()"
    ),
)
def blender_status() -> dict[str, Any]:
    return blender.status()


@tool(
    group="blender",
    description=(
        "Run Python inside the running Blender and return what it printed. This "
        "is the escape hatch for anything the typed tools do not cover — the "
        "whole bpy API is available.\n\n"
        "Results come back through **stdout**, so end the snippet with print(); "
        "assigning to a variable returns nothing. bpy.ops.* called from here runs "
        "the operator directly and never opens its confirmation popup."
        " Example: blender_python(code='import bpy; print(len(bpy.data.objects))')"
    ),
)
def blender_python(code: str, timeout: float | None = 120) -> dict[str, Any]:
    try:
        return blender.run_python(code, timeout=float(timeout or 120))
    except blender.BlenderDown as exc:
        return {"ok": False, "error": str(exc)}


@tool(
    group="blender",
    description=(
        "Measure the selected meshes against SE2's block rules: bounding size, "
        "triangle and vertex counts, materials, ngons. Pass `subject` as the "
        "block name (e.g. 'MyThruster250') and the size it declares is checked "
        "too — a block's name carries its largest dimension in centimetres, and "
        "a model that overflows it places wrongly in game. For scale: "
        "IonThruster150 is 8,459 verts, IonThruster500 is 17,859."
        " Example: blender_measure(subject='IonThruster500')"
    ),
)
def blender_measure(subject: str | None = "") -> dict[str, Any]:
    try:
        return blender.measure(subject or "")
    except blender.BlenderDown as exc:
        return {"ok": False, "error": str(exc)}


@tool(
    group="blender",
    description=(
        "Export the current mesh through VRAGE Tools into the exact FBX / LOD / "
        "collision layout the content pipeline expects — the supported way to get "
        "geometry out of Blender.\n\n"
        "`models_dir` is the *parent* of the variant folder: pass "
        "'<mod>/Assets/<Block>/Models' and the operator creates 'NonFractured/' "
        "under it holding '<name>.fbx', '<name>_LOD1..3.fbx' and the collision "
        "glTF. variant: NON_FRACTURED | FRACTURED | DEFORMED | NONE. "
        "limit: SELECTED_OBJECTS | ACTIVE_COLLECTION | VISIBLE_OBJECTS — with the "
        "default, an empty selection exports nothing silently. Reports the files "
        "that actually landed on disk."
        " Example: blender_export_model(name='MyBlock', models_dir='C:/Mods/MyMod/Models')"
    ),
)
def blender_export_model(
    name: str,
    models_dir: str,
    variant: str | None = "NON_FRACTURED",
    limit: str | None = "SELECTED_OBJECTS",
    lods: list[int] | str | None = None,
    collisions: bool | None = False,
) -> dict[str, Any]:
    if isinstance(lods, str):
        # "0,1,2" and "[0, 1, 2]" both turn up; neither is worth failing over.
        lods = [int(p) for p in lods.replace("[", " ").replace("]", " ")
                .replace(",", " ").split() if p.strip("-").isdigit()]
    try:
        return blender.export_model(
            name, models_dir,
            variant=(variant or "NON_FRACTURED").upper(),
            limit=(limit or "SELECTED_OBJECTS").upper(),
            lods=lods or [0], collisions=bool(collisions),
        )
    except blender.BlenderDown as exc:
        return {"ok": False, "error": str(exc)}


@tool(
    group="blender",
    description=(
        "Append SE2's shared material library into the Blender scene. Vanilla "
        "blocks carry no per-block LOD0 textures — they reference a shared set "
        "(PaintedMetalColorable, MetalDull, Chrome, the AtlasDecal atlases...), "
        "and only the furthest LOD uses a baked per-block atlas. Assigning these "
        "is how a mod block ends up surfaced like a vanilla one, with no texture "
        "painting at all."
        " Takes no arguments: blender_material_library()"
    ),
)
def blender_material_library() -> dict[str, Any]:
    try:
        return blender.import_material_library()
    except blender.BlenderDown as exc:
        return {"ok": False, "error": str(exc)}


# --------------------------------------------------------------------------
# Playbook
# --------------------------------------------------------------------------

@tool(
    group="knowledge",
    description=(
        "The end-to-end procedure for building a piece of SE2 content, from "
        "Blender model to publishable mod: which tool to call in what order, the "
        "traps that cost hours, and the measured numbers to design against. "
        "Read this before starting new content rather than inferring a workflow "
        "from the tool list.\n\n"
        "topic: 'index' lists what is available; then 'block', 'planet', "
        "'voxel_material', 'armor', 'texture', 'model', 'sound', 'publish', "
        "'troubleshoot'."
        " Example: mod_recipes(topic='index')"
    ),
)
def mod_recipes(topic: str | None = "index") -> dict[str, Any]:
    return recipes.get(topic or "index")


@tool(
    group="knowledge",
    description=(
        "Measured facts about the SDK that are documented nowhere and cannot be "
        "guessed from file names: the exact PNG formats for planet maps, the "
        "cube-face basis and the trap in it, how ore textures chain from PNG to "
        "voxel material, how ColorKeys really work, how a planet is wired, the "
        "cause of the 'dependencies hashes do not match' publish error, and why "
        "an editor that refuses to open is usually a project-dependency problem "
        "rather than a corrupted file.\n\n"
        "Read the relevant topic BEFORE answering a how-does-this-work question. "
        "topic: 'index' lists them; then 'file-format', 'project-dependencies', "
        "'ore-textures', 'planet-structure', 'colorkeys', 'map-formats', "
        "'cube-basis', 'planet-overlay', 'publish-hash', 'mod-project-layout'."
        " Example: explain(topic='rules')"
    ),
)
def explain(topic: str | None = "index") -> dict[str, Any]:
    return knowledge.get(topic or "index")


# --------------------------------------------------------------------------
# Prompts
#
# A tool list is a set of capabilities, not a plan, and a smaller model handed
# forty of them tends to start guessing. These are the three plans that matter,
# written as the opening instruction of a session — clients surface them as
# ready-made commands, which is often the whole interaction on a local setup.
# --------------------------------------------------------------------------

@server.prompt(
    name="se2_start",
    title="Start an SE2 modding session",
    description="Orientation: what this SDK is, and which tool to call first.",
)
def _prompt_start() -> str:
    return (
        "I am working on a Space Engineers 2 mod. Before answering anything:\n"
        "1. Call sdk_info to see the install and whether the index is ready.\n"
        "2. Call explain('index') and mod_recipes('index') and read the topic "
        "list — they hold measured facts and procedures that cannot be guessed "
        "from the files, and getting them wrong costs hours.\n"
        "3. Then ask me what I want to build.\n\n"
        "Throughout: find how vanilla does something with search_content before "
        "authoring anything, and never edit files inside the SDK's GameData — a "
        "mod overrides vanilla content with a partialdef instead."
    )


@server.prompt(
    name="se2_build",
    title="Build a piece of SE2 content",
    description="Walk the measured procedure for a block, planet, ore or armor.",
)
def _prompt_build(kind: str = "block", project: str = "") -> str:
    return (
        f"I want to add a new {kind} to Space Engineers 2"
        + (f", in the mod project at {project}" if project else "")
        + ".\n\n"
        f"Start by calling mod_recipes('{kind}') and following its steps in "
        f"order — it names the exact tool for each one and the traps that are "
        f"invisible until they have already cost an afternoon. Read any "
        f"explain() topic it points at before acting on that step.\n\n"
        "Show me the plan first, then work through it. After every write, run "
        "audit_project; it catches the failures that produce no error message "
        "anywhere, such as a mod that loads and shows nothing."
    )


@server.prompt(
    name="se2_diagnose",
    title="Diagnose a mod that is not working",
    description="Find why a mod fails to load, publish, or show up in game.",
)
def _prompt_diagnose(project: str = "", symptom: str = "") -> str:
    return (
        "A Space Engineers 2 mod is not behaving"
        + (f" — {symptom}" if symptom else "")
        + ".\n\n"
        "Work through this in order and report what each step found:\n"
        f"1. audit_project({project!r}) — structural errors, including the ones "
        "that produce no message anywhere.\n"
        "2. mod_recipes('troubleshoot') — match the symptom to a known cause.\n"
        "3. read_app_log(app='editor') and read_app_log(app='modhub') — the "
        "applications' own account of the failure.\n"
        "4. If it concerns publishing, read explain('publish-hash'); if the "
        "editor refuses to open, read explain('project-dependencies').\n\n"
        "Name the specific file and the specific cause before proposing a fix."
    )


def main() -> None:
    # Starts only when there is no index yet, and never blocks the handshake:
    # a client that waits for the server to answer must not be made to wait for
    # a two-minute first scan of the SDK.
    index.start_background_build()
    server.run("stdio")


if __name__ == "__main__":
    main()
