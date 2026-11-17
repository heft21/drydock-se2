# VoxelOctreeComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Components.VoxelOctreeComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Material` | Material to use as the base material for this voxel storage. |
| `ShapeCenter` | Specifies the center coordinates of the voxel shape within the storage. |
| `VoxelMapFile` | A reference to the resource file used to load the voxel map. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\VoxelOctreeComponent.def`

```json
{
  "Guid": "29f45833-9d49-4cdc-9d19-ee4e243f7c8b",
  "VoxelMapFile": "{G}ddb9cbcd-a84f-4a98-9be0-facf4e63e7d6",
  "Material": "2be020a3-440f-48ed-a62b-05274d52bcf4",
  "ShapeCenter": {
    "X": 0,
    "Y": 0,
    "Z": 0
  }
}
```

Others: `Boulder_15Component`, `Boulder_30Component`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelOctreeComponentDefinitionObjectBuilder')
search_content('', type_contains='VoxelOctreeComponentDefinitionObjectBuilder')
```
