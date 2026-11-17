# Orientation

## What SE2 content is

About 124,000 files, of which roughly 17,600 are definitions and 32,300 are
media assets. Every definition is JSON with the same envelope:

```json
{
  "$Bundles": { "System.Runtime": "1.0.0.0", "VRage": "2.3.0.2798" },
  "$Type": "VRage:Keen.VRage.Some.TypeObjectBuilder",
  "$Value": { "Guid": "…", "…": "…" }
}
```

**Everything references everything else by a bare GUID with no name attached**,
sometimes written `{G}<guid>`. That single fact shapes every workflow here: you
cannot read SE2 content top-down from a folder listing, only by resolving GUIDs.
Media assets are worse — their GUID lives only in a sibling `.meta` file, so a
`Model` or `Icon` reference is unresolvable without indexing those too.

## The order to do things in

1. **Find how vanilla does it.** Whatever you are building, the base game
   already contains something close. `search_content`, then `subject_files` for
   the whole file set of one thing.
2. **Read it, with its references resolved.** `read_definition` names every
   GUID the file points at.
3. **Learn what the fields mean.** `describe_type`, or the page under
   [`types/`](../types/index.md). The SDK's own XML documentation is the only
   authoritative source and it is genuinely good.
4. **Author yours.** `write_definition` produces the `.meta` sidecar correctly;
   doing that by hand is where corruption comes from.
5. **Check it.** `audit_project` offline, `editor_validation` in the editor.
6. **Test it in the game**, not in the editor — see the trap below.

## The four traps that cost the most time

### 1. An `Assets.meta` with no `DefinitionSetItem` silently disables the mod

The project builds, the editor validates clean, and the game loads nothing at
all. There is no error anywhere. `Assets.meta` must contain:

```json
{ "$Type": "VRage:Keen.VRage.ContentPipeline.Definitions.DefinitionSetItem",
  "DefinitionSetName": "World" }
```

and `World` must be one of the project's `DefinitionSetNames`. `audit_project`
checks this.

### 2. A mod must depend on **Vanilla**, not Engine

`Engine` is `079da0f2-4755-491e-8688-b68b91b2fad3`,
`Vanilla` is `56dacb76-e25e-468a-9432-21964a9a0569`.

Depending on Engine alone loads no vanilla definitions and no Game2 types, and
the symptoms never name the cause: `Cannot locate base definition for <guid>`,
assertion failures in `PartialDefinitionDiff.cs`, `Unable to locate a type named
Game2:…ObjectBuilder`. The editor then offers to delete the "corrupted" asset.
**Do not delete it.** The file is fine; its base is not loaded.

The cost of depending on Vanilla is that the standalone CLI
(`validate_project`, `build_project`) physically cannot load the project — the
SDK ships ~384 orphaned `.meta` files and the CLI has no stripped mode. Use
`audit_project` and the editor instead. Every real mod lives with this.

### 3. Asset processors run at project **load**, not at build

Edit a definition outside the editor and the compiled copy under `Content/`
keeps the old values while `Assets/` shows the new ones. `editor_build`
regenerates caches and definition sets; it does **not** re-run the per-asset
processors. Restart the editor on the project after editing files by hand.

### 4. The editor cannot show you everything

The editor previews assets. It does not run a game session, so anything that is
a simulation component — water above all — will never appear there no matter how
correctly it is authored. See [04-water.md](04-water.md). When something looks
missing in the editor, ask whether the editor is even capable of showing it
before you start changing files.

## Two things worth remembering

**Partialdefs mostly have no GUID of their own.** An `Override` partialdef holds
only the fields being changed, and its identity lives solely in its `.meta`
`AssetID`. An index keyed on `$Value.Guid` alone drops them entirely — and
patching vanilla content is exactly what a mod does.

**`Vanilla/Assets` and `Vanilla/Content` hold the same definitions**, source and
build output. Always read and copy from `Assets`.

## Where things live

```
<Steam>/steamapps/common/Space Engineers 2 - Mod SDK/
  GameData/Vanilla/Assets/     the base game's content — read-only reference
  GameData/Engine/             the engine's own definitions
  Editor/                      VRage.Editor.exe, the CLI, and *.xml field docs
  ExampleMod1/                 Keen's reference model/LOD/collision layout
  BlenderMaterialLibrary/      the shared SE2 materials

~/Documents/SpaceEngineers2/Mods/<YourMod>/      where mods live
%APPDATA%/VRAGE3.ModEditor/Temp/Logs/            editor log
%APPDATA%/VRAGE3.ModHUB/Temp/Logs/               Mod HUB log (publishing)
%APPDATA%/SpaceEngineers2/Temp/Logs/             the game's log and *_Stats.log
```

The game discovers unpublished mods directly from the mods directory — it is
launched with `-projectPaths:<mods dir>` and logs
`Discovered local mod <guid> <path>`. You do not have to publish to test.
