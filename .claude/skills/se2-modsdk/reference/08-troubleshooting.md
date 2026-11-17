# Symptom → cause

Work down this list before changing files. Most of these produce no error
message anywhere, which is exactly why they cost so much time.

## The mod loads but nothing appears in game

`Assets.meta` has no `DefinitionSetItem`. The project builds, the editor
validates clean, and the game mounts nothing. There is no error anywhere.
`audit_project` checks it. See [00-orientation.md](00-orientation.md).

## The editor refuses to open; Mod HUB says only `ApplicationError`

Either a dead `EditorExtensionAssembliesSearchPaths` entry — the editor throws
inside `EditorProjectLoaderComponent.Init`, before the window exists — or the
project's dependency came back as Engine instead of Vanilla after a re-save.

`read_app_log(app='editor')` names it. Note the editor logs to
`%APPDATA%/VRAGE3.ModEditor/Temp/Logs`, **not** the game's log directory, which
is why the failure looks silent.

## `Cannot locate base definition for <guid>`, or an offer to delete a "corrupted" asset

The project depends on Engine, not Vanilla. The file is fine; its base is not
loaded. **Do not delete it** — deleting a partialdef silently drops whatever it
was overriding. Fix the dependency.

Signature of this bug: *one* mod failing while sibling mods open normally,
usually after a newer Mod HUB re-saved the project.

## Edited a definition but the game still shows the old value

Asset processors run at project **load**, not at build. `editor_build`
regenerates caches and definition sets only. Restart the editor on the project.

And if you ran `refresh_meta` after editing by hand: it writes the new hash into
both the source record and the processing record, which tells the pipeline the
output is already current. If `Content/` still holds the old output the edit is
skipped. Either delete the matching file under `Content/`, or leave the `.meta`
stale until the next project load.

## `validate_project` fails with "Loose metafile"

The failure is in the SDK's Vanilla project, not your mod: it ships ~384
orphaned `.meta` files with no source asset. The standalone CLI has no stripped
mode and cannot load Vanilla at all — no combination of arguments fixes it.

Use `audit_project` for offline checks and `editor_build` / `editor_validation`
for the authoritative ones.

## "Asset file dependencies hashes do not match hashes saved in metadata"

An asset's dependencies hash differently from what its `.meta` records — for a
`.planetcubemap`, the six face PNGs. Usually it means an asset changed after the
editor last processed it. Run `audit_project(project, check_hashes=True)`
immediately after the failure and capture the full error text; the validator
names the failing assets. Full analysis in
[02-project-and-publishing.md](02-project-and-publishing.md).

## Mod HUB says "Project validation failed" and nothing else

`ShowDetailedErrors` in
`%APPDATA%/VRAGE3.ModHUB/Settings/ApplicationSettings.json` is false. Set it
true, or read the list through `editor_validation()` without leaving the agent.

## The planet is a perfectly smooth sphere

`HillParams` Min and Max are both 0, so the heightmap contributes no elevation.
Set them — and `MaxAltimeter` = `Max` — to a fraction of the radius. EarthLike
uses −0.01 / 0.12.

## The planet blurs into a bright featureless ball as the camera pulls away

The distant view is the `PlanetOverlay`, not the voxel terrain, so the fault is
in the overlay cubemaps. Two independent causes, both measurable:

- **It does not fit in VRAM.** An 8192 NAO compressed as BC7 costs 537 MB against
  268 MB for BC1, putting the planet over any shipped one; the streamer answers
  with low mips everywhere. Symptom fingerprint: **4K looks better than 8K.**
  Check the built `_Overlay_NAO.dds` — 268 MB means BC1, 537 MB means BC7. Fix
  the `.texpreset` the `.comptex` points at.
- **The surface is darker than the atmosphere.** Scattering is additive, so a
  planet below vanilla's 52–119 luma band is swallowed by its own atmosphere. A
  real-Earth albedo does this on its own: Blue Marble's ocean is luma 6 over 71%
  of the sphere.

See [03-planets.md](03-planets.md) for the preset table and the measurements.

