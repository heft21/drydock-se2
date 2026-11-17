# VoxelMaterialGameSettingsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.VoxelMaterialGameSettingsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FallbackMaterial` | The fallback material is used if suitable voxel material is not found. |

## A real one

`Vanilla\Assets\System\Configurations\VoxelMaterialGameSettings.def`

```json
{
  "Guid": "5a1dad61-ae9d-4bf8-998a-feb9a1d47972",
  "FallbackMaterial": "b0c83318-c4e7-45b0-9043-972a0e3fe345"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelMaterialGameSettingsConfigurationObjectBuilder')
search_content('', type_contains='VoxelMaterialGameSettingsConfigurationObjectBuilder')
```
