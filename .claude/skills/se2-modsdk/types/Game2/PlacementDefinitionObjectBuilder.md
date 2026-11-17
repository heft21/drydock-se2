# PlacementDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.PlacementDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **77**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlignWithMountPoints` | When true, the block's mount points will be taken into consideration when determining the best snap position. When false, the block's AABB is used. |
| `AllowSquareSnapping` | On faces of the block that are square, the block will try to maintain the same position in different rotations. Doesn't do anything if none of the faces on the block are square |
| `AutoRotateFace` | Optional face that will be used as the "bottom" of the autorotation, such as the back of a thruster/interior light. This is the side of the block that will be placed against the target block. When not provided, the block placer will pick the best face depending on the mount points. |
| `BestSnapSize` | Optional best snap size (in block cells) when being placed down. When not provided, the block placer picks the best snap size depending on the size of the block. |
| `MaxInVoxelRatio` | When the block intersects with voxel, the block is allowed to intersect by this ratio. This does not guarantee that the block will always be in the voxel by this ratio, it is only a limit. 0-1 |
| `OverrideSymmetries` | Specify a different symmetry for the block |
| `SizeGroup` | Optional override of the size group for this block |
| `SnapAlignment` | Changes how the block aligns when snapping. By default (when all flags are disabled), the block attempts to snap towards the center of the block. For example, a window block should snap on the outside edge of the snap grid instead of being centered. |

## A real one

`Vanilla\Assets\Armors\ArmorPlacerDefinition.def`

```json
{
  "Guid": "d3bfe2c2-79d1-4522-8c54-2f3a69f0b348",
  "BestSnapSize": null,
  "AlignWithMountPoints": false,
  "AllowSquareSnapping": true,
  "AutoRotateFace": null,
  "SizeGroup": null,
  "MaxInVoxelRatio": 0.9,
  "SnapAlignment": 0,
  "OverrideSymmetries": null
}
```

Others: `CornerPlacementDefinition`, `Propulsion PlacerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlacementDefinitionObjectBuilder')
search_content('', type_contains='PlacementDefinitionObjectBuilder')
```
