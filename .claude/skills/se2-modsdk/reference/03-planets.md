# Planets

## How a planet is wired together

```
PlanetGeneratorDefinition        HillParams, ZeroGround, MaxAltimeter, six heightmap GUIDs
  └─ heightmap cube map          6 × 16-bit greyscale PNG, colour type 0

PlanetBiomeMapDefinition         joins the two index maps
  ├─ BiomeMapDefinition
  │    └─ SurfaceBiomes[]        Key → engine-side GUID, NOT in GameData
  │         └─ Value → PlanetBiomeDefinition
  │                      ColorKey, OreRules, OresPerCubicKilometer
  └─ MaterialMapDefinition
       └─ PlanetMaterialMapDefinition   ColorKey
            └─ MaterialRules[] → PlanetMaterialPlacementRuleDefinition
                                   Layers[{Material, Depth}], Slope{Min,Max}

AtmosphereDefinition
PlanetEnvironmentRenderDefinition   names the CloudDefinition
PlanetOverlayDefinition             the CM/NAO cubemaps
VoxelPlanetRenderComponentDefinition  clipmap, overlay, spherization
PlanetInfoDefinition                ← without this the planet is unspawnable
```

Plus the prefab set copied from `Templates/Planets/PlanetWithAtmosphere`:
binding, `_Client`, `_ClientComposition`, `_Server`, `_ServerComposition`.

**In `SurfaceBiomes` the `ColorKey` is on the `Value` side.** The `Key` GUID
resolves to nothing anywhere in `GameData` — it is engine-side. Read the pair
the other way round and every ColorKey comes back null.

**Biome map and material map are different things.** The biome map drives ores,
flora, encounters and spawn rules; the material map drives what the ground is
made of. The biome map is coarse and the material map is rich: vanilla Byblos
has 4 biomes and 31 material ColorKeys.

**Cliffs are not encoded in the map.** Every placement rule carries its own
`Slope: {Min, Max}`, and one ColorKey can hold several rules, so the engine picks
the steep-slope variant itself. The map encodes terrain *type* only.

**Placement rules cross planet boundaries.** Byblos's material maps reference
Verdure's `CliffsSnowPlacementRule` and `SeaRocksPlacementRule`. A new planet can
reference vanilla rules directly instead of authoring its own.

**`UndergroundBiomes` carry no ColorKey**, so they cannot be painted. They are
depth layers, and vanilla puts only Nickel, Iron and InnerCore in them. Rare ore
is placed through surface biomes, which is why the biome map can steer it
geographically.

## `PlanetInfoDefinition` — the one that has no validator

```json
{
  "$Type": "Game2:Keen.Game2.Client.Debugging.Screens.Voxels.PlanetInfoDefinitionObjectBuilder",
  "$Value": {
    "Guid": "…",
    "Name": "Earth",                                    the label in the debug menu
    "Preview": "ab7795e6-b1be-44df-9f05-d002ff859409",  shared PlanetPreview_Server
    "Spawn": "<the planet's *_Server prefab GUID>"
  }
}
```

A planet can validate clean, build clean and still be impossible to spawn,
because nothing references `PlanetInfoDefinition` — so nothing detects that it is
missing. Shared previews: `PlanetPreview_Server`
`ab7795e6-b1be-44df-9f05-d002ff859409` (VS2_2 and later),
`PlanetPreview_Client` `ea21c45c-178d-4ac6-8445-7cad4c8faa63` (older).

Spawnable vanilla planets, by `Name`: Byblos, Kemik, Caligo, MarsLike, Palatine,
EarthLike, WaterPlanet, Geomeles.

## Height encoding

The generator maps a heightmap texel back to a radius:

```
radius(v) = R × (1 + hill_min + (v / 65535) × (hill_max − hill_min))
```

`ZeroGround` is sea level in the same radius fractions, so the texel at the
waterline is:

```
waterline = (ZeroGround − hill_min) / (hill_max − hill_min) × 65535
```

