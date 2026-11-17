# Water

Water in SE2 is two completely different systems that share a name, and almost
every performance complaint comes from using the expensive one to do the cheap
one's job.

| | **Planetary water** | **Water domain (massfill)** |
|---|---|---|
| what it is | ocean tiles: a water level per surface tile | a simulated grid of fluid cells |
| stored per unit | `WaterLevelUnscaled` — one distance from the gravity centre | `WaterCell` — density, solidness, flow, gravity, wall flags… |
| LOD0 unit size | a tile covering terrain | **0.5 m per cell** |
| cost | flat; it is a surface, not a volume | cubic in the volume filled |
| how you get it | a definition on the planet | the F12 debug menu, or a water tool |
| what it is for | oceans and seas | ponds, floods, ship interiors, water you interact with |

If you want an ocean on a planet, you want planetary water. The debug menu's
massfill is not a slower way to get the same thing — it is a different thing.

## Why massfill on a planet destroys performance

The shipped massfill component, `Assets/System/Water/WaterDomain/WaterDomainMassfill.def`:

```json
{
  "$Type": "VRage:…Water.Components.WaterDomainMassfillComponentDefinitionObjectBuilder",
  "$Value": { "Radius": 100000, "MaxCells": 10000000 }
}
```

`MaxCells` is ten million. `Migrations_2_3_0_343` records that **a LOD0 cell is
0.5 m**, so ten million of them is `10⁷ × 0.125 m³ = 1.25 × 10⁶ m³` — a cube
**108 m on a side**. That is a lake, and it is the entire budget.

A 100 km-radius planet's ocean shell, at the same cell size, would need on the
order of **3 × 10¹⁶ cells — about a billion times the cap.** The request is not
slow, it is impossible; what you actually get is the cap being spent near you,
re-simulated every tick.

And every one of those cells is a full fluid cell. From the SDK's own
documentation of `Keen.VRage.Water.WaterCell`:

- `Density` — total water in the cell, relative to cell size
- `EffectiveDensity` — density adjusted by solidness
- `DensityWhenLastActive`, `LastActiveVelocity`
- `Solidness`, `RawSolidness`, `MicroFlags` — and `HasMicroSolidness`, "if the
  cell is a reference to 8 smaller cells in a trench coat"
- `Flow` and `Gravity`, both **kept in world space** (three floats each)
- `DomainInfluence` — Manhattan distance field to the nearest solid cell
- `BlendDistance`, `RadiusBlend`, `WallFlags`, `AllowRenderBoost`

That is roughly 60–80 bytes of state per cell before any grid, mesh or GPU
buffer. Ten million cells is on the order of **0.7 GB of cell state alone**, all
of it touched by the simulation. A measured session that did this reported
23.6 GiB process memory and 3.34 s of accumulated GC pause.

**So: never massfill an ocean.** Massfill is sized for a pond.

## How planetary water is actually wired

```
Planet_ClientComposition.partialdef ─┐
                                     ├─ Components → Insert
Planet_ServerComposition.partialdef ─┘   { "Type": "VRage:Keen.VRage.Water.Components.PlanetaryWaterComponent",
                                           "Definition": <guid> }
                                                          ↓
                            PlanetaryWaterComponentDefinition
                                ├─ WaterLayers → PlanetaryWaterLayersDefinition   ← APPEARANCE ONLY
                                └─ WaterBiomes → PlanetaryWaterBiomesDefinition   ← per-biome water level
```

Four things about this that are easy to get wrong:

**1. The component goes in *both* compositions.** Client and server. The server
creates the water; the client renders it. One without the other gives you half a
feature.

**2. `WaterLayers` does not set the water level.** The SDK documents it as
*"Define how water **looks** at different locations"*. The layers are shells
around the planet, "structured sequentially starting at the planet center", each
with a `Thickness`, a `Blending` and a list of `Latitudes` whose `Profile` points
at a `WaterVisualProfileDefinition`. Vanilla's two stacks both total exactly
`1.09` — EarthLike as one shell, Verdure as four. It is a lookup for which
visual profile applies where, nothing more.

