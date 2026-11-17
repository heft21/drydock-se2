# VoxelStorageComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Components.VoxelStorageComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `VoxelMapFile` | A reference to the resource file used to load the voxel map. |

## A real one

`Vanilla\Assets\Procedural\VS1_5\System\Data\Asteroids\AsteroidStorageDefinitions\Asteroid64-001.def`

```json
{
  "Guid": "7f8a11c8-2035-4309-8a0a-072f4bb0cdbe",
  "VoxelMapFile": "{G}1691135f-ffdc-4ee1-be5f-470e0f13f8af"
}
```

Others: `Asteroid128-004`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelStorageComponentDefinitionObjectBuilder')
search_content('', type_contains='VoxelStorageComponentDefinitionObjectBuilder')
```
