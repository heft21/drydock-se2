# VoxelClipmapSettingsDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Definitions.VoxelClipmapSettingsDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Definitions`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AmbientOcclusion` | Ambient occlusion can add subtle shadows in crevices or areas with less light exposure, improving the overall visual quality. When configured, this setting applies ambient occlusion effects using the specified . If set to null the ambient occlusion for this clipmap will be disabled. |
| `ExtremeSetting` | Preset settings for extreme-quality rendering. These settings maximize visual fidelity at the expense of performance, intended for high-end hardware or offline rendering workflows. |
| `GISetting` | Preset settings for indirectly rendered terrain, such as in environment probes or during raytracing. Optimized for scenarios where terrain is rendered in the background or indirectly affects lighting. Suitable for global illumination (GI) and other indirect rendering workflows. |
| `HighSetting` | Preset settings for high-quality rendering. These settings prioritize visual quality while maintaining reasonable performance, making them suitable for high-performance hardware. |
| `LowSetting` | Preset settings for low-quality rendering. These settings prioritize performance over visual quality, making them suitable for lower-end hardware or performance-critical scenarios. |
| `NormalSetting` | Preset settings for normal-quality rendering. These settings balance performance and visual quality, offering a general-purpose configuration for most use cases. |

## A real one

`Vanilla\Assets\Environment\System\BoulderClipmapSettings.def`

```json
{
  "Guid": "6c73c7d4-74f7-4c97-ba27-80d6b85e5b6f",
  "LowSetting": {
    "CellBits": 4,
    "LodSize": 2,
    "AdditionalLodCells": [],
    "LastLod": 4,
    "LastLodRange": 16384,
    "MinSize": -1
  },
  "NormalSetting": {
    "CellBits": 5,
    "LodSize": 2,
    "AdditionalLodCells": [],
    "LastLod": 4,
    "LastLodRange": 16384,
    "MinSize": -1
  },
  "HighSetting": {
    "CellBits": 5,
    "LodSize": 2,
    "AdditionalLodCells": [],
    "LastLod": 6,
    "LastLodRange": 32768,
    "MinSize": -1
  },
  "ExtremeSetting": {
    "CellBits": 5,
    "LodSize": 9,
    "AdditionalLodCells": [],
    "LastLod": -1,
    "LastLodRange": -1,
    "MinSize": 16
  },
  "GISetting": {
    "CellBits": 4,
    "LodSize": 2,
    "AdditionalLodCells": [],
    "LastLod": 4,
    "LastLodRange": 16384,
    "MinSize": -1
  },
  "AmbientOcclusion": "64007eef-6433-45fc-9a23-84412da390dd"
}
```

Others: `AsteroidClipmapSettings`, `VoxelClipmapSettingsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelClipmapSettingsDefinitionObjectBuilder')
search_content('', type_contains='VoxelClipmapSettingsDefinitionObjectBuilder')
```
