# Drydock — an MCP server for Space Engineers 2 modding

*by Heft* · [github.com/heft21/drydock-se2](https://github.com/heft21/drydock-se2)

> *Built from the ground up. Borrowed from no one, owed to no one.*

Drydock is an MCP server for making Space Engineers 2 mods with an AI model at your side.
Any MCP client can use it. It is a community tool, not made or endorsed by Keen Software House.

## What it is underneath

Knowledge, lookup, careful editing and live control for the **Space Engineers 2
Mod SDK**. It never writes to the SDK itself — the shipped tree is reference
material, and a mod overrides it with a partialdef rather than editing it.

Built to work with any model — Claude, DeepSeek, a 7B running on your own
machine — so the knowledge that is normally only in someone's head is in the
server's instructions instead.

## Why it exists

The SDK is ~124,000 files, and **everything references everything else by bare
GUID with no names attached**. A folder listing tells you almost nothing, and
most of what matters — how ore textures chain together, what a ColorKey is, which
way the cube faces point — is documented nowhere.

This server indexes the definition files once and answers questions against that
index, with the undocumented parts written up as topics a model can read before
answering. It also drives the editor, Mod HUB and Blender directly, so a task can
go from "find how vanilla does this" to "see it on screen" without leaving the
tool surface.

## Setup

Install [Python](https://www.python.org/downloads/) 3.11 or newer, then:

```bash
pip install -r requirements.txt
python -m se2_mcp --selftest
```

Or install it as a package, which also gives you the `se2-mcp` command:

```bash
pip install -e .
```

`--selftest` is the whole install check: it finds the SDK, builds the index,
reads a real definition, then scaffolds a mod in a temporary folder, writes a
definition into it and audits the result. Seven checks; if they pass, the server
works.

Nothing needs configuring. The Mod SDK is found by asking Steam where its
libraries are, your own mod projects come from Mod HUB's own settings file, and
the search index builds itself. Override any of that only if detection is wrong:

```env
SE2_MODSDK=C:\Program Files (x86)\Steam\steamapps\common\Space Engineers 2 - Mod SDK
SE2_MCP_MOD_ROOTS=C:\Users\<you>\Documents\SpaceEngineers2\Mods
```

The index lives in `%LOCALAPPDATA%/se2-mcp/`, not in the repo — 19,979
definitions, 34,267 media assets and 203,800 reference edges, measured on this
install (SDK 4.0.0.3169, vanilla plus the local mod projects). It builds in a background thread at startup when it is missing, which
matters because the first build on a machine reads ~50,000 files off disk and
takes **a couple of minutes**; only rebuilds, with those files in the OS cache,
take the ~15 seconds it is usually quoted at. Blocking the handshake for that
long looks like a server that failed to start, and blocking the first tool call
hits the client's call timeout — so instead the server answers immediately, and
a lookup made too early comes back with `status: "not_ready", retry: true`
rather than hanging.

### As an MCP server

Copy `.mcp.example.json` to `.mcp.json` (which git ignores, since it holds
your own paths) and fill in the two paths, or put the block into another
project's config:

```json
{
  "mcpServers": {
    "se2-modsdk": {
      "command": "C:\\path\\to\\python.exe",
      "args": ["-m", "se2_mcp"],
      "cwd": "C:\\path\\to\\drydock-se2",
      "env": {
        "PYTHONPATH": "C:\\path\\to\\drydock-se2"
      }
    }
  }
}
```

Two things that are not optional, both learned by watching the server fail to
start:

- **`PYTHONPATH` must be set**, because `cwd` is not reliably applied by MCP
  clients. Without it `-m se2_mcp` runs in whatever directory the client happens
  to be in and dies with `No module named se2_mcp`, which surfaces only as a
  disconnected server.
- **Use an absolute interpreter path.** A bare `python` depends on whatever PATH
  the client inherits, which is not the shell's.

The same reasoning applies to any relative path in `args`: spell them out in
full rather than trusting `cwd`.

## Running against a local model

Everything here works the same whether the model is large or small, with one
setting worth changing. The default surface is the whole thing, and on a small
model accuracy on tool choice falls off long before it runs out of room:

```env
SE2_MCP_PROFILE=core
```

Measured over the wire, as a client actually receives it:

| profile | tools | `tools/list` |
|---|---:|---:|
| `full` (default) | 50 | ~9,200 tokens |
| `core` | 19 | ~4,100 tokens |
| `mini` | 8 | ~2,100 tokens |

(Counted as the JSON a client receives, at four characters per token.)

`core` drops the half of the surface that needs another program running — the
editor bridge, Mod HUB and Blender. `mini` goes further, to the smallest set
that can still take a mod from question to finished folder: `work_on`,
`explain`, `search_content`, `read_definition`, `describe_type`,
`scaffold_mod`, `write_definition`, `audit_project`. Below that a model cannot check its own
work, which costs more than the tokens it saves.

Start at `core`. Drop to `mini` only if the model is picking wrong tools —
fewer tools means more of the job has to come out of the model instead.

| variable | effect |
|---|---|
| `SE2_MCP_PROFILE=core` \| `mini` \| `full` | pick a surface; `full` is the default |
| `SE2_MCP_DISABLE=blender,editor` | drop whole groups (`knowledge`, `lookup`, `authoring`, `checking`, `logs`, `editor`, `modhub`, `blender`) |
| `SE2_MCP_TOOLS=sdk_info,explain,search_content` | an explicit list, overriding both |

Four things are handled server-side rather than being asked of the model:

- **`null` is accepted for every optional argument.** Models emit
  `{"kind": null}` constantly; it now behaves as if the argument were omitted
  instead of failing schema validation.
- **Objects may arrive as JSON text.** Asked for an object, a smaller model
  often sends `"{\"Foo\": 1}"` instead of `{"Foo": 1}`, and some agent runtimes
  stringify nested arguments on the way out. Where a parameter declares an
  object or an array, text that parses is parsed. Text that does not parse is
  passed through untouched, so the tool reports the real problem rather than a
  schema error.
- **No tool raises.** An unexpected failure comes back as a normal result
  carrying the reason and what to try next, which a model can act on — a
  transport-level traceback is unrecoverable. A wait is reported as a wait
  (`status: "not_ready"`), not as an error, because a model told something
  failed goes looking for something to fix.
- **Queries are matched word by word.** SE2 file names are PascalCase with no
  separators, so `search_content('ion thruster 500')` used to find nothing.
  Every word now has to appear somewhere in the row, and a query that matches
  nothing is retried on its most specific word.

Three prompts (`se2_start`, `se2_build`, `se2_diagnose`) carry the plans, since
a tool list is a set of capabilities and not a procedure. On a local client they
show up as ready-made commands.

## The two calls that bookend a session

**`work_on()`** is the first call of any session. It picks the mod project — one
project is chosen automatically, several and you get the list to ask the user
about — remembers the choice across sessions, installs the editor bridge, and
audits what is already there.

**`finish_and_publish()`** is what you call when the user says they are done.
It removes the bridge, which writes into the `.vrgproj` and must never ship,
re-audits, checks for `thumb.jpg` and a clean `EditorExtensionAssemblies`, and
answers with a `blocking` list that is empty when the mod is publishable.

Both are in the `core` profile, because forgetting either is expensive and a
small model is exactly the one that will forget.

## Tools

50 tools in eight groups (the groups `SE2_MCP_DISABLE` takes). The nineteen in **bold** are the `core` profile.

| group | tools |
|---|---|
| **Knowledge** | **`explain`** — measured reference facts, starting with `explain('rules')`; **`mod_recipes`** — build procedures |
| **Lookup** | **`sdk_info`**, **`build_index`**, **`search_content`**, **`resolve_guid`**, **`find_references`**, **`read_definition`**, **`subject_files`**, **`list_types`**, **`describe_type`** |
| **Authoring** | **`scaffold_mod`**, **`new_guids`**, **`write_definition`**, `refresh_meta` |
| **Checking** | **`work_on`**, **`finish_and_publish`**, **`self_test`**, **`audit_project`**, `validate_project`, `build_project` |
| **Logs** | **`read_app_log`**, `list_app_logs` — the editor's, HUB's and the game's own logs |
| **Editor** | `editor_status`, `install_bridge`, `uninstall_bridge`, `editor_state`, `editor_events`, `editor_eval`, `editor_eval_reset`, `editor_service`, `editor_screenshot`, `editor_validation`, `editor_build`, `editor_project`, `editor_viewmodels`, `editor_selection`, `editor_explorer`, `editor_generators`, `editor_create_from_template`, `editor_open_asset` |
| **Mod HUB** | `modhub_status`, `modhub_projects`, `launch_modhub`, `launch_editor` |
| **Blender** | `blender_status`, `blender_python`, `blender_measure`, `blender_export_model`, `blender_material_library` |

`explain` and `mod_recipes` are the two to read first. `explain` says what a
thing *is* — PNG formats, the cube basis, ColorKeys, why the editor refuses to
open. `mod_recipes` says how to build one, in what order, with which tool.

**`explain('rules')` is the one to read before writing anything.** Twelve
numbered rules, each measured against shipped data rather than reasoned about:
which cube face goes in which slot, which texture preset to use and what BC7
costs you, why a GUID for a `.png`/`.comptex`/`.cubemap` is never yours to
invent, and why the project must be reloaded after an edit. They are the
mistakes that cost the most time here, and none of them warn you.

## Tests

```bash
python -m unittest discover -s tests -t .
```

Covers authoring, the profile and nullability rules, and the search. The modules that talk to other programs are tested against
stand-ins on a local ephemeral port or with the process call patched out: the
editor bridge, Blender, Mod HUB, the content builder, the app logs, the session
state and the audit. Nothing starts a real process or touches your real mods,
cache or Mod HUB settings.

The suite runs without the SDK too: tests that need shipped content or its
index skip themselves, everything else runs. That is what
`.github/workflows/tests.yml` checks on a clean Windows runner, on Python 3.11
and 3.14.

## License

MIT, see [LICENSE](LICENSE).

## The handbook in `.claude/skills/se2-modsdk/`

A skill shipped inside this repository, in two halves.

`reference/` is nine hand-written pages of measured knowledge — the file format,
projects and publishing, planets, **water**, blocks and models, voxel materials,
the tooling, and a symptom-to-cause list. Each fact came from reading the shipped
data, decompiling the pipeline, or watching something fail.

`types/` is generated from the installed SDK (4.0.0.3169): 900 pages, one per `$Type` that
really occurs in content, each with the SDK's own XML field documentation, how
many definitions use it, and a real vanilla file to look at. Start at
`types/index.md`, sorted by usage.

```bash
python .claude/skills/se2-modsdk/check_version.py      # 0 match, 2 differ
python .claude/skills/se2-modsdk/build_reference.py    # regenerate types/
```

It is plain Markdown with no runtime dependency on the server, so it is equally
readable by a client that cannot run MCP at all. Claude Code picks it up as a
project skill automatically.

## Writing safely

The publish-hash investigation set the rules. A `.meta` records
`FileHash` = base64(MD5(bytes)) of its asset, and the pipeline compares them —
so editing an asset and leaving its meta alone manufactures the *"dependencies
hashes do not match"* failure that blocks publishing.

- **Nothing is written inside the SDK's `GameData`.** Every writing tool
  refuses: `write_definition` and `refresh_meta`.
- **Paths must be absolute.** A relative one would land wherever the server
  process happens to have been started, which is not anywhere the caller meant.
- **Existing files are not overwritten** unless `overwrite=true`, and the
  previous version — definition and sidecar both — is kept in `.backups/`.
- **An overwrite keeps the file's GUID.** That GUID is what every reference to
  it points at, and regenerating one would detach the file from everything that
  used it with nothing reporting the break.
- **`build_project` supports a dry run**, and `audit_project` is the offline
  check that works even when the CLI cannot load the project.

After any write, reload the project in the editor: asset processors run at
project *load*, not at build, so that is what refreshes the processed outputs.
`refresh_meta` writes the new hash into both the source and processing records,
which tells the pipeline the output is already current — so if `Content/` still
holds the old output, delete it or leave the `.meta` stale until the next load.

## The editor and Blender bridges

`install_bridge` adds a plugin DLL to a project's `EditorExtensionAssemblies`,
which is what makes `editor_eval`, `editor_screenshot` and the rest work. Two
things follow from that:

- **`uninstall_bridge` before publishing.** The bridge must never ship in a mod.
- **A dead bridge path bricks the project.** If the DLL is missing, the editor
  exits before its window appears and Mod HUB shows only `ApplicationError`. See
  `explain('project-dependencies')`.

Blender talks to the BlenderMCP add-on on `127.0.0.1:9876`, alongside Keen's
official `vrage_tools` add-on whose 27 operators produce the exact FBX/LOD/
collision layout the pipeline expects.

### The bridge is authenticated

`/eval` compiles and runs arbitrary C# inside the editor, so binding to
`127.0.0.1` is not on its own a protection. A web page the user happens to be
viewing can POST to localhost, and a body sent as `text/plain` is a "simple
request" that skips the CORS preflight entirely — which made every route
reachable from any site while the editor was open.

Three independent locks now:

- **A bearer token**, 32 random bytes, regenerated at every editor start and
  handed over through `%LOCALAPPDATA%/se2-mcp/bridge-token.txt`. Compared in
  constant time. It is written *after* the listener binds, so a second editor
  instance that loses the port cannot clobber the working one's token.
- **Host header validation**, so a name pointed at 127.0.0.1 (DNS rebinding)
  cannot arrive as a same-origin request.
- **`Content-Type: application/json` required on POST**, which is the exact
  thing a cross-origin simple request cannot send.

`/ping` stays open and deliberately thin, so a client with a stale token can
still tell "editor not running" from "token no longer matches".

### A script can stop itself

A script on the editor's UI thread cannot be aborted from outside — .NET Core
has no `Thread.Abort`, and Roslyn's cancellation token is not observed inside a
tight loop. An unbounded `while` therefore froze the editor until it was killed.

- **`EditorApi.Watchdog()`** — call it inside any loop and it throws once
  `timeout_ms` is spent. Measured: a runaway loop on the UI thread now returns
  its own diagnosis at exactly the budget, and the editor stays usable.
- The outer wait gets a **1.5 s grace period** and both clocks start when the
  request *arrives*, so the cooperative path always reports before the backstop.
- **A busy guard** refuses a second call in ~0.03 s naming the script that is
  stuck, instead of queueing behind a frozen dispatcher.
- **Requests are handled concurrently**, so `/state` and `/ping` still answer
  during a long `/eval` — which is exactly when you need to ask what is stuck.
  `editor_state` reports `running_script` with its age and first 200 characters.

## When Steam updates the game

Re-run `build_index`. The index is a SQLite database of the definition tree; a
game update changes the shipped content, and nothing else needs doing.
A different SDK path, or a mod project that appears or disappears, needs no
call at all: the server notices and refreshes the index in the background,
answering from the previous one until the new one is ready.

## Two things worth remembering

**Partialdefs mostly have no GUID of their own.** Their `Manipulator` holds only
the fields being changed, so an index keyed on GUID alone drops them entirely —
and patching vanilla content is exactly what a mod does.

**`Vanilla/Assets` and `Vanilla/Content` hold the same definitions**, source and
build output. A modder should be pointed at `Assets`.
