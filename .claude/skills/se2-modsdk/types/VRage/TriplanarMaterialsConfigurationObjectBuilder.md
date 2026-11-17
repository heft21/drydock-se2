# TriplanarMaterialsConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Render.TriplanarMaterialsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Render`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GlobalGI` | Low quality master terrain material used for GI. Uses Far3 colors. |
| `GlobalMulti` | Non-tessellated master terrain material allowing indexing of the individual materials from global material table and to be used when mesh mixes 2 or more materials |
| `GlobalPlanetGI` | Low quality master planet terrain material used for GI. Uses Far3 colors. |
| `GlobalSingle` | Non-tessellated master terrain material allowing indexing of the individual materials from global material table and to be used when mesh contains only single material |
| `GlobalTessellationMulti` | Tessellated master terrain material allowing indexing of the individual materials from global material table and to be used when mesh mixes 2 or more materials |
| `GlobalTessellationSingle` | Tessellated master terrain material allowing indexing of the individual materials from global material table and to be used when mesh contains only single material |
| `GlobalUltraMulti` | Experimental material for performing up to 3 different texture blends (with each blend having 2 textures, for 6 textures total) simultaneously |
| `ModelMaterialStateOverride` | Material State override for voxel materials to make them compatible with asset models (e.g. voxel debris) |
| `PlanetGlobalMulti` | Non-tessellated master planet terrain material allowing indexing of the individual materials from global material table and to be used when mesh mixes 2 or more materials |
| `PlanetGlobalSingle` | Non-tessellated master planet terrain material allowing indexing of the individual materials from global material table and to be used when mesh contains only single material. |
| `PlanetGlobalTessellationMulti` | Tessellated master planet terrain material allowing indexing of the individual materials from global material table and to be used when mesh mixes 2 or more materials |
| `PlanetGlobalTessellationSingle` | Tessellated master planet terrain material allowing indexing of the individual materials from global material table and to be used when mesh contains only single material |
| `PlanetGlobalUltraMulti` | Experimental material for performing up to 3 different texture blends (with each blend having 2 textures, for 6 textures total) simultaneously |
| `PlanetOverlaySettings` | Global settings for the planet overlay (e.g. transition distances) |
| `PlanetWaterSphere` | Water renderer for the planet sphere - uses the same passes as normal water but generates a sphere around the planet that matches the planet's spherization |
| `TriplanarSettings` | Global settings for the terrain material tessellation |
| `VoxelDefault` | For sample purposes, now not used - Deprecated |

## A real one

`Engine\Assets\Configurations\TriplanarMaterialsConfiguration.def`

```json
{
  "Guid": "bf119563-a48b-4e28-abdc-b20cebd5ca9c",
  "ModelMaterialStateOverride": "95a8abdd-7e1f-4cfc-b636-a1d73d2e7d8c",
  "VoxelDefault": "455e8a63-6679-4888-a390-64e86e155f54",
  "GlobalSingle": "455e8a63-6679-4888-a390-64e86e155f54",
  "GlobalMulti": "d2df6fae-b0d1-4011-9f75-dd04c05b67f9",
  "GlobalTessellationSingle": "1f6b37d2-a20e-49e1-b6b6-7857cf8d3a0c",
  "GlobalTessellationMulti": "caa2b6f4-1985-4cf4-9323-689b2aba883f",
  "GlobalGI": "5aabca2d-2de3-4088-adc9-b4b15e81ad5a",
  "PlanetGlobalSingle": "f76815ea-01b3-4ba3-986b-631ac4972242",
  "PlanetGlobalMulti": "af358e4c-a15a-4352-bcec-939d7ca75dc0",
  "PlanetGlobalTessellationSingle": "674bee31-bfcf-4b08-a735-bba46424444d",
  "PlanetGlobalTessellationMulti": "08ea214b-6a0e-48f3-998b-e9b9f23ccd71",
  "GlobalPlanetGI": "15831c0f-4e0d-48ff-8273-cb80fa42d931",
  "PlanetWaterSphere": "189bbce9-5723-4979-bdb8-1421074851a9",
  "TriplanarSettings": {
    "TessellationEnabled": true,
    "TessellationDisplacementOffset": -0.2,
    "TessellationDisplacementRange": 0.4,
    "TessellationCliffDisplacementOffset": -0.4,
    "TessellationCliffDisplacementRange": 0.8,
    "TessellationTriangleSize": 7.5,
    "TessellationFadeOutBegin": 25,
    "TessellationFadeOutEnd": 35,
    "TessellationMipmap": 1,
    "SpherizationEnabled": true,
    "SpherizationStart": 8000,
    "SpherizationRange": 50000,
    "SpherizationScale": 0.8,
    "NearHeightBlendingTightness": 30,
    "NearHeightBlendingInfluence": 4,
    "FarHeightBlendingTightness": 10,
    "FarHeightBlendingInfluence": 2,
    "NearFarBlendingStart": 0,
    "NearFarBlendingEnd": 40,
    "DistanceBlendTightenFactor": 0,
    "AntiTilingTightenFactor": 0,
    "TriplanarBlendTightenFactor": 0,
    "WeatheringLighteningMultiplier": 0.5,
    "WeatheringDarkeningMultiplier": 0
  },
  "PlanetOverlaySettings": {
    "OverlayTransitionFactor": 0.5,
    "OverlayColorStartMultiplier": 0.12,
    "OverlayColorEndMultiplier": 0.2,
    "OverlayMetalStartMultiplier": 0.12,
    "OverlayMetalEndMultiplier": 0.2,
    "OverlayNormalStartMultiplier": 0.12,
    "OverlayNormalEndMultiplier": 0.2,
    "OverlayRoughnessStartMultiplier": 0.12,
    "OverlayRoughnessEndMultiplier": 0.2,
    "OverlayAOStartMultiplier": 0.12,
    "OverlayAOEndMultiplier": 0.2,
    "OverlayEmissiveStartMultiplier": 0.12,
    "OverlayEmissiveEndMultiplier": 0.2
  },
  "GlobalUltraMulti": null,
  "PlanetGlobalUltraMulti": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TriplanarMaterialsConfigurationObjectBuilder')
search_content('', type_contains='TriplanarMaterialsConfigurationObjectBuilder')
```