| planet | HillParams | ZeroGround | waterline texel | band below |
|---|---|---|---|---|
| EarthLike | −0.01 … 0.12 | 0 | 5,041 | 8 % |
| Verdure | −0.01 … 0.12 | 0.015 | 12,603 | 19 % |
| Byblos | −0.3333 … 0.03333 | 0 | 59,577 | 91 % |
| Geomeles | −0.2 … 0.2 | — | — | — |

`Min = Max = 0` makes a perfectly smooth sphere and the heightmaps do nothing.
Every vanilla planet sets `MaxAltimeter` equal to `HillParams.Max`.

Any planet made after VS2.0 should reference a `PlanetVersionDefinition`:
`PlanetVersionDefinition_VS2-2` `f36276b0-3b93-44b3-9391-38a0cb8f4099`, or
`PlanetVersionDefinition_VS2-3` `81c50d54-f7c4-4afe-8c9a-b4732a1df638`, which is
a `Copy` of it.

## Exact PNG formats

Modern convention, VS2_0 onward. VS1_5 differs and is not a model to copy.

| map | format | sizes |
|---|---|---|
| heightmap | 16-bit greyscale, colour type 0 | 2048 / 4096 / 8192 square |
| biome map | 8-bit greyscale, colour type 0 | 4096 / 8192 |
| material map | 8-bit greyscale, colour type 0 | 2048 / 4096 / 8192 |
| albedo | 8-bit RGB | 4096 / 8192 |
| normal | 16-bit RGBA, alpha a dead 255 | 4096 / 8192 |
| ambient occlusion | 8-bit greyscale | 4096 / 8192 |
| roughness | 8-bit greyscale, optional | 4096 |

All non-interlaced. Colour type 4 (grey+alpha) also decodes but doubles the file
for a dead channel and no vanilla asset uses it. Normal and AO are often
authored at 8192 while albedo stays at 4096 — Caligo, Geomeles and Palatine all
do this; the sizes are independent.

Per-face PNGs are packed by the content pipeline into two cube maps via
`.comptex` intermediates: `*_cm.comptex` → `*_Overlay_CM.cubemap` (colour +
metal) and `*_nao.comptex` → `*_Overlay_NAO.cubemap` (normal + AO).

## The overlay is what you see from orbit, and it has a memory budget

`VoxelPlanetRenderComponentDefinition.PlanetOverlay` is, in the SDK's own words,
"displayed in place of detailed voxel rendering when the camera is sufficiently
far away". If a planet goes soft or washed-out as you pull back while vanilla
planets stay sharp, the overlay is where to look — and the usual cause is that it
does not fit in the streaming budget.

Total overlay VRAM, measured across every planet under `Assets/Procedural`:

| planet | CM | NAO | total |
|---|---|---|---|
| Byblos | 4096 BC1 67 MB | 4096 DXT1 67 MB | 134 MB |
| Testerran | 2048 BC7 34 MB | 4096 BC7 134 MB | 168 MB |
| MarsLike | — | 8192 DXT1 268 MB | 268 MB |
| Caligo / Geomeles / Palatine | 4096 BC1 67 MB | 8192 DXT1 268 MB | 335 MB |
| Kemik / **Verdure** | 8192 BC1 268 MB | 8192 DXT1 268 MB | **537 MB** |
| EarthLike | 2048 BC7 34 MB | 8192 BC7 537 MB | 570 MB |

**Six of the eight use `BC1`/`DXT1` for an 8192 NAO.** The two on BC7 are
EarthLike and Testerran, both VS1_5 — the oldest generation. A mod that lands on
BC7 at 8192 pays 537 MB for the NAO alone, 805 MB for the pair, more than any
shipped planet, and the streamer answers by serving low mips for the whole
sphere. Dropping to 4K hides it; fixing the compression is the actual cure.

### `.comptex` → `.texpreset` is what sets the format

