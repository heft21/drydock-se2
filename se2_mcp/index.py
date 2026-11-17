"""SQLite index over SE2 definition and asset files.

SE2 content is GUID-addressed JSON: every ``.def`` / ``.partialdef`` carries a
``$Type`` and a ``$Value``, and cross-references other assets by bare GUID.
Without an index those references are opaque, so this module builds:

* ``assets``  - one row per definition file
* ``files``   - one row per media asset (model/texture/audio), GUID from its .meta
* ``nested``  - sub-objects that declare their own Guid
* ``refs``    - the GUID reference graph, so reverse lookups are possible
* ``types``   - ``$Type`` histogram

The index is derived data and can always be rebuilt from the SDK.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

from .config import PATHS, DEF_SUFFIXES, extra_roots, normalize_guid

SCHEMA = """
CREATE TABLE IF NOT EXISTS assets (
    guid       TEXT PRIMARY KEY,
    path       TEXT NOT NULL,
    project    TEXT,
    kind       TEXT,          -- def | partialdef
    type       TEXT,          -- $Type of the root object
    def_type   TEXT,          -- partialdef: DefinitionType it produces
    base_guid  TEXT,          -- partialdef: BaseDefinition it diffs against
    diff_kind  TEXT,          -- partialdef: PartialDefinitionKind
    stem       TEXT,          -- file name without suffix
    subject    TEXT,          -- leading token of stem, e.g. "Battery50"
    name       TEXT           -- explicit Name/DisplayName/Id field, if any
);
CREATE INDEX IF NOT EXISTS ix_assets_subject ON assets(subject);
CREATE INDEX IF NOT EXISTS ix_assets_type    ON assets(type);
CREATE INDEX IF NOT EXISTS ix_assets_base    ON assets(base_guid);
CREATE INDEX IF NOT EXISTS ix_assets_stem    ON assets(stem);

-- Non-definition assets (models, textures, audio, ...). Their GUID lives in a
-- ".meta" sidecar, and definitions reference them by that GUID, so without this
-- table every Model/Texture/Icon reference is unresolvable.
CREATE TABLE IF NOT EXISTS files (
    guid      TEXT PRIMARY KEY,
    path      TEXT NOT NULL,
    project   TEXT,
    ext       TEXT,           -- .fbx, .png, .dds, ...
    processor TEXT,           -- content-pipeline processor id, e.g. P_PNG
    stem      TEXT
);
CREATE INDEX IF NOT EXISTS ix_files_stem ON files(stem);
CREATE INDEX IF NOT EXISTS ix_files_ext  ON files(ext);

-- Sub-objects that carry their own Guid and are referenceable, but are not
-- files in their own right. Kept apart from `assets` so a nested object can
-- never shadow a real definition with the same GUID.
CREATE TABLE IF NOT EXISTS nested (
    guid  TEXT NOT NULL,
    owner TEXT NOT NULL,
    path  TEXT NOT NULL,
    type  TEXT,
    field TEXT
);
CREATE INDEX IF NOT EXISTS ix_nested_guid  ON nested(guid);
CREATE INDEX IF NOT EXISTS ix_nested_owner ON nested(owner);

CREATE TABLE IF NOT EXISTS refs (
    src   TEXT NOT NULL,
    dst   TEXT NOT NULL,
    field TEXT
);
CREATE INDEX IF NOT EXISTS ix_refs_dst ON refs(dst);
CREATE INDEX IF NOT EXISTS ix_refs_src ON refs(src);

