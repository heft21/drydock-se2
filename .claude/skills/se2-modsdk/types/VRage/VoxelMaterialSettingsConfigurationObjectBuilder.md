# VoxelMaterialSettingsConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Definitions.VoxelMaterialSettingsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DepthCorrectionFactor` | The factor used for correction of depth sampling of materials in steep slopes. The depth will be corrected by [this factor] / [sampled normal] - 1; |
| `FallbackMaterial` | This material serves as a default option to ensure rendering continuity and prevent errors when the intended material cannot be found. |

## A real one

`Engine\Assets\Configurations\VoxelMaterialSettingsConfiguration.def`

```json
{
  "Guid": "d96828bd-bd4e-4622-a4d7-860a70fd2ff1",
  "FallbackMaterial": "b624ee22-1e44-486a-ab0a-04e2634a02d6",
  "DepthCorrectionFactor": 1.3
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelMaterialSettingsConfigurationObjectBuilder')
search_content('', type_contains='VoxelMaterialSettingsConfigurationObjectBuilder')
```