## "Asset file dependencies hashes do not match hashes saved in metadata"

**If the failing assets are `.planetcubemap` files, this is a Mod HUB bug and no
mod can fix it from the content side.** Confirmed by publishing a planet mod
successfully after applying the workaround below.

`P_PLANETCUBEMAP` — the processor for the height, biome and material cube maps —
lives in its own assembly, and Mod HUB does not reference it:

```
VRage.ContentPipeline.PlanetTextures.dll   <- Builder, Editor, Voxels.   NOT ModHUB
VRage.ContentPipeline.Textures.dll         <- ModHUB, Builder, Editor    (P_CUBEMAP, P_TEXTURE)
```

Publish validation runs *inside* Mod HUB, so `GetProcessorMetadata(".planetcubemap")`
misses and falls back to `DefaultAssetProcessor`. That produces both reported
errors at once — `ProcessorNotActual` (the stored `{1, "P_PLANETCUBEMAP"}` cannot
match a default) and `FilesDependenciesHashMismatching` (no processor, no
resolved dependencies). Every `.cubemap` asset validates fine because `P_CUBEMAP`
is in the assembly Mod HUB *does* load. That contrast is the proof.

The fix is Keen's own hidden switch, applied to those assets only:

```
.vrgproj                     EnableIgnoreProcessingErrorFlags: true
each .planetcubemap .meta    "IgnoredErrors": "FilesDependenciesHashMismatching, ProcessorNotActual"
```

**It must be applied with Mod HUB and the editor closed.** Both hold the project
in memory and write their own `.vrgproj` back over yours — measured: edited at
22:17, overwritten at 22:19, the flag silently back to `false` and the editor
bridge reinstated. `ShouldReport` checks the project flag *before* the per-asset
`IgnoredErrors`, so with the flag reverted the suppression is never read and the
error looks unchanged. `tools/prepare_publish.py` does all of it and refuses to
run while either app is up.

Then open Mod HUB and publish **without opening the editor first** — it puts the
bridge back and clears the flag again.

---

For every other asset type, the error means what it says. **Reproduce it offline
before theorising** — but note the CLI cannot reproduce the planetcubemap case,
because `VRage.ContentPipeline.Builder` *does* reference PlanetTextures and
therefore reports Success on a project Mod HUB rejects.

```bash
"$SDK/Editor/VRage.ContentPipeline.Builder.exe" -p "$MOD/$MOD.vrgproj" --prepareForPublish "$OUT" --globalProjectDirs "$SDK/GameData" --globalAssemblyDirs "$SDK/Editor"
```

`Exiting from processing done with Success.` means it would publish. `$OUT` must
**not already exist** — otherwise it fails instantly with "Publish directory
already exists", which is not the error you are chasing. Budget a couple of
minutes and a few GB for a planet mod.

The condition, from `ValidateProcessingFeature`:

```csharp
PerformImport(...).WaitBlocking(TimeSpan.FromSeconds(1L), out result);   // 1 s per asset
else if (preImportData is PreImportData.Success { OutdatedDependencies.Count > 0 })
    FilesDependenciesHashMismatching.TryAdd(assetFile, ...);
```

and the dependency set is **transitive** —
`GetTransitiveReferencesFrom(AssetID, {Dependency})`. A GUID is outdated when its
stored hash differs from the file's current hash **or when it is absent from
`DependenciesHashes` altogether**. That is why hand-writing a `.meta` with only
the direct dependencies manufactures this error, and why the fix is to let the
editor regenerate it rather than to patch the hash. An unresolvable dependency
reports "import failed" instead.

Two things worth checking that are *not* the cause: `ProcessorInfo.Version 0` on
a raw source PNG is normal (vanilla Verdure has 18 of 42 that way — the PNG is an
input, the `.comptex` is what gets processed), and `DependenciesHashes` entries
pointing at Engine/Vanilla files do not drift on their own.

