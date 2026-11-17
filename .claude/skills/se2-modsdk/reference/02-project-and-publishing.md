# Projects, building and publishing

## Layout

```
MyMod.vrgproj                     the project
ModProject.modhub-metadata        what the Workshop page shows
thumb.jpg                         store thumbnail
Assets.meta                       marks Assets/ as a definition set  ← load-bearing
Assets/                           SOURCE — everything you author
  <Thing>/
    <Thing>.def
    <Thing>.def.meta
    …
Content/                          BUILD OUTPUT — generated, never hand-edited
  *.dds, *.def, contentcache.vrb, definitionsets.vrb
Content.meta
```

Every directory under `Assets/` needs its own `.meta`, or the pipeline does not
mount what is inside it.

## The project file

```json
"$Value": {
  "Name": "MyMod",
  "Type": "Mod",
  "ProjectID": { "Guid": "…", "ModId": null, "ServiceId": "" },
  "ProjectDependencies": [ { "Guid": "56dacb76-e25e-468a-9432-21964a9a0569" } ],
  "DefinitionSetNames": [ "World", "Core" ],
  "GameExecutable": "SpaceEngineers2.exe",
  "ReferencedAssemblies": [ "Game2.Client.dll", "Game2.Game.dll", "Game2.Simulation.dll" ],
  "EditorExtensionAssemblies": [],
  "EditorExtensionAssembliesSearchPaths": [],
  "EnableIgnoreProcessingErrorFlags": false
}
```

| project | GUID |
|---|---|
| Engine | `079da0f2-4755-491e-8688-b68b91b2fad3` |
| Vanilla | `56dacb76-e25e-468a-9432-21964a9a0569` |

Vanilla already depends on Engine, so a real mod normally lists Vanilla alone.
See [00-orientation.md](00-orientation.md) for why depending on Engine only is
the single most expensive mistake available.

**`EditorExtensionAssemblies` bricks the project if the path is dead.** The
editor throws `Could not load extension assemblies for project <name>` inside
`EditorProjectLoaderComponent.Init` — before the window exists — and Mod HUB
shows only `Editor exited with error: ApplicationError`, with nothing in the
game's log because the editor logs to `%APPDATA%/VRAGE3.ModEditor/Temp/Logs`
instead. Keep these fields empty unless a bridge is genuinely installed.

## Building

Two paths, and the choice is forced by your dependencies:

| | works on | tool |
|---|---|---|
| standalone CLI | Engine-only projects | `validate_project`, `build_project` |
| the editor | anything, including Vanilla-dependent | `editor_build`, `editor_validation` |

The CLI cannot load Vanilla: the SDK ships ~384 orphaned `.meta` files ("Loose
metafile") and the CLI has no stripped mode. No combination of arguments fixes
it. The editor and Mod HUB do run in stripped mode.

`editor_build` calls `IProjectsService.GenerateCacheAndDefinitionSet`, which
rebuilds `contentcache.vrb` and `definitionsets.vrb`. It does **not** re-run the
per-asset processors — those run at project *load*.

## Testing without publishing

The game discovers mods straight from the mods directory. Launched with
`-projectPaths:<mods dir>`, it logs:

```
Discovered local mod <project guid> C:\Users\…\Documents\SpaceEngineers2\Mods\MyMod
```

So publishing is not a prerequisite for testing. Spawn a modded planet from the
debug menu: `CTRL+F12 → Gameplay → Voxel → <name from PlanetInfoDefinition> →
set radius → Activate planet placer`.

## Publishing

```
audit_project(project)            must be clean
uninstall_bridge(project)         the bridge must never ship
launch_editor(project)
editor_validation()               must report zero Errors
editor_build(with_blobs=True)
close the editor, launch_modhub(), press Publish there
```

Mod HUB has no publish command line — its CLI carries only `--useSteamPaths` and
`--nosplash`. Publishing happens in its window, over Steam UGC.

Checklist before you press it:

- `Assets.meta` declares a `DefinitionSetItem`.
- `thumb.jpg` exists at the project root.
- `ModProject.modhub-metadata` has the Name, Summary and Tags you want shown.
- No `EditorExtensionAssemblies` left in the `.vrgproj`.
- Nothing under `Content/` without a matching source under `Assets/` — stale
  compiled output ships too.

If it fails, `read_app_log(app='modhub', contains='publish')`. Publishing runs
inside the HUB and leaves nothing in the editor log. Also check
`ShowDetailedErrors` in
`%APPDATA%/VRAGE3.ModHUB/Settings/ApplicationSettings.json` — false gives you
one generic line instead of the real problem list.

## "Asset file dependencies hashes do not match hashes saved in metadata"

From `VRage.ContentPipeline.dll`, in
`ValidateProcessingFeature.ParallelValidateProcessingState`. It fires when an
asset's dependencies hash differently from what its `.meta` records. For a
`.planetcubemap` the dependencies are the six face PNGs.

There is an official suppression, deliberately hidden:
`EnableIgnoreProcessingErrorFlags` is a `[HideInInspector]` bool on
`VRageProjectData`, so it never appears in the editor UI. With it set, an
asset's `.meta` can list the error in its `IgnoredErrors` field. The flags enum:

```
None=0  FilesHashMismatching=1  FilesDependenciesHashMismatching=2
OutputsNotMatching=4  ImportFailed=8  ProcessingUnsuccessful=16
ProcessorNotActual=32  NotRespectedDetachedState=64
ProcessingProblemsFound=128  FilesPatchingRequired=256
```

That suppresses the symptom, not the cause.

What the publisher does differently from the editor: it pushes the project with
`ignoreCaches: true`, loads with `useFileWatcher: false`, and builds a fresh
`AssetProcessingUtilities` with `DefaultProcessorSettingsProvider` — whose
`TryGetSettings` returns false for every type — where the editor uses
`ProjectContextProcessorSettingsProvider`, which layers processor settings from
the asset's own `.meta` and every parent folder's. It registers exactly three
validations: `ValidateProcessingFeature` (with
`IgnoreLooseOutputFilesDuringValidation = true`), `ValidateProjectItemsFeature`
and `ValidatePngColorProfilesFeature`.

Note also that `ParallelValidateProcessingState` waits only **one second** per
asset import; on timeout the asset is skipped rather than reported.

Measured on two real mods, every `FileHash` and every `DependenciesHashes` entry
matched and was the right shape (planetcubemap 6, comptex 2–3, cubemap 13+).
Everything checkable offline was consistent — which points at state *at publish
time*: an asset changed after the editor last processed it, or a `Content/`
output regenerated between load and publish.

The diagnostic when it happens: `audit_project(project, check_hashes=True)`
immediately after the failure, plus the full error text — the validator names
the failing assets.

## Writing safely

- Nothing may be written inside the SDK's `GameData`.
- Paths must be absolute — a relative one lands wherever the process started.
- An overwrite must keep the file's GUID. That GUID is what every reference to
  it points at; regenerating one detaches the file from everything that used it,
  and nothing reports the break.
- After any write, reload the project in the editor. `refresh_meta` writes the
  new hash into both the source and processing records, which tells the pipeline
  the output is already current — so if `Content/` still holds the old output,
  delete it or leave the `.meta` stale until the next load.
