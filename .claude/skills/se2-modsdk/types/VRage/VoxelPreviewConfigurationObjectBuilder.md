# VoxelPreviewConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Definitions.VoxelPreviewConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `VoxelPlanetRender` | Definition used to render the preview specifically for voxel planet entities. |
| `VoxelRender` | Definition used to render the preview for non-planet voxel entities, such as asteroids. |

## A real one

`Engine\Assets\Configurations\Preview\VoxelPreviewConfiguration.def`

```json
{
  "Guid": "84205732-f776-4f6e-8093-2f0518297236",
  "VoxelRender": "6fd0260c-81e3-42f4-a9e7-363e98e58c26",
  "VoxelPlanetRender": "d5cd9788-8fa3-4670-bb0d-99001770f6bd"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelPreviewConfigurationObjectBuilder')
search_content('', type_contains='VoxelPreviewConfigurationObjectBuilder')
```
