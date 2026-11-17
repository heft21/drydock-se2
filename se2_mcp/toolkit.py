"""Tool registration: which tools exist, and what happens when one goes wrong.

Two problems this solves, both of them about the model on the other end rather
than about SE2.

**Small models drown in a long tool list.** The full set is a fine surface for a
large model and a poor one for a quantised model running locally: measured over
the wire, ``tools/list`` is ~12,000 tokens of schema before any work starts, and
accuracy falls off well before that. So the set is selectable —
``SE2_MCP_PROFILE=core`` keeps reading, authoring and checking; ``mini`` cuts to
the smallest surface that can still finish a mod; ``full`` adds the bridges to
the live editor, Mod HUB and Blender.

Profile sizes are derived from the sets below rather than written down, because
a hand-counted number in a docstring is wrong the first time a tool is added.

**Models get argument shapes wrong in two predictable ways.** They send ``null``
for optional arguments, and they send objects and arrays as JSON *text*. Both
are repaired in ``guard`` before the function runs, so ``{"kind": null}`` and
``{"value": "{\\"Foo\\": 1}"}`` behave like the call the model meant to make
instead of failing validation.

And nothing raises. An exception out of a tool reaches the model as a transport
error with a traceback, which is unrecoverable noise; here it becomes a normal
result carrying the reason and the next thing to try.
"""

from __future__ import annotations

import functools
import inspect
import json
import os
import sqlite3
from typing import Any, Callable

# Groups exist so a whole capability can be switched off — a machine with no
# Blender has no use for the Blender tools cluttering the list.
GROUPS = ("knowledge", "lookup", "authoring", "checking", "logs",
          "editor", "modhub", "blender")

# The read -> understand -> write -> check loop, which is all that most sessions
# need. Deliberately small: everything here earns its place in the budget, and
# the live-application bridges — the half of the surface that needs another
# program running — are exactly what is left out.
CORE_TOOLS = frozenset({
    # The session bookends. work_on is the first call of any session and
    # finish_and_publish is what strips the bridge before publishing, so a
    # small model running the core profile must still have both.
    "work_on", "finish_and_publish",
    "sdk_info", "self_test", "build_index",
    "explain", "mod_recipes",
    "search_content", "resolve_guid", "read_definition", "find_references",
    "describe_type", "list_types", "subject_files",
    "scaffold_mod", "write_definition", "new_guids",
    "audit_project", "read_app_log",
})

# The smallest surface that can still carry a mod from question to finished
# folder: understand, find, read, scaffold, write, check. Everything here is
# also in CORE_TOOLS. For a heavily quantised model even the core list is a lot
# of schema to hold, and each tool it cannot use is one more thing to guess with.
MINI_TOOLS = frozenset({
    "work_on",
    "explain",
    "search_content", "read_definition", "describe_type",
    "scaffold_mod", "write_definition",
    "audit_project",
})

# None means "no restriction". Sizes are derived, never written down.
PROFILES: dict[str, frozenset[str] | None] = {
    "mini": MINI_TOOLS,
    "core": CORE_TOOLS,
    "full": None,
}

PROFILE_NOTES = {
    "mini": "understand, find, read, scaffold, write, check — and nothing else",
    "core": "reading, authoring and checking content",
    "full": "everything, including the live editor, Mod HUB and Blender bridges",
}

# A tool that is in mini but not core would be unreachable at core, which is the
# kind of thing that only shows up as a model mysteriously losing a capability.
assert MINI_TOOLS <= CORE_TOOLS, sorted(MINI_TOOLS - CORE_TOOLS)


# Every tool the server module declares, enabled or not. Filled in by the
# registrar as the decorators run, so "18 of 50" reports a counted total rather
# than a number someone remembered to update.
_declared: set[str] = set()


def _declared_total() -> int:
    return len(_declared)


def describe_profiles() -> dict[str, str]:
    """Profile name -> human description, with the measured tool count."""
    return {
        name: (f"{len(tools) if tools is not None else 'all'} tools — "
               f"{PROFILE_NOTES.get(name, '')}")
        for name, tools in PROFILES.items()
    }


def profile() -> str:
    raw = (os.environ.get("SE2_MCP_PROFILE") or "full").strip().lower()
    return raw if raw in PROFILES else "full"


def _env_list(name: str) -> set[str]:
    raw = os.environ.get(name, "")
    return {p.strip().lower() for p in raw.replace(";", ",").split(",") if p.strip()}


def disabled_groups() -> set[str]:
    return _env_list("SE2_MCP_DISABLE") & set(GROUPS)


def enabled(name: str, group: str) -> bool:
    """Whether a tool should be registered in this process."""
    only = _env_list("SE2_MCP_TOOLS")
    if only:                                   # an explicit list wins outright
        return name.lower() in only
    if group in disabled_groups():
        return False
    allowed = PROFILES[profile()]
    return allowed is None or name in allowed


def selection_note() -> str | None:
    """One line describing a non-default selection, for sdk_info to report."""
    only = _env_list("SE2_MCP_TOOLS")
    if only:
        return f"SE2_MCP_TOOLS limits this server to: {', '.join(sorted(only))}"
    bits = []
    current = profile()
    if PROFILES[current] is not None:
        bits.append(
            f"SE2_MCP_PROFILE={current} — {len(PROFILES[current])} of "
            f"{_declared_total()} tools are exposed "
            f"({PROFILE_NOTES.get(current, '')}). The rest exist but are "
            f"switched off; set SE2_MCP_PROFILE=full to get them."
        )
    off = disabled_groups()
    if off:
        bits.append(f"SE2_MCP_DISABLE switched off: {', '.join(sorted(off))}.")
    return " ".join(bits) or None