**`--prepareForPublish` does not strip the editor bridge.** The packaged
`.vrgproj` keeps `EditorExtensionAssemblies` and its absolute search path; a
subscriber has neither, and a dead bridge path stops the editor opening at all.
Remove it first — `finish_and_publish` does.

Last resort, symptom only: set `EnableIgnoreProcessingErrorFlags` on the project
and `"IgnoredErrors": "FilesDependenciesHashMismatching"` on the failing asset.

## A cubemap you authored by hand reports every face as an unresolved GUID

You invented AssetIDs for the `.comptex` files and wrote them into the
`.cubemap`. **If the editor is running it watches the project folder, imports
anything new, and assigns its own AssetID**, overwriting the `.meta` you wrote —
so the GUIDs the cubemap points at no longer exist.

For **media** (`.png`, `.comptex`, `.cubemap`, `.texpreset`) the AssetID is the
editor's to allocate. Write the asset file, let the editor import it, then read
the ID back out of the `.meta` and write *that* into whatever references it.
Inventing GUIDs is only safe for `.def`/`.partialdef`, where `write_definition`
owns both the file and its sidecar.

`audit_project` catches this immediately — but rebuild the index first, or it
reports assets it has simply not seen yet.

## Only some of the assets you just edited get processed

Asset processors run at project **load**. Files edited individually in a session
tend to get processed as you go; **several files written in the same second — a
batch edit or a script — can be skipped entirely**, and the editor then reports
`Preset reference is outdated` (or leaves the asset stale with no message).

The tell is in the `.meta`, in its `AssetProcessingMetaDataItem`:

```
processed          not processed
─────────────      ─────────────────────
Version: 5         Version: 0
Identifier:        Identifier: ""
  "P_TEXTURE"      ContentFiles: null
ContentFiles: {…}  AssetHash: ""
AssetHash: <hash>  ← equals FileInfoMetaDataItem.FileHash when current
```

`AssetHash` empty or different from the file's own `FileHash` means the output on
disk does not correspond to the source. **Reload the project**; do not hand-edit
the meta, and do not conclude the edit itself was wrong — the source files are
usually fine.

## The planet does not appear in the debug menu template list

There is no `PlanetInfoDefinition`. Nothing references it, so no validator
reports it missing. See [03-planets.md](03-planets.md).

## No water on the planet

First: **were you testing in the editor?** The editor runs no server session and
water is created only by the server, so planetary water can never appear there —
for your planet or for vanilla EarthLike. Test in game.

Second: in the shipped content only EarthLike (legacy VS1_5) wires planetary
water at all; even Byblos has an orphaned water-layers definition. A correctly
authored mod can still show nothing because the feature is not switched on for
modern planets. Check the game log before changing anything.

Full analysis, including why massfill destroys performance, in
[04-water.md](04-water.md).

## Water is unbearably slow after adding it from the debug menu

You are running a 10-million-cell fluid simulation. Massfill is sized for a pond
(`MaxCells: 10000000` at 0.5 m per cell ≈ a 108 m cube), not an ocean. See
[04-water.md](04-water.md).

## A GUID will not resolve

Dictionary keys, `TagSlots` values, `SurfaceBiomes`/`MaterialRules` keys and
animation node ids are GUIDs that name a type or a node, not a file. They do not
resolve in vanilla either. Only real asset references must.

## Blender export produced nothing

`limit='SELECTED_OBJECTS'` with an empty selection exports nothing and reports
success. Select the mesh, or pass `limit='VISIBLE_OBJECTS'`. Always check the
files that actually landed on disk.

## An editor plugin loads but is never instantiated

One of the three assembly attributes is missing — `[assembly: IndexMetadata]`,
`[assembly: MetadataDependencies(...)]`, `[module: ModuleIndexedAttributes(...)]`.
Without all three the assembly loads and the plugin is silently skipped. See
[07-tooling.md](07-tooling.md).

## Textures come out wrong after a resize

An index map (biome, material) was resampled with a smooth filter. Any bilinear
or area filter invents in-between values that map to no material. Nearest
neighbour only — always. Keen made this mistake themselves on Verdure's 2048
material map.
