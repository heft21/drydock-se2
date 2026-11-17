# VoxelProceduralTrimmingConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Definitions.VoxelProceduralTrimmingConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Enabled` | Toggles the trimming process for removing small voxel cells. When set to true, the procedural voxel trimming will be applied during readouts. If false, no trimming is performed. |
| `MaxPostProcessingLod` | Specifies the last level of detail (LOD) at which post-processing trimming will be applied. No trimming will be performed for levels of detail above this value. |
| `MaxRemovedCells` | Maximum number of voxel cells that can be removed during a single trimming pass. This prevents excessive removals in cases where cascading effects generate large numbers of new candidates for removal, helping to maintain performance during processing. Default: 255. |
| `NeighborsConsideredLimit` | Maximum number of non-empty neighbors a voxel cell can have before it is no longer considered for removal. This prevents the trimming process from removing cells that are part of significant structures. Default: 12. |
| `ThresholdLevelIncrement` | Defines the reduction in the removal threshold for each non-empty neighbor found around a voxel cell. This decreases the likelihood of removal for cells surrounded by non-empty neighbors, helping preserve significant geometry. Default: 4. |
| `ThresholdMaximumLevel` | Maximum content level a cell can have to be eligible for removal if all its neighbors are empty. Cells with content levels above this threshold will not be removed, even if surrounded by empty neighbors. Default: 247. Note: Content levels range from 0 to 255, where 0 represents empty and 255 represents full. |

## A real one

`Engine\Assets\Configurations\VoxelProceduralTrimmingConfiguration.def`

```json
{
  "Guid": "2fd7d814-138b-4305-afba-c2f854f50e7e",
  "Enabled": true,
  "ThresholdMaximumLevel": 255,
  "ThresholdLevelIncrement": 1,
  "NeighborsConsideredLimit": 0,
  "MaxRemovedCells": 255,
  "MaxPostProcessingLod": 1,
  "MaxTrimmingPasses": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelProceduralTrimmingConfigurationObjectBuilder')
search_content('', type_contains='VoxelProceduralTrimmingConfigurationObjectBuilder')
```
