"""Measured facts about the SE2 Mod SDK, written as answers rather than notes.

Everything here came from reading the shipped data and, where it mattered, from
decompiling the content pipeline — not from documentation, which does not exist
for most of it. Each topic is meant to be enough on its own for a model with no
other context to act correctly.

This is the reference half of the server's knowledge. `recipes.py` is the
procedural half: what to do, in what order, with which tool. Look here for what
a thing *is*, there for how to build one.
"""

from __future__ import annotations

from typing import Any

TOPICS: dict[str, dict[str, str]] = {

    "file-format": {
        "title": "How every definition file is shaped",
        "summary": "The JSON envelope, GUID references, and the partialdef pattern.",
        "body": r"""Every `.def` and `.partialdef` file has the same envelope:

    {
      "$Bundles": { "VRage": "2.3.0.2798", ... },
      "$Type": "Assembly:Namespace.TypeObjectBuilder",
      "$Value": { "Guid": "...", ... }
    }

`$Type` is "assembly:full.type.name" — the assembly is VRage or Game2.
`$Value.Guid` is the definition's own identity. **Everything references
everything else by bare GUID with no names attached**, sometimes written
`{G}<guid>`. That is why an index is worth building: a folder listing tells you
almost nothing.

`.partialdef` files are the SDK's central pattern — 9,142 of the 35,174
definition files. They are a delta against a base rather than a whole object:

    "$Type": "VRage:Keen.VRage.ContentPipeline.Definitions.PartialDefinitionDiff",
    "$Value": {
      "BaseDefinition": "<guid of the thing being patched>",
      "PartialDefinitionKind": "Copy" | "Override",
      "Manipulator": { ...the fields to change... },
      "DefinitionType": "VRage:Full.Type.Of.The.Base"
    }

Lists inside a Manipulator are often `$DeltaEncoded`, with `Keys`, `Changed`
(each entry `Insert`/`Update` at an `Index`) and `Removed`. This is how a mod
edits vanilla content without copying it.

Newtonsoft.Json is used on the game side, and it requires `$id` to be the first
property of an object when present. Never re-serialise a definition with a
generic JSON writer that reorders keys.""",
    },

    "project-dependencies": {
        "title": "Project dependencies, and the two ways they stop the editor",
        "summary": "Engine vs Vanilla, and dead EditorExtensionAssemblies paths.",
        "body": r"""A mod's `.vrgproj` lists `ProjectDependencies` by project GUID. There
are only two projects to depend on, and they are not interchangeable:

    Engine    079da0f2-4755-491e-8688-b68b91b2fad3   the engine only, no content
    Vanilla   56dacb76-e25e-468a-9432-21964a9a0569   the game's content (depends on Engine)

**Almost every mod must depend on Vanilla.** Depending on Engine alone loads no
templates, no vanilla definitions and no Game2 object-builder types, and the
symptoms do not name the cause:

    JsonSerializationException: Cannot locate base definition for <guid>
    Assertion failure in ...ContentPipeline/Definitions/PartialDefinitionDiff.cs:66
    Unable to locate a type named Game2:Keen.Game2.Client...ObjectBuilder

The editor then offers to delete or back up the "corrupted" asset. **Do not
delete it** — the file is fine; its base is simply not loaded. Deleting a
partialdef silently drops whatever it was overriding. Fix the dependency instead.

Observed on a real project: the mod had been re-saved by a newer HUB, and the
dependency came back as Engine. Every `_ServerComposition`, `_PlanetGenerator`,
`_EnvironmentData` and `_PlanetAmbianceAudio` partialdef failed at once. Sibling
mods on the older version still listed Vanilla and opened normally — so *one mod
failing while the others are fine* is the signature of this bug.

**The second failure mode: EditorExtensionAssemblies.** These two fields load a
plugin DLL into the editor at startup:

    "EditorExtensionAssemblies": [ "SomeBridge.dll" ],
    "EditorExtensionAssembliesSearchPaths": [ "C:\\some\\build\\output" ]

If the DLL is not at that path, the editor does not warn and carry on — it
throws `Could not load extension assemblies for project <name>` inside
`EditorProjectLoaderComponent.Init`, which happens before the window exists.
Mod HUB shows only `Editor exited with error: ApplicationError`, with no log in
`%APPDATA%/SpaceEngineers2/Temp/Logs` because the editor logs to its own
`%APPDATA%/VRAGE3.ModEditor/Temp/Logs` instead.

So a renamed or moved build folder silently bricks the project. Keep these
fields empty unless a bridge is actually installed, and never let them ship —
`uninstall_bridge` clears them.

Reading the log is the fast path for both: `read_app_log(app='editor')`.""",
    },

    "ore-textures": {
        "title": "How to change an ore or voxel material's textures",
        "summary": "The full chain from a PNG to a voxel material, and how a mod injects it into a generator.",
        "body": r"""This is the chain, verified against a working mod:

    VoxelMaterialDefinition           identity: Name, PhysicsMaterial
      ^ VoxelMaterial
    VoxelRenderMaterialDefinition     binds VoxelMaterial -> RenderMaterial + Icon
      ^ RenderMaterial
    TriplanarSingleMaterialDefinition  the actual textures
      |- ColorMetal{XZ,Y}{Near,Far1,Far2}       <- *_cm.comptex
      |- NormalRoughness{XZ,Y}{Near,Far1,Far2}  <- *_nr.comptex
      |- Extensions{XZ,Y}{Near,Far1,Far2}       <- *_add.comptex
      |- Displacement{XZ,Y}{Near,Far1,Far2}     <- *_displacement.comptex
      \- ColorFar3: a single packed colour for the farthest LOD
           ^ each .comptex packs source PNGs
    PNG sources: Albedo, AO, Height, Normal, Roughness, (Metalness)
                 at three levels: _Y_Near, _Y_Far1, _Y_Far2

So "replace an ore's texture" means: author the PNGs, let the `.comptex` recipes
pack them, and point a TriplanarSingleMaterialDefinition at the results. The
VoxelMaterialDefinition itself holds no textures at all.

**Injecting into a generator.** For asteroids, a mod overrides the vanilla
VoxelGeneratorDefinition with a partialdef:

    "PartialDefinitionKind": "Override",
    "DefinitionType": "VRage:Keen.VRage.Voxels.Definitions.VoxelGeneratorDefinition",
    "Manipulator": {
      "Settings": { "DepositsCountCoefficient": 1, "DepositSizeDenominator": 12 },
      "DepositMaterials": { "$DeltaEncoded": true, "Keys": [...], "Changed": [
        { "Kind": "Insert", "Index": 0,
          "Value": { "Material": "<VoxelMaterial guid>",
                     "AsteroidGeneratorSpawnProbabilityMultiplier": 7 } } ],
        "Removed": [...] }
    }

**On a planet the ores come from somewhere else.** They are in
`PlanetBiomeDefinition.OreRules[].Ore.Material` — again a VoxelMaterial GUID,
with MinSize, MaxSize, MinBiomeDepth, MaxBiomeDepth and a Probability, plus
`OresPerCubicKilometer` on the biome. So changing a planet's ore textures means
finding the VoxelMaterials named in that planet's biome definitions and
replacing their render materials — not touching the asteroid generator.

Use `find_references` on a VoxelMaterialDefinition GUID to see every generator,
biome and placement rule that spawns it before changing anything.""",
    },

    "planet-structure": {
        "title": "How a planet is wired together",
        "summary": "Generator, height cube map, biome map, material map, and what each drives.",
        "body": r"""    PlanetGeneratorDefinition        HillParams, ZeroGround, six heightmap GUIDs
      \- heightmap cube map           6 x 16-bit greyscale PNG, colour type 0

    PlanetBiomeMapDefinition         joins the two index maps
      |- BiomeMapDefinition
      |    \- SurfaceBiomes[]        Key -> engine-side GUID, NOT in GameData
      |         \- Value -> PlanetBiomeDefinition
      |                       ColorKey, OreRules, OresPerCubicKilometer
      \- MaterialMapDefinition
           \- PlanetMaterialMapDefinition   ColorKey
                \- MaterialRules[] -> PlanetMaterialPlacementRuleDefinition
                                       Layers[{Material, Depth}], Slope{Min,Max}

**In SurfaceBiomes the ColorKey is on the `Value` side.** The `Key` GUID
resolves to nothing anywhere in GameData — it is engine-side. Read the pair the
other way round and every ColorKey comes back null.

**Biome map and material map are different things.** The biome map drives ores,
flora, encounters and spawn rules; the material map drives what the ground is
made of. The biome map is coarse and the material map is rich: vanilla Byblos
has 4 biomes and 31 material ColorKeys.

**Cliffs are not encoded in the map.** Every placement rule carries its own
`Slope: {Min, Max}`, and one ColorKey can hold several rules, so the engine
picks the steep-slope variant itself. The map encodes terrain *type* only.

**Placement rules cross planet boundaries.** Byblos's material maps reference
Verdure's `CliffsSnowPlacementRule` and `SeaRocksPlacementRule`. A new planet
can reference vanilla rules directly instead of authoring its own.

**UndergroundBiomes carry no ColorKey**, so they cannot be painted. They are
depth layers, and vanilla puts only Nickel, Iron and InnerCore in them. Rare ore
is placed through surface biomes, which is why the biome map can steer it
geographically.""",
    },

    "colorkeys": {
        "title": "ColorKeys are author-defined, not a fixed set",
        "summary": "There is no magic numbering; the map's values must match your own definitions.",
        "body": r"""A `ColorKey` is just the 8-bit value you painted into the index map. You
choose it, and you bind it by creating a PlanetMaterialMapDefinition or
PlanetBiomeDefinition with that number.

Verdure's habit of using multiples of ten is a Verdure habit, nothing more.
Measured across all fifteen vanilla planets:

    Verdure, Byblos   biome 10,20,...,80 and 200
    Caligo            90, 100, 101
    Geomeles          90, 96
    Palatine          90...97
    Kemik             10, 40, 50, 228, 230
    MarsLike          22, 46, 55...61
    EarthLike         0, 3, 10, 13, 17, 20, 27, 30, 33, 36, 40, 43, 46, 50, 56, 60, 75, 76

Material maps use their own, denser space — Verdure 1..93, Byblos up to 111.

The only hard rule: **the set of values present in the map must match the set of
definitions you created**, or texels fall through to nothing.

And the one universal constraint on these maps: **index maps must only ever be
resampled nearest-neighbour**. Any bilinear or area filter invents in-between
values that map to no material. Keen's own 2048 material map for Verdure carries
106, 113, 135, 140, 164, 194, 224, 253, 254 and 255 that do not exist in the 8192
original — they filtered a downscale.""",
    },

    "map-formats": {
        "title": "Exact PNG formats for planet maps",
        "summary": "Measured across all fifteen vanilla planets.",
        "body": r"""Modern convention, VS2_0 onward. VS1_5 differs and is not a model to copy.

    heightmap      16-bit greyscale, colour type 0    2048 / 4096 / 8192 square
    biome map       8-bit greyscale, colour type 0    4096 / 8192
    material map    8-bit greyscale, colour type 0    2048 / 4096 / 8192
    albedo          8-bit RGB                         4096 / 8192
    normal         16-bit RGBA, alpha a dead 255      4096 / 8192
    ambient occl.   8-bit greyscale                   4096 / 8192
    roughness       8-bit greyscale, optional         4096

All non-interlaced. Colour type 4 (grey+alpha) also decodes but doubles the file
for a dead channel and no vanilla asset uses it.

Normal and AO are often authored at 8192 while albedo stays at 4096 — Caligo,
Geomeles and Palatine all do this. The sizes are independent.

Per-face PNGs are packed by the content pipeline into two cube maps via
`.comptex` intermediates: `*_cm.comptex` -> `*_Overlay_CM.cubemap` (colour +
metal) and `*_nao.comptex` -> `*_Overlay_NAO.cubemap` (normal + AO).

**Height encoding.** The generator maps a texel value back to a radius:

    radius(v) = R * (1 + hill_min + (v / 65535) * (hill_max - hill_min))

`ZeroGround` is sea level in the same radius fractions, so the texel at the
waterline is `(zero_ground - hill_min) / (hill_max - hill_min) * 65535`.
Verdure: -0.01..0.12, ZeroGround 0.015 -> 12603. Byblos, the water planet:
-0.3333..0.03333, ZeroGround 0 -> 59577, spending 91% of the band below water.

**The coastline is a contract.** Planetary water sits exactly on ZeroGround, so
land must encode strictly above the sea value and ocean strictly below. A single
land texel at or below it leaks water inland.""",
    },

    "cube-basis": {
        "title": "The cube-face basis, and the trap in it",
        "summary": "Which way each face points. Verified by seam measurement, not assumed.",
        "body": r"""`+u` is increasing image column, `+v` increasing image row, world `+Y` is
the north pole.

    face    normal   +u (right)   +v (down)
    front   Z-       +X           Y-
    right   X-       Z-           Y-
    back    Z+       X-           Y-
    left    X+       Z+           Y-
    up      Y+       X-           Z+
    down    Y-       X-           Z-

**The trap:** around the equator the strip runs right to left, so `front`'s
right-hand edge joins `left`, not `right`. The commonly posted cross diagram is
easy to read the wrong way here.

This was verified by measuring cross-face seam error on Keen's own Verdure
heightmaps under this basis and under plausible wrong ones: correct basis gives
a seam/interior ratio of 0.99, a rotated `up` gives 1.51, all faces flipped
gives 6.09, and a reversed equator gives 144.

Adjacent faces sample the sphere half a texel apart across a shared edge, so
their edge values are *not* meant to be identical. Generate all six from one
global field and the seams come out right with no stitching step.

**Keen's own maps name faces straight through** — the file called `left` goes in
the left slot. A generator that already uses this basis needs no swap; adding
one mirrors the planet.

**Two cubemap formats name their slots differently, and this is the single
easiest thing to get backwards.** `.planetcubemap` (height, biome, material) has
NAMED slots — `Right Left Up Down Backward Forward` — and the names match
straight through. `.cubemap` (overlay CM and NAO) has AXIS slots, and there you
must go through the table above:

    PositiveXTexture  <- the face called LEFT   (its normal is X+)
    NegativeXTexture  <- the face called RIGHT  (its normal is X-)
    PositiveYTexture  <- up
    NegativeYTexture  <- down
    PositiveZTexture  <- the face called BACK   (its normal is Z+)
    NegativeZTexture  <- the face called FRONT  (its normal is Z-)

Verdure's own overlay cubemap is wired exactly this way. It looks like a
mistake and is not.

**Check it by measurement, not by reasoning.** A surface normal points outward,
so on the `+X` cube face of the built `_Overlay_NAO.dds` the mean red channel
must exceed 128, and on `-X` fall below it. Verdure measures +X R=180, -X R=80,
+Y G=178, -Y G=74, +Z B=175, -Z B=74 — all six on the correct side.

**A cube face's ground scale is not uniform.** With `r² = 1 + s² + t²` over face
coordinates, `|dP/ds| = R·√(1+t²)/r²`, and one texel is `ds = 2/N`. At N = 8192
and R = 60 km that is 14.65 m per texel at the centre against 6.90 m at the
corner — a factor of 2.12. Stock normal map filters assume a constant spacing
and therefore exaggerate corner slopes; so does any slope statistic that applies
the centre spacing to a whole face, an error that has silently doubled a
vertical-scale calibration before now.""",
    },

    "rules": {
        "title": "Hard rules — read this before writing anything",
        "summary": "Short, exact, measured. Every line here was verified against shipped data, not guessed.",
        "body": r"""Numbered so you can follow them without judgement calls.

1. GUIDs FOR MEDIA ARE NOT YOURS TO INVENT.
   For .png .comptex .cubemap .texpreset: create the FILE, let the editor
   import it, then READ the AssetID back out of the .meta beside it.
   The editor watches the project folder and overwrites any AssetID you wrote.
   Only .def and .partialdef take a GUID you supply, via write_definition.

2. CUBEMAP SLOTS. Two formats, two naming schemes.
   .planetcubemap  (height, biome, material)  slots are NAMED:
       Right Left Up Down Backward Forward   -> match straight through,
       left.png goes in Left.
   .cubemap  (overlay CM/NAO, clouds)  slots are AXES:
       PositiveXTexture <- the face called LEFT
       NegativeXTexture <- the face called RIGHT
       PositiveYTexture <- up
       NegativeYTexture <- down
       PositiveZTexture <- the face called BACK
       NegativeZTexture <- the face called FRONT
   Yes, +X takes "left". The left face's normal is X+. Vanilla does this.

3. CHECK RULE 2 BY MEASUREMENT, NOT BY THINKING.
   Decode the smallest mip of each cube face of the built _Overlay_NAO.dds.
   +X mean red MUST be > 128, -X < 128, +Y green > 128, -Y < 128,
   +Z blue > 128, -Z < 128. Verdure reads 180/80, 178/74, 175/74.

4. OVERLAY NORMAL+AO COMPRESSION.
   Each face .comptex must point at TangentToWorldSpace<Dir>NormalAOTexture
   (BC1_UNORM), NEVER PBRMaterialTemplate_NormalAOTexture (BC7_UNORM).
   BC7 doubles VRAM: 537 MB instead of 268 MB for an 8192 cube. Over budget
   the whole planet streams from low mips and looks blurry from orbit.
   Symptom that proves it: 4K looks BETTER than 8K.
   Pick the preset by the SLOT the image sits in (rule 2), not by file name.
   Colour uses PBRMaterialTemplate_ColorTexture on all six faces.

5. CUBEMAP CATEGORY.
   Overlay colour  -> "PlanetColorOverlay"
   Overlay normal/AO -> "PlanetOverlays"
   Cloud cubemaps  -> "None"
   The wrong one still builds, so nothing warns you.

6. AFTER EDITING ASSETS, RELOAD THE PROJECT.
   Processors run at project LOAD, not at build. Several files written in the
   same second are often skipped entirely. A .meta whose
   AssetProcessingMetaDataItem shows Version 0 / Identifier "" / AssetHash ""
   was never processed. Reload; do not hand-edit the meta.

7. INDEX MAPS ARE NEAREST-NEIGHBOUR ONLY.
   Biome and material maps hold indices, not values. Any interpolation invents
   indices that resolve to nothing.

8. A MOD DEPENDS ON THE VANILLA PROJECT, NOT ENGINE.

9. COLORKEYS ARE AUTHOR-DEFINED. They are just the 8-bit number you painted.
   In SurfaceBiomes the ColorKey is on the VALUE side, not the Key side.

10. PLANET SURFACE BRIGHTNESS HAS A WORKING RANGE.
    Mean colour of the built _Overlay_CM.dds is 52..119 across all vanilla
    planets. Below that floor the atmosphere swallows the planet at distance.
    Real Earth imagery breaks this on its own: Blue Marble's ocean is luma 6
    over 71% of the sphere.

11. NEVER WRITE INSIDE THE SDK's GameData. Override with a partialdef.

12. BEFORE PUBLISHING, call finish_and_publish. The editor bridge writes into
    the .vrgproj and must not ship.""",
    },

    "planet-overlay": {
        "title": "The distant-view overlay: compression, VRAM budget and brightness",
        "summary": "Why a planet blurs to a bright ball when you pull away, measured across every vanilla planet.",
        "body": r"""`VoxelPlanetRenderComponentDefinition.PlanetOverlay` is, in the SDK's own
field documentation, "displayed in place of detailed voxel rendering when the
camera is sufficiently far away". Everything you see from orbit is this, not the
voxel terrain. Two independent things go wrong with it.

**1. It does not fit in the streaming budget.** Total overlay VRAM, measured on
the built .dds files of every planet under Assets/Procedural:

    Byblos                     134 MB   (CM 4096 BC1, NAO 4096 DXT1)
    Testerran                  168 MB
    MarsLike                   268 MB
    Caligo/Geomeles/Palatine   335 MB   (CM 4096, NAO 8192 DXT1)
    Kemik, VERDURE             537 MB   (CM 8192 BC1, NAO 8192 DXT1)
    EarthLike                  570 MB

Six of the eight use BC1/DXT1 for an 8192 NAO; only EarthLike and Testerran use
BC7, and both are VS1_5, the oldest generation. BC7 is 16 bytes per block against
BC1's 8, so an 8192 cube costs 537 MB instead of 268. A mod on BC7 pays 805 MB
for the pair — more than any shipped planet — and the streamer answers by serving
low mips for the whole sphere.

**The fingerprint is that 4K looks BETTER than 8K.** Check the built
`_Overlay_NAO.dds`: 268 MB means BC1, 537 MB means BC7.

The format comes from the `.texpreset` that each face's `.comptex` names in
`PresetReference`, via its `OutputFileCompression` field. Presets are media
assets, so their GUID is in the `.meta`, not the `.texpreset` body.

    PBRMaterialTemplate_ColorTexture               BC1_UNORM_SRGB   3 ch
    PBRMaterialTemplate_ColorMetalTexture          BC7_UNORM_SRGB   4 ch
    PBRMaterialTemplate_NormalAOTexture            BC7_UNORM        4 ch  <- wrong for planets
    TangentToWorldSpace<Dir>NormalAOTexture        BC1_UNORM        3 ch  <- correct

The generic NormalAO preset is wrong twice: BC7, and it passes the normal
through unchanged. The TangentToWorldSpace family is per-face and rotates the
normal into world space for that face's orientation - which is why there are six
and why every vanilla planet uses a different one on each face. Without it the
shading direction is wrong per face and the surface reads flat, not merely soft.

Pair the preset to the SLOT the image occupies, not to its file name: the image
in PositiveXTexture takes ...LeftNormalAOTexture, NegativeXTexture takes
...RightNormalAOTexture, +Z takes ...Backward, -Z takes ...Forward. See
`explain('cube-basis')`.

Colour needs no family - PBRMaterialTemplate_ColorTexture on all six faces.

`CubemapModel.Category` is `PlanetColorOverlay` for colour and `PlanetOverlays`
for normal/AO; all 8 vanilla colour and all 7 NAO cubemaps follow this. Both
strings exist in VRage.ContentPipeline.Textures.dll, so the wrong one still
builds.

**2. The surface is darker than its own atmosphere.** Mean colour of the built
`_Overlay_CM.dds`, from the BC1 mip at <=64 px: Titan 52, Byblos 85, Verdure 96,
Kemik 112, Palatine 117, Geomeles 119. Vanilla spans 52-119. Atmosphere
scattering is additive over the surface, so a planet below that floor is
swallowed by its own atmosphere at distance and reads as a bright featureless
ball no matter how correct the atmosphere settings are.

Real-Earth imagery walks into this: Blue Marble's ocean is about (2,5,20), luma
6, over 71% of the sphere. Keen's own water world does not - **Byblos paints its
sea bed sandy (90,80,67) and lets the volumetric water supply the blue.**""",
    },

    "publish-hash": {
        "title": '"Asset file dependencies hashes do not match hashes saved in metadata"',
        "summary": "Where the error comes from, and the hidden flag that suppresses it.",
        "body": r"""**If the failing assets are `.planetcubemap` files, this is a Mod HUB bug.**
Confirmed 2026-08-14 by publishing a planet mod after applying the fix below.
`P_PLANETCUBEMAP` lives in `VRage.ContentPipeline.PlanetTextures.dll`, and
**VRAGE3.ModHUB.dll does not reference that assembly** - only Builder, Editor and
Voxels do. Publish validation runs inside Mod HUB, so the processor lookup misses,
falls back to DefaultAssetProcessor, and reports BOTH `ProcessorNotActual` and
`FilesDependenciesHashMismatching` on those assets. Every `.cubemap` asset is fine
because `P_CUBEMAP` is in the assembly Mod HUB does load.

Fix, on the planetcubemap assets only:

    .vrgproj                   EnableIgnoreProcessingErrorFlags: true
    each .planetcubemap .meta  "IgnoredErrors":
                               "FilesDependenciesHashMismatching, ProcessorNotActual"

**Apply it with Mod HUB and the editor CLOSED.** Both hold the project in memory
and write their own .vrgproj back over yours - measured: edited 22:17, reverted
22:19, flag back to false and the bridge reinstated. `ShouldReport` checks the
project flag BEFORE the per-asset IgnoredErrors, so a reverted flag makes the
whole suppression invisible and the error looks unchanged. Then publish without
opening the editor first. `tools/prepare_publish.py` does all of it and refuses
to run while either app is up.

The CLI cannot reproduce this particular case - Builder references PlanetTextures
and reports Success on a project Mod HUB rejects.

**For every other asset type, reproduce it offline before theorising.** The
content pipeline builder exposes the same entry point ModHub uses - it validates, generates
caches, copies the project, and aborts on this failure:

    "<SDK>/Editor/VRage.ContentPipeline.Builder.exe" -p "<mod>/<mod>.vrgproj"
        --prepareForPublish "<folder that must NOT already exist>"
        --globalProjectDirs "<SDK>/GameData" --globalAssemblyDirs "<SDK>/Editor"

`Exiting from processing done with Success.` means it would publish. If the
target folder exists it fails instantly with "Publish directory already exists",
which is not the error you are chasing.

Note it does NOT strip the editor bridge - the packaged .vrgproj keeps
`EditorExtensionAssemblies`, and a subscriber who lacks that DLL cannot open the
project at all. Remove it first (finish_and_publish does).

From `VRage.ContentPipeline.dll`, in
`ValidateProcessingFeature.ParallelValidateProcessingState`. It fires when

    result.PreImportData is PreImportData.Success { OutdatedDependencies.Count > 0 }

The dependency set is **transitive**, from

    GetTransitiveReferencesFrom(assetFile.AssetID, {AssetReferenceType.Dependency})

and a GUID counts as outdated when the stored hash differs from the file's
current hash **or when the GUID is absent from DependenciesHashes altogether**.
So a hand-written .meta listing only direct dependencies manufactures this error.
An unresolvable dependency reports "import failed" instead.

The validator also waits only `TimeSpan.FromSeconds(1)` per asset import.

— that is, an asset's dependencies hash differently from what its `.meta`
records. For a `.planetcubemap` the dependencies are the six face PNGs.

There is an official suppression, and it is deliberately hidden:

    private bool ShouldReport(ProcessingErrors ignoredErrors, ProcessingErrors current, ...) {
      if (assetFile.Project.VRageProject.Data.EnableIgnoreProcessingErrorFlags)
        return !ignoredErrors.HasAnyFlag(current);
      return true;
    }

`EnableIgnoreProcessingErrorFlags` is a bool on `VRageProjectData` marked
`[HideInInspector]`, so it never appears in the editor UI. With it set, an
asset's `.meta` can list the error in its `IgnoredErrors` field, which is already
present on every meta as `"IgnoredErrors": "None"`.

`ProcessingErrors` is a flags enum:

    None=0  FilesHashMismatching=1  FilesDependenciesHashMismatching=2
    OutputsNotMatching=4  ImportFailed=8  ProcessingUnsuccessful=16
    ProcessorNotActual=32  NotRespectedDetachedState=64
    ProcessingProblemsFound=128  FilesPatchingRequired=256

This suppresses the symptom rather than fixing the cause.

**What the publisher does differently.** `VRAGE3.ModHUB.dll` builds a
`PublishPreparationProjectLoadingSetup` that:

- pushes the project with `ignoreCaches: true`, so nothing cached is trusted;
- loads with `useFileWatcher: false`;
- constructs a **fresh** `AssetProcessingUtilities` with
  `DefaultProcessorSettingsProvider`, whose `TryGetSettings` returns false for
  every type — whereas the editor uses `ProjectContextProcessorSettingsProvider`,
  which layers processor settings from the asset's own `.meta` and every parent
  folder's `.meta`;
- registers exactly three validations: `ValidateProcessingFeature` (with
  `IgnoreLooseOutputFilesDuringValidation = true`), `ValidateProjectItemsFeature`
  and `ValidatePngColorProfilesFeature`.

Note also that `ParallelValidateProcessingState` waits only **one second** for
each asset's import (`WaitBlocking(TimeSpan.FromSeconds(1))`); if it times out,
`result` is null and that asset is skipped entirely rather than reported.

**What has been ruled out.** The settings-provider difference is real in code but
does not by itself explain a failure on a project whose metas carry no processor
settings — and measured on two real mods, none do; their metas are structurally
identical to vanilla's. File hashes were also checked directly: recomputing
base64(MD5(bytes)) for every asset and every processed output gives 84 of 84
matching on vanilla Verdure, and on both of the user's mods every hash matches
with nothing missing. `DependenciesHashes` are present and the right shape too
(planetcubemap 6, comptex 2–3, cubemap 13+), matching vanilla.

So everything checkable offline is consistent. That points at state *at publish
time* rather than at anything wrong in the committed files — most likely an asset
changed after the editor last processed it, or a `Content/` output regenerated
between load and publish.

**The diagnostic to run when it happens:** `audit_project(project,
check_hashes=True)` immediately after a failed publish, and capture the full
error text — the validator names the failing assets, and that name plus the hash
report identifies the file in one step. `read_app_log(app='modhub',
contains='publish')` has the HUB's side of it.""",
    },

    "mod-project-layout": {
        "title": "How a mod project is laid out",
        "summary": "Assets are what you author; Content is build output.",
        "body": r"""    MyMod.vrgproj                     project file
    ModProject.modhub-metadata        publish metadata
    thumb.jpg                         store thumbnail
    Assets/                           SOURCE — everything you author
      <Thing>/
        <Thing>.def                   e.g. TriplanarSingleMaterialDefinition
        <Thing>VoxelMaterialDefinition.def
        <Thing>VoxelRenderMaterialDefinition.def
        <Thing>_Y_Near_Albedo.png     and AO, Height, Normal, Roughness, Metalness
        <Thing>_y_near_cm.comptex     packing recipes
      Override of <Vanilla>.partialdef   how you patch vanilla content
    Content/                          BUILD OUTPUT — generated, do not hand-edit
      *.dds, *.def, contentcache.vrb, definitionsets.vrb

Every source file has a sibling `.meta` carrying its AssetID GUID, the processor
that handles it (`P_PNG`, `P_PLANETCUBEMAP`, …), content-file hashes and
`IgnoredErrors`. Asset processors run at project *load*, not at build, so after
editing files outside the editor the project has to be reloaded for the metadata
to catch up.""",
    },

    "g-screen": {
        "title": "Why a perfectly valid block never appears in the G screen",
        "summary": "The tile chain, the computed BlockKind.Blocks list, and the silent filter.",
        "body": r"""The G screen is built from definitions, in this order:

    CategoryDefinition -> SubcategoryDefinition -> BlockGroupDefinition (a tile)
        -> BlockKindDefinition (a kind) -> kind.Blocks (the blocks of that kind)

`BlockKindDefinition.BlockGroups` points up to the group, the group's
`Subcategories` entry points to the subcategory. All of that is ordinary
serialized data and easy to get right.

The trap is `BlockKindDefinition.Blocks`. It is `[NoSerialize]`: a
`BlockKindDefinitionPostProcessor` computes it at load time by scanning every
`EntityCompositeDefinition` for which

    clientServerInfo.IsServer(composite)
      && composite.TryGetDefinition<CubeBlockComponent, CubeBlockDefinition>()
           is CubeBlockDefinition d
      && d.BlockKind == thisKind

and `GScreen.BlockGroupTileModel` then keeps only `group.BlockKinds` entries with
`k.Blocks.Length > 0`. A kind with an empty `Blocks` list is dropped **without
any log line** - the block is simply absent while validation says
"No invalid assets".

`IsServer(composite)` is true only when all three exist:

    1. a PrefabBindingDefinition whose ServerComposite is that composite,
    2. a ClientPrefab that really is a PrefabDefinition,
    3. a PrefabDefinition whose `Composition` is that composite.

Practical consequences:

- A `CubeBlockDefinition.BlockKind` guid is the whole link. If it is null or
  points elsewhere, the kind stays empty. Vanilla templates set it in
  `WeldersPowerableBlockDefinition.partialdef`-style base definitions.
- The post-processor only sees what is loaded. Build the prefab and the
  compositions **before** the definition set is generated, otherwise the kind is
  written with zero blocks and the game has nothing to show.
- The editor's `Create Prefab > Blocks > Breakable > Welder` (and Ion Thruster)
  templates create no BlockKind, no BlockGroup and no recipe. A copied block
  inherits the vanilla kind and shows up inside the vanilla tile. Give it its own
  kind + group + recipe when it should have its own tile.
- `BlockGroupDefinition.BlockKinds` is normally empty in files; the reverse index
  is filled at runtime. Do not treat an empty list as the bug.

Verify it in the running editor instead of guessing: read the kind definition and
count `Blocks`, `BlockGroups`, and the group's `Subcategories`. Zero blocks with
a correct `BlockKind` means the prefab/composition side is broken, not the UI.
""",
    },

    "composition-tags": {
        "title": "Composition TagSlots: the crash that looks like a grid bug",
        "summary": "Wrong tag mappings kill the entity at spawn and surface as 'Dead block in add'.",
        "body": r"""In an `EntityCompositeDefinition` every component dependency is resolved
through `TagSlots`: a dictionary from a dependency slot name to a component key
inside the same composition. `EntityAllocator.InitDependencies` walks the
components, looks the slot name up, and assigns the component instance to the
field.

If the mapped component does not implement the field's interface, allocation
throws and the block entity never becomes alive:

    ArgumentException: Object of type 'X' cannot be converted to type 'Y'
      at EntityAllocator.InitDependencies

The grid then reports `Assertion Failure: Dead block in add`
(`CubeGridComponent.CommitBlockChangesImpl`), and a `NullReferenceException` in
`Scene.Archetype.TypeIndex` may follow. **The grid assertion is a symptom**; the
real line is one second earlier:

    Error: Exception raised during NetworkStory:
      EntityBundleInitException: Bundle failed to initialize (Failed to allocate
      <composite guid> (<name>))
     ---> ArgumentException: Object of type '...' cannot be converted to '...'

Typical damage: copying a block template and swapping components makes the
editor rewrite `TagSlots`, so a single component (often the integrity tool) ends
up mapped to every slot. Real examples seen in a Welder-derived block:

    IntegrityToolComponent -> IBackpackItemConverter   (does not implement it)
    SphereShapeEntityDetectorComponent -> IToolOriginProvider
        (only AreaIntegrityToolEntityDetectorComponent implements that interface)

Rules that keep it working:

1. Copy the template's `TagSlots` block verbatim; do not hand-write it and do not
   let the editor "fix" it after swapping components.
2. Every value must be a component key that exists in the same composition and
   whose type implements the interface the slot names.
3. A server composition and its client composition are different: a slot that is
   valid on the server can be wrong on the client and vice versa. In the observed
   project the server was correct and the client composition was the one that
   crashed.
4. Extra slots are not harmless. A slot named after a provider interface is used
   by the allocator even when the vanilla block does not declare it.

Check before launching the game: resolve both composites and print, for each
tag, the target component type; then diff the tag set against the vanilla block
of the same family. Slots that exist only on the mod side are the suspects.

**Adding or removing a component is a two-file edit.** The composition's
`Keys` list and the prefab's `_entity.ObjectBuilders` list are the same parts in
the same order, so both must grow or shrink together:

    composition:  Keys += <new key>
                  Changed += Insert at Index = len(Keys)-1
                     Value { "Definition": <guid or null>, "Type": "Game2:...Component" }
    prefab:       _entity.ObjectBuilders.Keys += <the same key, same position>
                  Changed += Insert at the same Index, Value: null   (no builder data)

The two `Keys` lists are the same GUIDs in the same order - the composition names
the parts and the prefab carries their saved state. Generating a *different* GUID
for the prefab half is the classic mistake and produces the type-mismatch error
below; check `composition.Keys == prefab.ObjectBuilders.Keys` after the edit.

Miss the prefab half and the editor reports

    Mismatch in Entity parts OBs:13 IDs:15 Tags:15 Types:15 Defs:15

Insert in the wrong position and it reports a type mismatch at that index

    ObjectBuilder ...IntegrityToolObjectBuilder type doesn't match expected
    ...BlockPermissionsObjectBuilder

Both are index errors, not definition errors. Do the edit with one script that
touches both files and computes the index from the current `Keys` length.

**Two ways this goes wrong even with the right indices.**

1. A `$DeltaEncoded` list inside a partialdef's `Manipulator` needs its `Keys`
   array populated. Writing `"Keys": []` and then `Changed: [{Kind: Update,
   Index: 2, ...}]` makes the reader apply index 2 to an empty list:
   `JsonSerializationException ... Index was out of range` while the project
   loads. Copy the base's key list, never invent an empty one.
2. `Content/*.def` files are **compiled outputs**, not assets. Copying one into
   `Assets/` and pointing the project at it can take the whole editor down on
   load (observed: hard crash, no dialog). Take the shape from the templates or
   rebuild the definition field by field; use Content only to read values.
""",
    },

    "material-swap": {
        "title": "Working-state material swap: BlockMaterialSwapper",
        "summary": "How a block glows only while it works, and the two errors the validator raises first.",
        "body": r"""A block changes its look while `FunctionalBlockComponent.Working` is true
through one client-only definition plus one client component:

    BlockMaterialSwapperDefinition          (Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Render)
      WorkingReplacementModels:   ["{G}<model asset guid>", ...]
      WorkingReplacementsMeshParts: [{"$Key": "<material name>", "$Value": "<material def guid>"}]

    BlockMaterialSwapperComponent           Definition = the above, client composition only

`WorkingReplacementsMeshParts` keys are **material names as they appear in the
model**, so `EmissiveOff` covers every part modelled with that material. Fracture
parts need their own keys, named `<FractureId>-<Material>` (e.g.
`Fracture_10-EmissiveOff`).

Block material GUIDs on 4.0.0.3165:

    EmissiveOff        d2648963-ef2b-442d-af7b-ee3d79dad677
    EmissiveColorable  5ca7a862-77ab-45eb-982c-16c384abe801   <- glows in the painted colour
    EmissiveWhite      8ffced10-c911-4a5a-921f-075ee31ca2cc
    EmissiveGreen      78f2cbaa-112e-4068-99e7-c146d4da58f2

Two traps, both from the validator:

1. `Meshparts are set, but no model. No swapping will be performed.` - the
   definition needs `WorkingReplacementModels` to list every model asset whose
   parts may be swapped: the main `Model`, `DamagedModel` and `FractureModel` from
   the block's `BlockModelDefinition`, `{G}` prefixed.
2. `Mismatch in Entity parts OBs:14 IDs:15` - adding the component to the client
   composition also needs its ObjectBuilder key in the client prefab (the
   two-file rule in `composition-tags`). The prefab half is easy to forget because
   the editor still runs; only validation complains.
""",
    },

    "localization": {
        "title": "Text keys: .loc-texts, the Core set, and the two silent failures",
        "summary": "How custom names are shipped, and why the editor rejects keys that exist.",
        "body": r"""UI names are localization keys, not strings. `UIData.Name`,
`BlockKindDefinition.Name`, `.Description` and `BlockGroupDefinition.Name` all
hold a key; an unknown key makes the asset invalid with

    Unrecognized value '<key>'

Texts are shipped as a `.loc-texts` JSON asset, one file per culture:

    Assets/Localization/en-US/MyMod.loc-texts   { "MyMod_Name": "Hello", ... }

plus an `Override` partialdef of the culture definition that appends it as a
resource:

    BaseDefinition: <guid of the en-US CultureInfoAssetDefinition>
    PartialDefinitionKind: Override
    Manipulator: Resources $DeltaEncoded -> Insert { ContentId, Asset: "{G}<loc-texts asset id>" }

**This works, but only in exactly one configuration** (verified in game: the block
showed its own name and description):

1. `Assets/Localization.meta` carries
   `{"$Type": "...DefinitionSetItem", "DefinitionSetName": "Core"}` - the folder
   is a Core set root, because the base `CultureInfoAssetDefinition` lives in
   Core and a partialdef must sit in the same set as its base.
2. `.vrgproj -> $Value.DefinitionSetNames` is `["World", "Core"]`.
3. The `.loc-texts` sidecars carry the AssetID their `Override` partialdefs
   reference, with `P_DEFAULT` and correct hashes.
4. **No other enabled mod declares Core.** Two projects pushing a Core set is
   what produces
   `InvalidOperationException: The set Core cannot be mounted ... already pushed
   to DefinitionManager` followed by `Projects popped out of order` on shutdown.
   A scratch/test copy of the mod is the usual culprit - keep only one project
   with Core per world.

The two failure modes seen while learning this:

- Override in **World**: `DefinitionSetCollectionGenerator` throws
  `... are not in the same definition set ('Core' and 'World')`. The editor build
  swallows the exception, so `definitionsets.vrb` silently keeps its old contents
  (see `stale-content`) and new definitions never reach the game.
- A second Core from another mod: world load aborts with the mount error above,
  the mod's definitions never load, and the block is simply absent from the G
  screen.

Practical checks before blaming the texts: run the definition-set collection in
the editor and confirm it lists **both** sets (`World 28, Core 4`); if Core is
missing, the folder meta lost its `DefinitionSetItem` (the editor rewrites the
sidecar) or the project no longer mounts Core.

Asset metadata for `.loc-texts` is `P_DEFAULT`, not `P_DEF`. `authoring.refresh_meta`
rewrites the whole sidecar with `P_DEF` and empty outputs, which the pipeline then
refuses ("Can't translate a resource handle ... to file handle"). Keep the original
meta and patch only `FileHash`, `ContentFiles.MainOutput.FileHash` and
`AssetHash` with `base64(md5(bytes))`.

Vanilla keys ("ToolWelder", "WelderDesc") are an acceptable placeholder while
testing: they already exist, so validation stays green, but the block shows the
vanilla name.
""",
    },

    "mod-scripting": {
        "title": "Mod C# scripts run in the shipped game only with the -loadScripts launch argument",
        "summary": "Verified 2026-11-04: GameApp registers the mod script compiler only when -loadScripts is passed; publishing does not ship Scripts/.",
        "body": r"""CORRECTION (2026-11-04, verified in game 4.0.0.3165):
`Keen.Game2.GameApp` calls `AddScripting(engineBuilder)` only `if (args.Contains("-loadScripts"))`.
With that argument the game compiles `<mod>/Scripts/{Simulation,Client}`, loads
`<Project>.Simulation.dll` and runs its jobs. Proof: a static job marked with a `JobGroup`
subclass (`[After(typeof(Keen.Game2.Simulation.Physics))]`) wrote a line every 600 steps.
Launch through Steam (the exe hands off to Steam and drops arguments otherwise):
`steam.exe -applaunch 1133870 -projectPaths:"<mod>.vrgproj" -globalProjectDirs:"<Mods>;<SDK>\GameData" -loadScripts`.
Jobs are found by `JobReflectionIndexer.IsJob` (attributes deriving from `JobGroup`);
a bare `[ModuleInitializer]` never fires because nothing touches the types.
Limits: players must add `-loadScripts` to their launch options, and the editor's
`ProjectPublishHelper.CopyProjectAsync` copies only Assets, Content, Worlds and the
.vrgproj, so `Scripts/` is not in a published mod.

The older measurement below was made WITHOUT -loadScripts and is kept for history.

The SDK ships a script compiler (`VRage.Scripting`, `GameScriptCodeProvider`,
`ModCompilationDescriptor`), `VRageProject.Scripts` points at `<mod>/Scripts`, and
`LoadedScriptsProviderComponent.ConfigureSession` adds jobs from compiled
assemblies. It is easy to conclude that mod code runs. Measured on 4.0.0.3165,
it does not.

The measurement, repeated twice:

    Scripts/Simulation/<Name>/Probe.cs with a [ModuleInitializer] that appends a
    timestamped line to a file on disk
    -> game launched with -projectPaths:<mod>.vrgproj
    -> log shows "Pushing Project <mod>" and "Registering worlds from <mod>"
    -> the file is never created; the log has no compile line and no error

Putting the same file under `Content/Scripts/Simulation/...` changes nothing.
The editor is different: with the startup hook in place
(`Tools/EditorScriptRefsHook`) it does compile scripts, which is why code can
look validated and still never execute in game.

Consequences for design:

- Definition-only mods are the shipping shape today: vanilla components plus
  their definitions, tuned by data. A wide-area welder, a faster tool, custom
  recipes, models and UI text all work this way.
- Do not put a mod script type into a definition. It fails before any of the
  above matters: the definition loader cannot resolve
  `MyMod:Namespace.Component`, and that failure takes down the whole definition
  set load ("Unable to locate a type named ...").
- Behaviour that needs code (target selection, grinding rules, claims,
  per-block state) has to wait for Keen, or be expressed with vanilla components
  and their configuration.
- Keep `Scripts/` out of the project until scripts actually run: a root
  `Scripts` folder makes the editor compile them at load, which needs the hook
  and otherwise blocks the project from opening.

Verify before designing around scripts: drop the probe in, launch with
`-projectPaths`, and look for the file. If it is missing, plan a data-only mod.
""",
    },

    "stale-content": {
        "title": "An orphaned file in Content/ makes the build skip the definition set",
        "summary": "Silent set-generation failure: new definitions never reach the game.",
        "body": r"""Deleting or moving a definition asset out of `Assets/` does **not** delete its
compiled copy from `Content/`. That leftover is enough to break the whole build in
a way nothing reports:

- the set generator walks the project and finds an output whose source is gone (or
  a partialdef whose base moved to another definition set),
- it throws inside `DefinitionSetCollectionGenerator.CollectDefinitionSetCollection`,
- `editor_build` / GenerateCacheAndDefinitionSet catches and ignores it,
- `Content/definitionsets.vrb` keeps its **previous** contents; its timestamp does
  not move.

Everything downstream then lies: `editor_validation` still says "No invalid
assets", the editor still shows the new definition (it reads Assets), and the game
loads the old set. The symptom appears only at world load:

    SerializationException: Cannot locate value for definition <new guid>
    from provided DefinitionSerializationContext
    -> Loading of save '<world>' ended with exception

How to see the exception the build hides: call
`DefinitionSetCollectionGenerator.CollectDefinitionSetCollection()` yourself in
`editor_eval` and print the exception, or read the built set and look for the new
GUID. `Tools/scripts/editor_definition_sets.cs` does exactly that; flip its `SAVE`
flag to write the rebuilt set without waiting for a build.

Fix and prevention:

1. After removing or relocating an asset, delete the matching file under
   `Content/` before building (`Content/Localization/...` in the observed case).
2. Rebuild, then confirm `definitionsets.vrb` changed: compare its modification
   time and search its bytes for the GUID of the newest definition.
3. Treat "world fails with Cannot locate value for definition X" as a packaging
   problem first - the definition exists in Assets and Content, it is just not in
   the set.
""",
    },

    "stale-sdk-assets": {
        "title": "The SDK's Vanilla assets are older than the game - do not copy them",
        "summary": "Old bundle versions, renamed types, and what prevents migrations from saving you.",
        "body": r"""Files under `GameData/Vanilla/Assets` (and the mirrored
`GameData/Vanilla/Content`) are stamped with the bundle version they were authored
against, often `2.2.0.x`, while the installed game and editor are `4.0.0.x`. The
runtime applies **name migrations** to those files, so the game loads them fine
and nothing looks wrong.

Copy such a file into a mod and re-stamp its `$Bundles` to the current version and
the migrations stop applying. The editor then refuses the asset with

    Unable to locate a type named Game2:...Tools.Voxels.DrillDamage.DrillDamageComponent

because that type no longer exists under that name. The same happens if a partial
definition carries an old type name in an `Insert` value.

Consequences:

- Author new definitions against the current **templates**
  (`GameData/Vanilla/Assets/Templates/...`), which are stamped with the current
  version and use current type names.
- Use the compiled `Content` of the game to *read* what vanilla does, not as a
  source to copy wholesale.
- If you must fork an old file, either keep its original `$Bundles` version so the
  migrations still run, or translate every stale type name by hand.
- A block template ("Create Prefab > Blocks > Breakable > Welder") is the safe
  starting point for the composition; the vanilla 400 block's composition is not.
""",
    },

    "editor-bridge": {
        "title": "Driving the editor through the MCP bridge, and when it goes deaf",
        "summary": "Install, launch, the reload rule, and what a dead listener looks like.",
        "body": r"""The bridge is a plugin inside `VRage.Editor.exe` listening on
`http://127.0.0.1:8765` with a bearer token file. It only loads when the project
is launched with it installed:

    install_bridge(project)   # adds SE2McpBridge.dll + its search path to the .vrgproj
    launch_editor(project)    # VRage.Editor.exe --project ... --globalProjectDirs ...
    editor_status()           # poll until connected == true (~10-40 s)

The bridge comes up long before the project finishes loading; `editor_project()`
reports `loaded: false` until the definition manager is ready, which can take
another 30-60 s.

**Known failure:** writing project files while the editor has it open kills the
bridge's HTTP listener while the editor process keeps running. Symptom is
`connection refused` on 8765 with `VRage.Editor` alive and responsive. There is no
in-editor recovery - kill the editor and relaunch. Batch file writes, then restart
once.

Ordering that works:

    write definitions / assets
    restart editor, wait for editor_project().loaded
    editor_build()            # GenerateCacheAndDefinitionSet, writes Content/*.vrb
    editor_validation()       # per-asset problems, the same list the editor shows

`editor_validation` only sees assets the pipeline processed; "File missing from
content" means the build has not produced an output yet. Definition post
processors (block kinds, block sizes, progression) run on load, so a stale editor
session can report an older linking state than the current files - always rebuild
and re-read before concluding that data is wrong.

Before publishing run `uninstall_bridge(project)`: the packaged `.vrgproj` must not
reference the bridge, or subscribers without that DLL cannot open the project.
""",
    },

    "block-tuning": {
        "title": "Making a copied welder behave like a wide-area repair block",
        "summary": "Range and repair speed live in two definitions; never override the vanilla ones.",
        "body": r"""A Welder-derived block inherits three numbers that decide how it feels:

    SphereShapeEntityDetectorDefinition.QueryRadius   default 2.5 m
    IntegrityToolDefinition.IntegrityChange           default 1.25 (per 10 ticks)
    IntegrityToolDefinition.MaxInteractionDistance    default 100 m

The sphere detector is the area search: it queries entities around the block's
`QueryDummy` (dummy type ToolDetection, `fb621cb9-...`), so the model needs a
dummy of that type where the block should measure from. The integrity tool then
welds what the area detector reports.

Scale them by authoring **your own** copies, not by overriding vanilla:

    Nanobot_SphereShapeEntityDetectorDefinition.partialdef
        BaseDefinition <vanilla welder detector guid>, Copy,
        Manipulator { Guid: <new>, QueryRadius: 30.0 }

    Nanobot_IntegrityToolDefinition.partialdef
        BaseDefinition <vanilla welder integrity tool guid>, Copy,
        Manipulator { Guid: <new>, IntegrityChange: 5.0 }

then repoint the composition's `SphereShapeEntityDetectorComponent` and
`IntegrityToolComponent` entries at the new GUIDs (both server and client
composition, if they reference them).

Why copies: an `Override` partialdef of `Welder400IntegrityToolDefinition`
changes **every welder in the game**, silently. An empty `Override` is still a
global patch and should be deleted.

Recipe for a wider, faster variant of an existing block:

1. Read the two vanilla definitions and note the fields above.
2. Write copies with new GUIDs and the values you want (`QueryRadius` 30-50,
   `IntegrityChange` 4-6).
3. Repoint the components in the composition(s); check the tags still resolve.
4. Rebuild, then read the loaded definitions back and confirm the values and the
   component wiring (`SphereShapeEntityDetectorComponent -> <your guid>`).
5. In game: damage a block 20-30 m away and confirm it repairs; the inventory or
   the conveyor network still has to supply the components.

A visual/physics note: the block does not "reach" further by moving anything -
only the query radius changes. If it stops at short range, confirm the model's
ToolDetection dummy exists and that the area detector component is present.

**Three more fields decide how the block plays, and two of them default to
nothing.**

    CubeBlockDefinition.PCU                     inherited; 250 on welder-family
    CubeBlockDefinition.ConsumedResource        { Type: <Electricity guid>, Amount: kW }
    CubeBlockDefinition.ConsumptionPriority     { Priority: 0-10 }
    InventoryComponent -> InventoryDefinition   MaxMass in kg

The welder template ships `ConsumedResource = { Type: Electricity, Amount: 0 }`,
i.e. the block repairs for free. That is almost never what you want, and nothing
warns about it - the block works perfectly, it just draws zero power. Set an
amount (120 kW is a reasonable wide-area tool) and keep `Priority` at 8.

Inventory capacity is `MaxMass`, not a stack count, and it lives in the
`InventoryDefinition` the `InventoryComponent` points at. To grow it, write a
`Copy` of the vanilla inventory definition with a new GUID and a higher
`MaxMass`, then repoint the component (composition index of
`InventoryComponent`) - the tags keep pointing at the component key, so they
need no change.

`PCU` is a plain field on the block definition; raise it with the block's power,
not with its usefulness.

**A tool block has no idle/active split.** Measured on 4.0.0.3165:

    vanilla Welder400        ConsumedResource.Amount = 0     (welders are free)
    refinery                 ItemConverterDefinition.ConsumedResource = 3200 kW

`PowerableBlockComponent` draws the block-level `Amount` **constantly while the
block is enabled** - the control panel then shows max input == current input, and
turning the block off is the only thing that drops it to 0. Production blocks
behave differently because their `ItemConverter` asks for power only while it
converts (`ItemConverterDefinition.ConsumedResource` is a ceiling, not a floor).

There is no data-level way to tie a tool's draw to its work: a per-block "mode"
toggle is component state, and making power follow it needs a mod component,
which does not run in this build (see `mod-scripting`). Pick a flat number while
the block is on, or leave it at 0 like vanilla.

**Terminal labels are shared vanilla keys.** The "Mode selection" switch on a
welder comes from `TerminalScreenIntegrityToolModeSelection` ("Mode selection" /
"Mod seçimi"), used by every integrity tool. A mod can rename it only by
overriding that key in its culture override, which renames it for vanilla
welders and grinders too - usually not worth it. New rows (range, colour filter,
priority) are component properties surfaced by the terminal; they need a block
component with synced properties, so they are code, not data.
""",
    },

    "inventory-logistics": {
        "title": "Making a block pull components from the conveyor network",
        "summary": "ItemRequester + InventoryStockpile, the two-file rule, and the tags they need.",
        "body": r"""A welder (or any block that consumes items while working) takes those items
from two places: its own inventory, and the conveyor network through an
`ItemRequesterComponent`. The block templates under `Templates/Blocks/Breakable`
ship the small 13-component composition **without** it, so a block cloned from
them welds only from its own inventory - and stops the moment that is empty,
with no error.

Two components have to be added to the server composition:

    ItemRequesterComponent
        Definition: null
        Type: Game2:Keen.Game2.Simulation.WorldObjects.Items.ItemRequesterComponent

    InventoryStockpileComponent
        Definition: 1d389292-3075-4237-a278-0aad0191d493   (vanilla welder's; verify)
        Type: Game2:Keen.Game2.Simulation.WorldObjects.Items.InventoryStockpileComponent

The edit is the two-file rule from `composition-tags`, and the keys matter:

    composition  Keys += [k_req, k_stock]
                 Changed += Insert at len-2 {Definition: null, Type: ...ItemRequesterComponent}
                          + Insert at len-1 {Definition: <stockpile def>, Type: ...InventoryStockpileComponent}
    prefab       _entity.ObjectBuilders.Keys += [k_req, k_stock]   <- SAME GUIDs, same order
                 Changed += Insert at the same indices, Value: null

Tag slots to add in the composition (keys are the ones above):

    ItemRequesterComponent      -> k_req
    IItemRequester              -> k_req
    InventoryRequester          -> <inventory component key>
    InventoryStockpile          -> <inventory component key>
    InventoryStockpileComponent -> k_stock

Verification before touching the game: the resolved composite should report the
new parts (`components: 15` for a 13-part template block), every tag above should
resolve to a component of that type, and the allocator preflight should come back
empty for server and client. Then test in game with the block's inventory empty,
a container of components behind a conveyor, and a damaged block within range -
it should repair using the conveyor's items.

Debug the prefab half with `composition.Keys == prefab.ObjectBuilders.Keys`.
When those two lists differ, the editor fails at load with either
`Mismatch in Entity parts OBs:...` or a type mismatch at the first differing
index, and neither message mentions the real cause.
""",
    },
}


def get(topic: str = "index") -> dict[str, Any]:
    """Look a topic up forgivingly: exact id, then letters-only, then title."""
    raw = (topic or "index").strip().lower()
    if raw in ("index", "", "list"):
        return {
            "topics": {k: v["summary"] for k, v in TOPICS.items()},
            "note": (
                "These are measured reference facts. For the procedure to build "
                "something — which tool in what order — call mod_recipes."
            ),
        }
    if raw in TOPICS:
        return {"topic": raw, **TOPICS[raw]}

    squashed = "".join(c for c in raw if c.isalpha())
    for key, value in TOPICS.items():
        if "".join(c for c in key if c.isalpha()) == squashed:
            return {"topic": key, **value}
    for key, value in TOPICS.items():
        if raw in value["title"].lower() or raw in key:
            return {"topic": key, **value}

    return {"error": f"No topic '{topic}'", "available": sorted(TOPICS)}
