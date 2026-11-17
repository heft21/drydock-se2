# TerrainDetailCubemapDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.Surface.TerrainDetailCubemapDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet.Surface`
- definitions using it: **9**

## What it is

The detail cubemap is a cubemap texture that assigns each region on the surface to a detail texture. This texture is applied on top of the base map and can enhance the level of detail.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlendingCoverageMap` | used to blend the materials from adjacent Patterns with similar height. |
| `DecayFactor` | Factor used to scale down detail heightmaps as lods get more distant to achieve the fade out effect. |
| `LookupCubemap` | Cubemap lookup textures. Each pixel's value represents a detail pattern on the pattern map. |
| `LookupPlanetCubemap` | Cubemap lookup textures. Each pixel's value represents a detail pattern on the pattern map. |
| `MaterialBlendingThreshold` | Normally materials are assigned by the pattern that contributes the most height to a position. This threshold can be used to improve interpolation if multiple patterns contribute similar heights. |
| `Patterns` | Mapping of texture values to the pattern they should represent. |
| `TargetPlanetRadius` | Expected radius of a planet that uses this cubemap. |

## A real one

`Vanilla\Assets\Environment\Planets\EarthLike\DetailCubemap.def`

```json
{
  "Guid": "22ae874a-f601-4990-af20-987f57cf92a4",
  "Patterns": {
    "43": "7d1d5dd3-f497-4da2-a51b-66caccf135a3",
    "33": "358fb457-39b3-4cc7-a5e3-93a3d40da5a0",
    "76": "61b78e11-728a-4d0f-92b8-b0e7e6861080",
    "0": "61b78e11-728a-4d0f-92b8-b0e7e6861080"
  },
  "LookupCubemap": {
    "Right": "{G}d7b1d2c6-8d32-485b-9bf2-2e41385f6076",
    "Left": "{G}a35b7b68-dc44-4250-8b43-97c9d2d25db6",
    "Up": "{G}c7ad3ed1-e05e-4b6c-9a08-5cac5e44ed33",
    "Down": "{G}5ca78b07-8185-4cd0-b0a0-fd88629c243f",
    "Backward": "{G}fc08b6de-0900-4918-98e9-70b662d51692",
    "Forward": "{G}4dd42eb4-66e1-4d00-90d8-3b90a6e6a121"
  },
  "LookupPlanetCubemap": "{G}aadfff26-e4e2-45eb-ab2e-827cad5e5508",
  "TargetPlanetRadius": 60000,
  "DecayFactor": 0,
  "MaterialBlendingThreshold": 0,
  "BlendingCoverageMap": null
}
```

Others: `MarsLikeDetailCubemap`, `KemikDetailCubemap`

---

Read it with the MCP server rather than by hand:

```
describe_type('TerrainDetailCubemapDefinitionObjectBuilder')
search_content('', type_contains='TerrainDetailCubemapDefinitionObjectBuilder')
```
