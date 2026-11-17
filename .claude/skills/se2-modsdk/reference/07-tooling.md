# The tooling

## The MCP server

This skill ships inside the `se2-modsdk` MCP server. The server indexes the SDK
once and answers against that index — 17,600 definitions, 32,300 media assets,
170,000 reference edges — which is the only practical way to work with content
that addresses everything by bare GUID.

```
sdk_info                    what is installed, whether the index is ready
build_index                 rebuild after a game update
self_test                   prove the whole stack works, end to end

search_content(q, kind=, type_contains=, project=)
resolve_guid(guid)          the single most useful operation
find_references(guid)       reverse dependencies: what breaks if I change this
read_definition(target, at=, max_bytes=)
subject_files(subject)      every file belonging to one block/thing
list_types(contains=)       what kinds of thing are definable
describe_type(name)         the SDK's own field documentation

scaffold_mod(dir, name)     a buildable project, publish metadata included
new_guids(count)
write_definition(path, type_name, value)   with a correct .meta sidecar
refresh_meta(path)          after editing a definition by hand

audit_project(dir)          the offline check that works on Vanilla-dependent mods
validate_project(dir)       the CLI — Engine-only projects
build_project(dir, mode=)

read_app_log(app=, contains=)   app: editor | modhub | game
list_app_logs(app=)
```

Search matches **every word** of the query, so `search_content('ion thruster
500')` finds `IonThruster500` despite SE2's separator-free PascalCase names.

`explain(topic)` and `mod_recipes(topic)` carry the same measured knowledge as
these reference pages, in tool form.

Set `SE2_MCP_PROFILE=core` to expose nineteen tools instead of fifty — worth
doing for a small local model — or `mini` for eight.

## Reading the logs

Three applications, three log directories, and they do not overlap:

| app | directory | the only place that tells you |
|---|---|---|
| `editor` | `%APPDATA%/VRAGE3.ModEditor/Temp/Logs` | why the editor refused to open |
| `modhub` | `%APPDATA%/VRAGE3.ModHUB/Temp/Logs` | why a publish failed |
| `game` | `%APPDATA%/SpaceEngineers2/Temp/Logs` | what your mod did once loaded |

The game's log is the underused one. It reports `Discovered local mod <guid>
<path>` for every mod in the mods directory, `Initializing …Component` for each
subsystem, and — in the `*_Stats.log` beside it — per-pass **draw** counts, which
is how you find out whether a feature actually rendered rather than merely
loading. See [04-water.md](04-water.md) for a worked example.

## The editor bridge

`install_bridge(project)` adds a plugin DLL to a project's
`EditorExtensionAssemblies`, which is what makes the `editor_*` tools work. The
plugin opens an HTTP listener on `127.0.0.1:8765` inside `VRage.Editor.exe`.

```
editor_status()             is it reachable
editor_state()              loaded project, selection
editor_events(since=)       watch it moment to moment
editor_eval(code)           run C# inside the editor process
editor_validation()         the errors that block publishing
editor_build()              the only build that works on Vanilla-dependent mods
editor_screenshot()         a PNG of the window
editor_explorer()           what the Project Explorer is showing
editor_generators(contains=)      the Create Asset / Create Prefab menus
editor_create_from_template(path) generate a block from a template
editor_open_asset(name)
```

The editor's services are `internal`, so `editor_eval` reaches them by
reflection:

```csharp
EditorApi.GetService("Keen.VRage.Editor.Services.Selection.ISelectionService")
EditorApi.FindType("Keen.VRage.Water.Components.PlanetaryWaterComponent")
```

That is genuinely powerful — you can enumerate loaded assemblies, inspect a
runtime type's fields and methods, and read the live view-model tree. It is also
arbitrary code execution in the editor process; read a snippet before running it.

**Call `EditorApi.Watchdog()` inside any loop.** A script running on the
editor's UI thread cannot be aborted from outside — .NET Core has no
`Thread.Abort` and Roslyn's cancellation token is not observed inside a tight
loop — so a long one has to agree to stop itself. `Watchdog()` throws once
`timeout_ms` is spent. Without it, an unbounded loop freezes the editor until it
is killed.

If a script does wedge, the bridge serves requests concurrently, so
`editor_state()` still answers and reports `running_script` with its age and
first 200 characters, and any further `editor_eval` fails immediately naming
what is stuck rather than queueing behind it.

The bridge requires a bearer token, regenerated at every editor start and read
from `%LOCALAPPDATA%/se2-mcp/bridge-token.txt`; it also validates the Host
header and requires `Content-Type: application/json` on POST. Those three
together are what stop a web page the user is viewing from reaching an endpoint
that runs arbitrary C#. A 401 almost always means the editor was restarted
after the server last read the file.

Two consequences of how the bridge is installed:

- **`uninstall_bridge` before publishing.** The bridge must never ship in a mod.
- **A dead bridge path bricks the project.** If the DLL is missing the editor
  exits before its window appears. See
  [02-project-and-publishing.md](02-project-and-publishing.md).

Three assembly attributes have to be written by hand for a plugin built outside
Keen's build system, and missing any one means the assembly loads and the plugin
is silently never instantiated:

```csharp
[assembly: IndexMetadata]
[assembly: MetadataDependencies(new[] { "VRage.Plugin.Editor", "VRage.Library" })]
[module: ModuleIndexedAttributes(typeof(ProjectPluginAttribute),
                                 new[] { typeof(BridgePlugin) }, new string[0])]
```

## Blender

Blender talks over the BlenderMCP add-on on `127.0.0.1:9876`, alongside Keen's
official `vrage_tools`.

```
blender_status()             is VRAGE Tools enabled — without it there is no correct export
blender_measure(subject=)    geometry against SE2's block rules
blender_export_model(...)    the FBX/LOD/collision layout the pipeline expects
blender_material_library()   append the shared SE2 materials
blender_python(code)         the escape hatch; results come back via stdout, so print()
```

## Mod HUB

```
modhub_status()      settings, mods directory, which apps are running
modhub_projects()    the mods, with publish state and mod id
launch_modhub()
launch_editor(project)
```

Mod HUB has no plugin system and no publish command line — its CLI carries only
`--useSteamPaths` and `--nosplash`. Publishing happens in its window. But
everything that *blocks* a publish is visible through the editor bridge with
`editor_validation`.

`launch_editor` passes the same arguments Mod HUB itself uses — both
`globalProjectDirs` plus the game executable path. Without those the Vanilla
dependency fails to resolve.