**3. The water surface radius comes from `PlanetGeneratorDefinition.ZeroGround`.**
Sea level is `R × (1 + ZeroGround)`, in the same radius fractions as
`HillParams`. The heightmap texel that sits exactly at the waterline is:

```
waterline = (ZeroGround − HillParams.Min) / (HillParams.Max − HillParams.Min) × 65535
```

**The coastline is a contract.** Land must encode strictly above that value and
ocean strictly below it. A single land texel at or below it leaks water inland.

**4. `WaterBiomes` is how you get lakes.** `PlanetaryWaterBiomesDefinition` holds
`BiomeHeights`, a list of `{ Biome, Height }` where `Height` is documented as
*"Planetary height of the biome"*. That is a per-biome water level — a mountain
lake is a biome with a water height above sea level, not a massfill. Vanilla's
only example leaves it `null`, so this is untrodden ground, but it is the
intended mechanism and the visual profiles are already there for it
(`MountainLakeVisualProfile`, `MediterrainLakeVisualProfile`,
`UndergroundLakeVisualProfile`).

## The state of water in the shipped game

Measured against SDK 2.3.0.2798, across all 17,643 indexed definitions:

- `PlanetaryWaterComponentDefinition` is used **exactly once** — by `EarthLike`,
  which is a **legacy VS1_5** planet.
- `ByblosWaterLayersDefinition` exists and **nothing references it**. Byblos is
  the VS3_0 water planet — `HillParams -0.3333…0.03333`, 91 % of its height band
  below sea level — and its water component was never connected.
- No VS2_x or VS3_0 planet wires planetary water at all.

So the engine side is finished and the content side is not. `VRage.Water` is
fully implemented — `PlanetaryWaterComponent` is a `GameComponent, IInSceneListener`
with `OceanLevelRadius`, `MaxWaterRadius`, `TryCreateOceanTile`,
`QueryOceanTiles`, `DecimateRegion`, `RestoreRegion` — and the sessions are
registered in `Assets/System/World.def`. Keen simply has not turned it on for
any modern planet.

That means a mod can wire it correctly and still see nothing, and the mod is not
at fault. Check the game log before assuming otherwise (below).

## Water is created by the server, and never by the editor

```
                          CanCreateGrids  CanUpdateSolids  ForbidWatergridCreations
ClientWaterSessionDefinition    false          false               true
ServerWaterSessionDefinition    true           true                false
```

The client session is forbidden from creating water. Only the server session
does, and **the editor runs no server session** — it previews assets. So:

> **Planetary water can never appear in VRage.Editor's Render View.**
> Testing water in the editor proves nothing, for a mod planet or for EarthLike.

The only valid test is in game. `WaterDomainComponent` is documented as
*"contains and simulates water grids"*, and it owns the planetary component:
`WaterDomainComponent.PlanetaryWater` is *"planetary water component owned by
this domain (ocean tiles on the planet surface)"*, with `OceanProxy` being a
*"proxy for overlapping procedural water from a parent planetary domain"*. None
of that machinery is stood up outside a running session.

## Diagnosing it from the game's own log

The game logs to `%APPDATA%/SpaceEngineers2/Temp/Logs`. The MCP server reads
them: `read_app_log(app='game', contains='…')`.

What to look for, and what it means:

```
Discovered local mod <guid> <path>            your mod was found at all
Initializing WaterSessionServerConfiguratorComponent   the water system started
Initializing WaterSessionClientConfiguratorComponent
WaterCoreConfiguration → "DisableRendering": false     water rendering is on
WaterLoddingAlgorithmConfiguration → "UseLegacy": false
```

The `*_Stats.log` beside it is the decisive one. It carries a `Water` section
under `GPU Water Stats` (`Particles`, `WaterMesh`), `Water:` entries in the
render memory pools, and — the part that actually answers the question — a
`Water:` line in the per-pass **draw** stats:

```
MainView[…]
  Mwm: 177
  Armor: 97
  Water: 1        ← water was drawn this frame
```