Each face PNG has a `.comptex` sidecar whose `PresetReference` names a
`.texpreset` under `Engine/Assets/Materials/Presets`. The preset's
**`OutputFileCompression`** field decides the DDS format. The presets are *media*
assets, so their GUID lives in the `.meta` sidecar, not in the `.texpreset` body.

| preset | compression | out channels |
|---|---|---|
| `PBRMaterialTemplate_ColorTexture` | `BC1_UNORM_SRGB` | 3 |
| `PBRMaterialTemplate_ColorMetalTexture` | `BC7_UNORM_SRGB` | 4 |
| `PBRMaterialTemplate_NormalAOTexture` | **`BC7_UNORM`** | 4 |
| `TangentToWorldSpace{Forward,Backward,Left,Right,Up,Down}NormalAOTexture` | **`BC1_UNORM`** | 3 |

The generic `PBRMaterialTemplate_NormalAOTexture` is the wrong choice for a
planet twice over: it is BC7, and it passes the normal through unchanged. The
`TangentToWorldSpace*` family is per-face and converts the normal into world
space for that face's orientation — which is why there are six of them and why
Verdure uses a different one on each face. Without it the shading direction is
wrong per face and the surface reads flat rather than merely soft.

**The face-to-preset pairing follows the axis wiring, not the file name.** Give
each face the preset for the *slot it occupies*: the image in `PositiveXTexture`
takes `…LeftNormalAOTexture`, the one in `NegativeXTexture` takes
`…RightNormalAOTexture`, `+Z` takes `…BackwardNormalAOTexture`, `−Z` takes
`…ForwardNormalAOTexture`.

Colour needs no such family — `PBRMaterialTemplate_ColorTexture` on all six.

### Category on the cubemap

`CubemapModel.Category` is `PlanetColorOverlay` for colour and `PlanetOverlays`
for normal/AO. All 8 vanilla colour cubemaps and all 7 NAO cubemaps follow this
without exception. Both strings exist in
`VRage.ContentPipeline.Textures.dll`, so the wrong one still builds.

### Overlay brightness has a working range

Mean colour of the built `_Overlay_CM.dds`, decoded from the BC1 mip at ≤64 px:
Titan 52, Byblos 85, Verdure 96, Kemik 112, Palatine 117, Geomeles 119. Vanilla
spans **52–119**. Atmosphere scattering is additive over the surface, so a planet
much darker than that floor is swallowed by its own atmosphere at distance and
reads as a bright featureless ball however correct the atmosphere settings are.

Real Earth imagery walks straight into this: Blue Marble's ocean is about
`(2,5,20)`, luma 6, over 71% of the surface. Keen's own water world does not do
that — **Byblos paints its sea bed sandy `(90,80,67)` and lets the volumetric
water supply the blue.**

## The cube-face basis, and the trap in it

`+u` is increasing image column, `+v` increasing image row, world `+Y` is the
north pole.

| face | normal | +u (right) | +v (down) |
|---|---|---|---|
| front | Z− | +X | Y− |
| right | X− | Z− | Y− |
| back | Z+ | X− | Y− |
| left | X+ | Z+ | Y− |
| up | Y+ | X− | Z+ |
| down | Y− | X− | Z− |

**The trap:** around the equator the strip runs right to left, so `front`'s
right-hand edge joins `left`, not `right`. The commonly posted cross diagram is
easy to read the wrong way here.

Verified by measuring cross-face seam error on Keen's own Verdure heightmaps:
the correct basis gives a seam/interior ratio of 0.99, a rotated `up` gives 1.51,
all faces flipped gives 6.09, and a reversed equator gives 144.

Adjacent faces sample the sphere half a texel apart across a shared edge, so
their edge values are *not* meant to be identical. Generate all six from one
global field and the seams come out right with no stitching step.

**Keen's own maps name faces straight through** — the file called `left` goes in
the left slot. A generator that already uses this basis needs no swap; adding one
mirrors the planet.