CREATE TABLE IF NOT EXISTS types (
    type TEXT PRIMARY KEY,
    n    INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT
);
"""

# Fields that carry a human-facing identifier, checked in priority order.
NAME_FIELDS = ("Name", "DisplayName", "Id", "SubtypeId", "SubtypeName")

# Structural keys, not references.
SKIP_KEYS = {"$Bundles", "$Type"}

# ``.meta`` sidecars are numerous (~50k) and only two fields matter, so they are
# scraped with a regex instead of a full JSON parse.
_ASSET_ID_RE = re.compile(r'"AssetID"\s*:\s*"([0-9a-fA-F-]{36})"')
_PROCESSOR_RE = re.compile(r'"Identifier"\s*:\s*"([^"]+)"')


@dataclass
class IndexStats:
    definitions: int = 0
    media: int = 0
    nested: int = 0
    refs: int = 0
    errors: int = 0
    seconds: float = 0.0
    error_samples: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        d = {
            "definitions": self.definitions,
            "media_assets": self.media,
            "nested_objects": self.nested,
            "reference_edges": self.refs,
            "parse_errors": self.errors,
            "seconds": round(self.seconds, 1),
        }
        if self.error_samples:
            d["error_samples"] = self.error_samples[:5]
        return d


def connect(read_only: bool = False) -> sqlite3.Connection:
    path = PATHS.db_path
    if read_only and not path.exists():
        raise FileNotFoundError("Index not built yet. Run the build_index tool first.")
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def roots() -> list[tuple[str, Path]]:
    """(project name, directory) pairs that should be indexed."""
    return [
        (d.name, d)
        for d in (PATHS.vanilla, PATHS.engine, *extra_roots())
        if d.is_dir()
    ]


def _scan_dirs(root: Path) -> list[Path]:
    """Source directories inside a project.

    ``Content/`` is the compiled output of ``Assets/`` and holds a byte-identical
    copy of every definition. Indexing it would double the work and make every
    search return each hit twice, so it is skipped.
    """
    dirs = [p for p in root.iterdir() if p.is_dir() and p.name != "Content"]
    return dirs or [root]


def _walk_guids(node: Any, prefix: str = "") -> Iterator[tuple[str, str]]:
    """Yield (guid, dotted-field-path) for every GUID string in the tree."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in SKIP_KEYS:
                continue
            yield from _walk_guids(v, f"{prefix}.{k}" if prefix else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            # Positions are noise in long arrays; keep the parent field name.
            yield from _walk_guids(v, f"{prefix}[{i}]" if len(node) < 32 else prefix)
    elif isinstance(node, str):
        g = normalize_guid(node)
        if g:
            yield g, prefix


def _walk_nested(node: Any, path: str = "") -> Iterator[tuple[str, str, str]]:
    """Yield (guid, $Type, field-path) for nested objects that declare a Guid."""
    if isinstance(node, dict):
        t = node.get("$Type")
        raw = node.get("Guid")
        g = normalize_guid(raw) if isinstance(raw, str) else None
        if t and g and path:
            yield g, t, path
        for k, v in node.items():
            if k in SKIP_KEYS:
                continue
            yield from _walk_nested(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for v in node:
            yield from _walk_nested(v, path)


def _own_guid(kind: str, value: dict) -> str | None:
    """The GUID identifying this file, matching the AssetID in its .meta.

    An *Override* partialdef is the exception: it changes an existing
    definition rather than declaring a new one, so it carries no Guid anywhere
    in its body. Its identity lives only in the sidecar — see `_meta_asset_id`.
    """
    if kind == "partialdef":
        man = value.get("Manipulator")
        if isinstance(man, dict) and isinstance(man.get("Guid"), str):
            g = normalize_guid(man["Guid"])
            if g:
                return g
    raw = value.get("Guid")
    return normalize_guid(raw) if isinstance(raw, str) else None


def _meta_asset_id(def_path: Path) -> str | None:
    """The AssetID from a definition's sidecar, for files that declare none."""
    meta = def_path.with_name(def_path.name + ".meta")
    try:
        head = meta.read_text(encoding="utf-8-sig", errors="replace")[:2048]
    except OSError:
        return None
    m = _ASSET_ID_RE.search(head)
    return normalize_guid(m.group(1)) if m else None


def _explicit_name(value: dict) -> str | None:
    for f in NAME_FIELDS:
        v = value.get(f)
        if isinstance(v, str) and v and not normalize_guid(v):
            return v
    return None


def build() -> IndexStats:
    """(Re)build the index from scratch. Safe to call at any time."""
    started = time.time()
    stats = IndexStats()

    db_path = PATHS.db_path
    # Per-process, so two servers sharing a cache directory cannot write over
    # each other's half-built database.
    tmp_path = db_path.with_suffix(f".building-{os.getpid()}")
    tmp_path.unlink(missing_ok=True)

    conn = sqlite3.connect(tmp_path)
    conn.executescript(SCHEMA)
    # Bulk write to a throwaway file: durability is irrelevant, speed is not.
    conn.execute("PRAGMA journal_mode=OFF")
    conn.execute("PRAGMA synchronous=OFF")

    asset_rows: list[tuple] = []
    file_rows: list[tuple] = []
    nested_rows: list[tuple] = []
    ref_rows: list[tuple] = []
    type_counts: dict[str, int] = {}

    def flush() -> None:
        if asset_rows:
            conn.executemany(
                "INSERT OR REPLACE INTO assets "
                "(guid,path,project,kind,type,def_type,base_guid,diff_kind,stem,subject,name)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                asset_rows,
            )
            asset_rows.clear()
        if file_rows:
            conn.executemany(
                "INSERT OR REPLACE INTO files (guid,path,project,ext,processor,stem)"
                " VALUES (?,?,?,?,?,?)",
                file_rows,
            )
            file_rows.clear()
        if nested_rows:
            conn.executemany(
                "INSERT INTO nested (guid,owner,path,type,field) VALUES (?,?,?,?,?)",
                nested_rows,
            )
            nested_rows.clear()
        if ref_rows:
            conn.executemany("INSERT INTO refs (src,dst,field) VALUES (?,?,?)", ref_rows)
            ref_rows.clear()

    def note_error(path: Path, exc: Exception) -> None:
        stats.errors += 1
        if len(stats.error_samples) < 20:
            stats.error_samples.append(f"{path.name}: {exc}")

    for project, root in roots():
        base = root.parent
        for scan in _scan_dirs(root):
            for path in scan.rglob("*"):
                suffix = path.suffix

                if suffix == ".meta":
                    inner = Path(path.name[: -len(".meta")])
                    # A definition's sidecar adds nothing we do not already have.
                    if inner.suffix in DEF_SUFFIXES or not path.is_file():
                        continue
                    try:
                        head = path.read_text(encoding="utf-8-sig", errors="replace")[:2048]
                    except OSError as exc:
                        note_error(path, exc)
                        continue
                    m = _ASSET_ID_RE.search(head)
                    g = normalize_guid(m.group(1)) if m else None
                    if not g:
                        continue
                    proc = _PROCESSOR_RE.search(head)
                    file_rows.append((
                        g,
                        str(path.parent.relative_to(base) / inner.name),
                        project,
                        inner.suffix.lower(),
                        proc.group(1) if proc else None,
                        inner.stem,
                    ))
                    stats.media += 1

                elif suffix in DEF_SUFFIXES and path.is_file():
                    try:
                        with open(path, "r", encoding="utf-8-sig") as fh:
                            doc = json.load(fh)
                    except Exception as exc:  # one bad file must not abort the run
                        note_error(path, exc)
                        continue
                    if not isinstance(doc, dict):
                        continue
                    value = doc.get("$Value")
                    if not isinstance(value, dict):
                        continue

                    kind = suffix.lstrip(".")
                    guid = _own_guid(kind, value)
                    if not guid:
                        # Override partialdefs declare no Guid; skipping them
                        # would hide exactly the files a mod uses to change the
                        # base game. Fall back to the sidecar's AssetID.
                        guid = _meta_asset_id(path)
                    if not guid:
                        continue

                    root_type = doc.get("$Type") or ""
                    rel = str(path.relative_to(base))
                    stem = path.name[: -len(suffix)]

                    base_guid = diff_kind = def_type = None
                    if kind == "partialdef":
                        bd = value.get("BaseDefinition")
                        base_guid = normalize_guid(bd) if isinstance(bd, str) else None
                        diff_kind = value.get("PartialDefinitionKind")
                        def_type = value.get("DefinitionType")

                    asset_rows.append((
                        guid, rel, project, kind, root_type, def_type, base_guid,
                        diff_kind, stem, stem.split("_", 1)[0], _explicit_name(value),
                    ))
                    stats.definitions += 1
                    type_counts[root_type] = type_counts.get(root_type, 0) + 1

                    for ng, ntype, npath in _walk_nested(value):
                        if ng != guid:
                            nested_rows.append((ng, guid, rel, ntype, npath))
                            stats.nested += 1

                    # Deduped per file so delta-encoded key arrays do not
                    # dominate the table.
                    seen: dict[str, str] = {}
                    for dst, fld in _walk_guids(value):
                        if dst != guid and dst not in seen:
                            seen[dst] = fld
                    ref_rows.extend((guid, dst, fld) for dst, fld in seen.items())
                    stats.refs += len(seen)

                else:
                    continue

                if (len(asset_rows) >= 4000 or len(file_rows) >= 4000
                        or len(ref_rows) >= 8000 or len(nested_rows) >= 8000):
                    flush()

    flush()
    conn.executemany(
        "INSERT OR REPLACE INTO types (type,n) VALUES (?,?)", sorted(type_counts.items())
    )
    stats.seconds = time.time() - started
    conn.executemany(
        "INSERT OR REPLACE INTO meta (key,value) VALUES (?,?)",
        [
            ("built_at", str(int(time.time()))),
            ("sdk", str(PATHS.sdk)),
            ("stats", json.dumps(stats.as_dict())),
            ("roots", json.dumps([str(p) for _, p in roots()])),
        ],
    )
    conn.commit()
    conn.close()

    _swap_in(tmp_path, db_path)
    return stats


SWAP_RETRY_FOR = 10.0
SWAP_RETRY_EVERY = 0.25


def _swap_in(tmp_path: Path, db_path: Path) -> None:
    """Put the new database in place.

    On Windows the replace fails while a reader still has the old file open, so
    it is retried for a while instead of unlinking first (which fails the same
    way and would leave no index at all).
    """
    deadline = time.monotonic() + SWAP_RETRY_FOR
    while True:
        try:
            os.replace(tmp_path, db_path)
            return
        except PermissionError:
            if time.monotonic() >= deadline:
                tmp_path.unlink(missing_ok=True)
                raise
            time.sleep(SWAP_RETRY_EVERY)


def _meta_rows() -> dict[str, str]:
    conn = connect(read_only=True)
    try:
        return {r["key"]: r["value"] for r in conn.execute("SELECT key,value FROM meta")}
    finally:
        conn.close()


def index_status() -> dict[str, Any]:
    if not PATHS.db_path.exists():
        return {"built": False, "hint": "Call build_index to create it."}
    try:
        rows = _meta_rows()
    except (sqlite3.DatabaseError, FileNotFoundError) as exc:
        return {"built": False, "error": str(exc)}
    out: dict[str, Any] = {"built": True, "db": str(PATHS.db_path)}
    if "built_at" in rows:
        out["built_at"] = time.strftime(
            "%Y-%m-%d %H:%M", time.localtime(int(rows["built_at"]))
        )
    for k in ("stats", "roots"):
        if k in rows:
            out[k] = json.loads(rows[k])
    refreshing = building()
    if refreshing:
        out["refreshing"] = True
    stale = stale_reason(rows)
    if stale:
        out["stale"] = stale
        if refreshing:
            out["hint"] = ("Being refreshed in the background; lookups use the "
                           "previous index until it is done.")
        else:
            out["hint"] = "Call build_index to pick the change up."
            if _refresh_failed_for == stale:
                out["refresh_error"] = _build_error
    return out


def stale_reason(rows: dict[str, str] | None = None) -> str | None:
    """Why the stored index no longer describes this machine, if it does not.

    A game update changes file contents and cannot be detected cheaply, but the
    two changes that silently produce wrong answers — a different SDK install,
    or a mod project added or removed — are both visible from the stamp written
    at build time.
    """
    try:
        rows = _meta_rows() if rows is None else rows
    except (sqlite3.DatabaseError, FileNotFoundError):
        return None
    if rows.get("sdk") and rows["sdk"] != str(PATHS.sdk):
        return f"indexed from {rows['sdk']}, now using {PATHS.sdk}"
    try:
        indexed = set(json.loads(rows.get("roots") or "[]"))
    except json.JSONDecodeError:
        return None
    current = {str(p) for _, p in roots()}
    added = current - indexed
    gone = indexed - current
    parts = []
    if added:
        parts.append(f"{len(added)} project(s) not indexed: "
                     + ", ".join(sorted(Path(p).name for p in added)[:5]))
    if gone:
        parts.append(f"{len(gone)} indexed project(s) no longer present: "
                     + ", ".join(sorted(Path(p).name for p in gone)[:5]))
    return "; ".join(parts) or None


class IndexBuilding(RuntimeError):
    """The index is being built right now; the same call will work shortly.

    ``retryable`` is what the tool wrapper looks for: this is a wait, not a
    failure, and reporting it as an error would send a model looking for
    something to fix.
    """

    retryable = True


_build_lock = threading.Lock()
_build_thread: threading.Thread | None = None
_build_started: float = 0.0
_build_error: str | None = None
_stale_checked: float = 0.0
_refresh_failed_for: str | None = None
_refresh_reason: str | None = None
STALE_CHECK_EVERY = 30.0


def building() -> bool:
    """Whether a background build is running right now."""
    return _build_thread is not None and _build_thread.is_alive()


def clear_refresh_failure() -> None:
    """Forget a failed automatic refresh, e.g. after a manual rebuild worked."""
    global _refresh_failed_for
    _refresh_failed_for = None


def refresh_if_stale(force_check: bool = False) -> str | None:
    """Start a background rebuild when the stored index no longer matches this machine.
    Returns the reason when a rebuild is running because of it, else None."""
    global _build_thread, _build_started, _build_error, _refresh_reason, _stale_checked
    try:
        if not PATHS.db_path.exists():
            return None                          # start_background_build's case
        if building():
            return _refresh_reason
        now = time.monotonic()
        if not force_check and now - _stale_checked < STALE_CHECK_EVERY:
            return None
        _stale_checked = now
        if PATHS.check():
            return None
        reason = stale_reason()
        if not reason or reason == _refresh_failed_for:
            return None
        with _build_lock:
            if building():
                return _refresh_reason
            _refresh_reason = reason
            _build_started = time.time()
            _build_error = None
            print(f"se2-mcp: index is out of date ({reason}), "
                  f"refreshing it in the background.", file=sys.stderr)
            _build_thread = threading.Thread(
                target=_run_build, name="se2-index-refresh", daemon=True)
            _build_thread.start()
            return reason
    except Exception:                            # a lookup must never fail on this
        return None


def _run_build() -> None:
    """The background build. Field documentation rides along; it costs ~2s."""
    global _build_error, _refresh_reason, _refresh_failed_for
    try:
        stats = build()
        from . import docs
        if not docs.is_built():
            docs.build()
        # stdout is the MCP transport, so progress goes to stderr.
        print(f"se2-mcp: index ready, {stats.definitions} definitions "
              f"in {stats.seconds:.0f}s.", file=sys.stderr)
    except Exception as exc:                     # a dead thread must say why
        _build_error = f"{type(exc).__name__}: {exc}"
        print(f"se2-mcp: index build failed: {_build_error}", file=sys.stderr)
        if _refresh_reason:
            _refresh_failed_for = _refresh_reason
    finally:
        _refresh_reason = None


def start_background_build() -> bool:
    """Begin building the index without blocking, if it is missing.

    Called at server startup. Building takes a couple of minutes the first time
    a machine reads the SDK — long enough that doing it inside the first tool
    call would hit the client's call timeout, and long enough that doing it
    before the server answers would look like a server that failed to start.
    So it happens alongside, and tools that need it wait a bounded time.
    """
    global _build_thread, _build_started
    if PATHS.check():
        return False
    if PATHS.db_path.exists():
        return bool(refresh_if_stale(force_check=True))
    with _build_lock:
        if _build_thread is not None and _build_thread.is_alive():
            return True
        if PATHS.db_path.exists():
            return False
        print("se2-mcp: no index yet, building it in the background "
              "(a couple of minutes on first run).", file=sys.stderr)
        _build_started = time.time()
        _build_thread = threading.Thread(
            target=_run_build, name="se2-index-build", daemon=True)
        _build_thread.start()
        return True


def ensure(wait: float = 25.0) -> None:
    """Make sure the index exists, waiting up to `wait` seconds for a build.

    A model that skips the setup step is the normal case, not the exception, so
    the index is never simply missing: it is either there, or on its way and
    the caller is told to try again.
    """
    if PATHS.db_path.exists():
        refresh_if_stale()
        return
    problems = PATHS.check()
    if problems:
        raise FileNotFoundError("; ".join(problems))

    start_background_build()
    thread = _build_thread
    if thread is not None:
        thread.join(timeout=max(0.0, wait))
    if PATHS.db_path.exists():
        return
    if _build_error:
        raise RuntimeError(f"Index build failed: {_build_error}")
    elapsed = int(time.time() - _build_started) if _build_started else 0
    raise IndexBuilding(
        f"The definition index is still building ({elapsed}s so far; it scans "
        f"~50,000 SDK files and takes a couple of minutes the first time). "
        f"Nothing is wrong and nothing needs doing — make the same call again "
        f"in a minute."
    )