Zero water draw calls with the sessions initialised means the water system is
alive but has nothing to draw. Water draws present but no ocean visible means
you are looking in the wrong place — ocean tiles stream in near the viewer
(`RegionChanged`, `StorageRangeChanged`, `QueryOceanTiles`), so you have to be
close to the surface, not in orbit.

## Performance knobs, if you must have simulated water

These are configuration definitions, overridable with a partialdef:

| definition | field | effect |
|---|---|---|
| `WaterCoreConfiguration` | `DisableRendering` | stops drawing water; the sim still runs |
| `WaterLoddingAlgorithmConfiguration` | `UseLegacy` | switches the LOD algorithm |
| `WaterDomainMassfillComponentDefinition` | `MaxCells` | **the one that matters** — lower it |
| | `Radius` | massfill reach, 100 km by default |
| `WaterDomainDefinition` | `DefaultAbandonedWaterCountThreshold` | when stray water is dropped (1000) |
| | `DefaultAbandonedWaterDensityThreshold` | 1.9 static / 0.3 dynamic |
| | `DefaultAbandonedWaterSolidnessThreshold` | 0.5 |
| | `DynamicDomain` | domain follows a moving entity |

`GPUWaterGridRenderEntity.LodFlags` documents the render side: LOD in bits 0–4,
node type in 5–6, and a high-resolution flag in bit 7 — set means
`HIGH_GRID_RESOLUTION` (16), clear means `LOW_GRID_RESOLUTION` (8).

Lowering `MaxCells` is the honest fix for a laggy massfill. It does not make the
ocean work; it makes the pond affordable.

## Building an ocean, in order

1. **Set the height band first.** `HillParams` and `ZeroGround` in the planet
   generator decide where the water is. Compute the waterline texel with the
   formula above.
2. **Author the heightmap against it.** Below the waterline is ocean floor,
   above it is land, and nothing straddles it by accident. A useful sanity
   check is the fraction of texels below the waterline — Earth is 71 %.
3. **Author the water layers**, or copy vanilla's: a `Copy` partialdef of
   `VerdureWaterLayersDefinition` (`d287d35b-0e86-4c58-add9-fe38f992d721`)
   whose `Manipulator` contains only a new `Guid`. That is exactly what
   `ByblosWaterLayersDefinition` is.
4. **Write the `PlanetaryWaterComponentDefinition`**, pointing `WaterLayers` at
   it and leaving `WaterBiomes` null unless you want per-biome levels.
5. **Insert it into both compositions**, `_ClientComposition` and
   `_ServerComposition`, as a delta-encoded `Insert` at the end: add one fresh
   GUID to `Components.Keys`, then a `Changed` entry
   `{ "Kind": "Insert", "Index": <last>, "Value": { "Definition": <guid>,
   "Type": "VRage:Keen.VRage.Water.Components.PlanetaryWaterComponent" } }`.
6. **Reload the project in the editor and rebuild.** Asset processors run at
   project *load*.
7. **Test in game.** Not in the editor. Fly to the surface, not orbit.
8. **If nothing appears, read the game log** before changing anything — the
   answer is usually that the feature is off in this build, not that the mod is
   wrong.

## Reference files

```
Vanilla/Assets/System/World.def                             registers both water sessions
Vanilla/Assets/System/Water/ClientWaterSessionDefinition.def
Vanilla/Assets/System/Water/ServerWaterSessionDefinition.def
Vanilla/Assets/System/Water/PlanetaryWaterLayers/            EarthLike, Verdure, Byblos
Vanilla/Assets/System/Water/WaterVisualProfiles/             Ocean, lakes, space
Vanilla/Assets/System/Water/WaterDomain/                     domains, massfill, prefabs
Vanilla/Assets/System/Water/WaterGrid/                       the simulated grids
Vanilla/Assets/System/Water/SlimDomains/                     water inside ship grids
Vanilla/Assets/System/Creative Tools/Water Hand/WaterHand.def   the in-game water tool
Vanilla/Assets/Procedural/VS1_5/Planets/EarthLike/Data/EarthLikePlanetaryWaterComponentDefinition.def
```

The last one is the only working example of planetary water in the entire SDK.
Read it before writing your own.
