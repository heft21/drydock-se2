# VoxelGeneratorDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Definitions.VoxelGeneratorDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Definitions`
- definitions using it: **10**

## What it is

VRage | Voxels - VoxelGeneratorDefinition

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DepositMaterials` | The list of ore deposit materials that can be spawned. |
| `Settings` | Specifies the number of shapes that will be used in procedural additions and removals. Also includes settings for the size and count of ore deposits. |
| `SurfaceMaterials` | The list of materials that can appear on the voxel shape. |
| `VoxelMapsUsedAsPrimaryAdditionShape` | The list of possible voxel maps that can be used as the base shape. Base shape determines the size of the storage. It is recommended that these be the biggest voxel maps or parts of shapes may get clipped off. |
| `VoxelMapsUsedInProceduralAdditions` | The list of voxel maps that can be used for adding shapes to the base structure. It is recommended to use smaller shapes than the primary ones or parts of shapes may get clipped off. |
| `VoxelMapsUsedInProceduralRemovals` | The list of voxel maps that can be used for removing shapes from the base structure. It is recommended to use smaller shapes than the primary ones or parts of shapes may get clipped off. |

## A real one

`Vanilla\Assets\Procedural\VS2_2\System\Data\Volumes\KemikRingField.def`

Too large to inline. Fields present:

`DepositMaterials`, `Guid`, `Settings`, `SurfaceMaterials`, `VoxelMapsUsedAsPrimaryAdditionShape`, `VoxelMapsUsedInProceduralAdditions`, `VoxelMapsUsedInProceduralRemovals`

Others: `IceShatterField`, `FieldGenerator1`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelGeneratorDefinitionObjectBuilder')
search_content('', type_contains='VoxelGeneratorDefinitionObjectBuilder')
```
