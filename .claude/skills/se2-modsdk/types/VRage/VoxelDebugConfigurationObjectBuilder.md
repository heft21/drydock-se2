# VoxelDebugConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Components.VoxelDebugConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FloraDebugRadius` | radius from the camera position to sample nearby flora items |
| `ObserverTag` | Tag associated to the observable entity whose transform we should use as vantage point for this system (e.g. camera) |

## A real one

`Engine\Assets\Configurations\Setup\VoxelDebugConfiguration.def`

```json
{
  "Guid": "6d4d9d95-9fe7-4811-a82d-5728d837c3c4",
  "ObserverTag": "VoxelObserver",
  "FloraDebugRadius": 100
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelDebugConfigurationObjectBuilder')
search_content('', type_contains='VoxelDebugConfigurationObjectBuilder')
```
