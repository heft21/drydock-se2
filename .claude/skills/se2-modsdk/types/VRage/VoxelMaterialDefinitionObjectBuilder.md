# VoxelMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Definitions.VoxelMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Definitions`
- definitions using it: **114**

## What it is

Object builder for .

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Name` | Name of the voxel material. Note: Will be replaced with filename once the functionality is available. |
| `PhysicsMaterial` | Material specific data for collision handling. For setting up global fallbacks and voxel specific constants, check VoxelDestructionDefaults configuration. If this is null on a material, the default values will be used. |

## A real one

`Engine\Assets\Materials\Voxels\FallbackVoxelMaterial.def`

```json
{
  "Guid": "b624ee22-1e44-486a-ab0a-04e2634a02d6",
  "Name": "FallbackVoxel",
  "PhysicsMaterial": "8fabb5be-014a-4c11-a16d-8bd2dc293d9f"
}
```

Others: `IceOre`, `GoldOre`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelMaterialDefinitionObjectBuilder')
search_content('', type_contains='VoxelMaterialDefinitionObjectBuilder')
```