**A cube face's ground scale is not uniform.** With `r² = 1 + s² + t²` over face
coordinates, `|dP/ds| = R·√(1+t²)/r²`, and one texel is `ds = 2/N`. At N = 8192
and R = 60 km that is **14.65 m per texel at the centre against 6.90 m at the
corner** — a factor of 2.12. Stock normal map filters assume constant spacing and
therefore exaggerate corner slopes; so does any slope statistic that uses the
centre spacing for the whole face, which is a mistake that has silently doubled a
vertical-scale calibration before now.

## Two cubemap formats, two different slot names

This is the single most confusing thing about planet maps, because the same six
images are addressed two different ways depending on the file.

| file | type | slots |
|---|---|---|
| `.planetcubemap` | `PlanetCubemapData` — height, biome, material | **named**: `Right` `Left` `Up` `Down` `Backward` `Forward` |
| `.cubemap` | `CubemapModel` — overlay CM and NAO | **axis**: `PositiveXTexture` `NegativeXTexture` `PositiveYTexture` … |

For `.planetcubemap` the names match straight through — `left.png` goes in
`Left`. For `.cubemap` you have to go through the basis table above, and the X
pair is the one everybody gets backwards:

| axis slot | takes the face called | because that face's normal is |
|---|---|---|
| `PositiveXTexture` | **left** | X+ |
| `NegativeXTexture` | **right** | X− |
| `PositiveYTexture` | up | Y+ |
| `NegativeYTexture` | down | Y− |
| `PositiveZTexture` | **back** | Z+ |
| `NegativeZTexture` | **front** | Z− |

Verdure's own `Verdure_Overlay_NAO.cubemap` is wired exactly this way:
`PositiveXTexture → Planet_Left_nao`, `NegativeXTexture → Planet_Right_nao`. It
looks like a mistake and is not.

**How to check without guessing.** A surface normal points outward, so on the
`+X` face the mean red channel must be above 128 and on `−X` below it. Decode the
smallest mip of each cube face of the built `_Overlay_NAO.dds` and read the mean
per channel. Measured on Verdure: `+X` R=180, `−X` R=80, `+Y` G=178, `−Y` G=74,
`+Z` B=175, `−Z` B=74 — all six on the correct side. Any face on the wrong side
is a wiring or preset error.

## Clouds are a volumetric shell, not a painted texture

`CloudDefinitionObjectBuilder` raymarches a shell. There is no cloud image
anywhere — it takes three small textures and composites procedural noise on top:

| input | resolution | compression | contents |
|---|---|---|---|
| `BiomeTexture` | 256² cube | `R8G8_UNORM` | **R = coverage (added), G = density (multiplied)** |
| `WeatherOverlays[].OverlayTexture` | 256² cube | `R8G8_UNORM` | greyscale; rotates about `RotationAxis` at `RotationSpeed` |
| `ShapeLUT` | **32×32** | `R8G8_UNORM` | X = coverage, Y = height; R = probability, G = density |

Only R and G survive compression. The presets are `CloudCoverageDensity`
(`12a74b43-cbb8-4f9e-9d9b-2814bdc44a19`) and `CloudShapeLUT`
(`6d858b29-fa6d-46e9-b04e-b3de79d669f0`); each takes **one** source PNG and
reads its R and G. Cloud cubemaps set `Category: None`, and unlike the overlay
they are named by axis (`*_px`, `*_nx`, …) and wire straight through.

The SDK's field docs give Earth-like values outright: `CloudTint` white,
`HenyeyGreensteinEccentricity` 0.99, `HenyeyGreensteinScattering` 1.0, and
`AmbientPlanetAlbedo` **0.15** ("Value of earth, without clouds, is 0.15" —
Verdure ships 0.1).

**Do not copy a vanilla cloud biome map onto an Earth.** Verdure's was measured
back into lat/lon and it is latitude-banded (zonal std 48 against meridional 14)
but banded the *wrong way* for Earth:

| band | Verdure R | Earth, MODIS May |
|---|---|---|
| equator | 112 — its **minimum** | 0.69 — a **maximum** (ITCZ) |
| subtropics | 168 / 153 | 0.53 / 0.55 — the **minimum** |
| mid-latitudes | 202 / 203 | 0.66 / 0.85 |
| poles | 110 / 101 | 0.73 / 0.66 |