# ---------------------------------------------------------------------------
# Failure containment
# ---------------------------------------------------------------------------

# What to try next, per exception type. A model that gets "no such file" and
# nothing else tends to retry the same call; a model that is told which tool
# fixes it usually goes and calls that tool.
_HINTS: dict[type, str] = {
    FileNotFoundError:
        "The path does not exist. Check it with sdk_info (for the SDK) or "
        "modhub_projects (for your own mod projects).",
    PermissionError:
        "Windows is holding the file. Close the editor or Mod HUB and retry.",
    sqlite3.DatabaseError:
        "The search index is damaged. Call build_index to rebuild it.",
    UnicodeDecodeError:
        "The file is not UTF-8 text. Definition files are JSON; a binary asset "
        "has to be read through its .meta sidecar instead.",
    TimeoutError:
        "The operation did not finish in time. The editor may be busy loading a "
        "project; check editor_status.",
}


# Windows localises socket errors, so on a Turkish install "connection refused"
# arrives as "Hedef makine etkin olarak reddettiginden baglanti kurulamadi". A
# model reading that has to translate an OS message before it can act on it, so
# the numeric code — which is stable everywhere — is turned back into English.
_SOCKET_CODES = {
    10061: "connection refused, nothing is listening on that port",
    10060: "connection timed out",
    10013: "permission denied by a firewall or security policy",
    10048: "the port is already in use by another process",
    11001: "host not found",
}


def describe_os_error(exc: BaseException) -> str:
    """A language-neutral description of a failed connection or file access."""
    cause: BaseException = exc
    for _ in range(4):                    # URLError wraps the real OSError
        inner = getattr(cause, "reason", None)
        if isinstance(inner, BaseException):
            cause = inner
        else:
            break
    code = getattr(cause, "winerror", None) or getattr(cause, "errno", None)
    if code in _SOCKET_CODES:
        return f"{_SOCKET_CODES[code]} (error {code})"
    if code:
        return f"{type(cause).__name__} {code}"
    return type(cause).__name__


def _hint_for(exc: Exception) -> str | None:
    for kind, hint in _HINTS.items():
        if isinstance(exc, kind):
            return hint
    return None


def _fail(tool_name: str, exc: Exception) -> dict[str, Any]:
    # An exception marked `retryable` describes a wait, not a fault. Reporting
    # one as an error sends a model hunting for something to fix, and small
    # models tend to "fix" it by inventing a different tool call.
    if getattr(exc, "retryable", False):
        return {"status": "not_ready", "retry": True, "detail": str(exc),
                "tool": tool_name}
    out: dict[str, Any] = {
        "error": f"{type(exc).__name__}: {exc}",
        "tool": tool_name,
    }
    hint = _hint_for(exc)
    if hint:
        out["hint"] = hint
    return out


def _declares_json(annotation: Any) -> bool:
    """Does this parameter declare an object or an array?

    ``from __future__ import annotations`` leaves annotations as strings, so
    both the string and the real generic alias have to be recognised.
    """
    if isinstance(annotation, str):
        text = annotation
    else:
        text = getattr(annotation, "__name__", None) or str(annotation)
    return text.lstrip("'\"").startswith(("dict", "list"))


def guard(fn: Callable[..., Any]) -> Callable[..., Any]:
    """Wrap a tool so it always returns a result, never raises.

    Also repairs the two argument shapes models get wrong:

    *Optional arguments sent as ``null``.* Every optional parameter is declared
    nullable, and the declared default is restored here — so ``{"kind": null}``
    behaves like an argument that was never passed.

    *Objects and arrays sent as JSON text.* A smaller model asked for an object
    will often send ``"{\\"Foo\\": 1}"`` instead of ``{"Foo": 1}``; some agent
    runtimes stringify nested arguments on the way out too. Where the parameter
    declares dict or list and a string arrives, it is parsed. A model that sends
    the object properly is unaffected, and text that will not parse is left
    alone so the tool can report the real problem.
    """
    signature = inspect.signature(fn)
    defaults = {
        name: param.default
        for name, param in signature.parameters.items()
        if param.default is not inspect.Parameter.empty and param.default is not None
    }
    json_params = {
        name for name, param in signature.parameters.items()
        if _declares_json(param.annotation)
    }

    @functools.wraps(fn)
    def inner(**kwargs: Any) -> Any:
        for key, value in list(kwargs.items()):
            if value is None and key in defaults:
                kwargs[key] = defaults[key]
            elif key in json_params and isinstance(value, str):
                try:
                    kwargs[key] = json.loads(value)
                except ValueError:
                    pass          # let the tool explain what was wrong with it
        try:
            return fn(**kwargs)
        except Exception as exc:                 # a tool must not kill the call
            return _fail(fn.__name__, exc)

    return inner


def registrar(server: Any) -> Callable[..., Callable]:
    """Build the decorator the server module uses to declare a tool."""

    def tool(group: str, description: str, name: str | None = None):
        if group not in GROUPS:
            raise ValueError(f"Unknown tool group {group!r}")

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            tool_name = name or fn.__name__
            _declared.add(tool_name)
            if enabled(tool_name, group):
                server.tool(name=tool_name, description=description)(guard(fn))
            return fn

        return decorator

    return tool