Real cloud climatology is free from NASA NEO as 0.1° float GeoTIFF:
`MODAL2_M_CLD_FR` (cloud fraction → coverage) and `MODAL2_M_CLD_OT` (optical
depth → density), at
`https://neo.gsfc.nasa.gov/archive/geotiff.float/<dataset>/<dataset>_<year>-<mm>.FLOAT.TIFF`.
Average a dozen or more of the same month so the map is a climatology and not one
year's ENSO state, and match the month to the albedo — the ITCZ migrates. **The
files are big-endian (`MM`) and PIL does not swap them**; read without the
byteswap and every value comes out around 1e38. `99999.0` is the no-data fill.

Two statistics worth matching, measured off Verdure, because plain fractal noise
misses both badly and the clouds then read as a smooth sheet instead of distinct
systems: its weather map has a mean absolute neighbour difference of **22.6** and
a standard deviation of **105.6** out of 255 — more than a uniform
distribution's 73.6, so it is nearly bimodal and wants a contrast curve.

Generating the weather noise as a function of the **3D direction vector** makes
it seamless across every cube edge for free — two faces meeting ask the same
question of the same point. Measured seam difference 3.7/255 against an interior
neighbour difference of 21.8, a ratio of 0.17.

`ShellStartHeight` and `ShellThickness` are multiples of planet radius. Verdure
uses 0.04 / 0.04 — at R = 60 km that is clouds from 2.4 to 4.8 km, *below* its
7.2 km peaks. On a planet with a compressed vertical scale the same numbers put
the clouds far above the mountains; pick a shell that still clears the highest
terrain and no more.

Who made vanilla's, from the PNG metadata: `VerdureCloudShape.png` is **GIMP
2.10**, `cloud_weather_*.png` are **Adobe Photoshop 26.8**, and the cloud biome
faces carry no authoring metadata at all. There is no specialist cloud tool.

## ColorKeys are author-defined

A `ColorKey` is just the 8-bit value you painted into the index map. You choose
it, and you bind it by creating a `PlanetMaterialMapDefinition` or
`PlanetBiomeDefinition` with that number. Verdure's habit of using multiples of
ten is a Verdure habit, nothing more:

```
Verdure, Byblos   biome 10,20,…,80 and 200
Caligo            90, 100, 101
Geomeles          90, 96
Palatine          90…97
Kemik             10, 40, 50, 228, 230
MarsLike          22, 46, 55…61
EarthLike         0, 3, 10, 13, 17, 20, 27, 30, 33, 36, 40, 43, 46, 50, 56, 60, 75, 76
```

Material maps use their own, denser space — Verdure 1..93, Byblos up to 111.

The only hard rule: **the set of values present in the map must match the set of
definitions you created**, or texels fall through to nothing.

**Index maps must only ever be resampled nearest-neighbour.** Any bilinear or
area filter invents in-between values that map to no material. Keen's own 2048
material map for Verdure carries 106, 113, 135, 140, 164, 194, 224, 253, 254 and
255 that do not exist in the 8192 original — they filtered a downscale.

## Building one, in order

1. `search_content('PlanetGenerator')` and read the Byblos set under
   `Assets/Procedural/VS3_0/Planets/Byblos` — the newest complete planet.
2. Author the maps: six 8192² 16-bit greyscale PNGs per cubemap, plus a
   `.planetcubemap` naming all six by GUID.
3. Write each definition above, including `PlanetInfoDefinition`.
4. `audit_project` — catches unresolved GUIDs and missing sidecars the editor
   will not.
5. `launch_editor`, `editor_validation`, `editor_build`.
6. In game: `CTRL+F12 → Gameplay → Voxel → pick the planet → set radius →
   Activate planet placer`.

For oceans see [04-water.md](04-water.md) — the height band has to be designed
around the waterline before you author a single texel.
