# BlockPlacerConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.BlockPlacerConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AutoRotateGravityType` | When the gravity of this type is present, gravity aligned rotation will work |
| `BuildCollisionCheckSeparatingDistance` | Maximum distance around the preview collider to check |
| `CollisionCheckLayers` | All layers to check when probing for collision |
| `DebrisClearLayers` | Any entity that is detected with this layer during block materialization gets deleted |
| `DefaultBlockSymmetry` | The default block symmetry to use for blocks unless overridden |
| `DefaultSizeGroup` | The default size group when first activating the block placer |
| `GridPrefab` | Server prefab of a grid entity |
| `MaxBlocksPreciseAABB` | The maximum number of blocks where a precise AABB for the grid can be calculated. After which the grid storage boundary is used (imprecise) |
| `MaxDistance` | The maximum distance a grid can be modified from |
| `MaxSizeBlocksBoundingBoxes` | The maximum number of bounding blocks after which they are combined into a single bounding block |
| `MaxSupportDistance` | Maximum length the supports can be |
| `MaximumMergeDeviationDistance` | Maximum separation/penetration 2 grids can be in before merging with block placement is rejected |
| `ProjectionPrefab` | Server prefab of a projected grid entity |
| `SupportBlock` | Prefab of block that will be added as supports |
| `SupportGravityType` | When the gravity of this type is present, supports will be generated |
| `SupportsBaseColor` | Color of the last support block (the one connected to the voxel). When null, no color is used |
| `SupportsColor` | Color of supports blocks. When null, no color is used |
| `VerticalSupportsBias` | Bias multiplier for vertical supports vs horizontal ones. Higher values means that vertical trusses will be picked more often |

## A real one

`Vanilla\Assets\System\Configurations\BlockPlacerConfiguration.def`

```json
{
  "Guid": "bdc03f82-f9ff-4fa6-8848-a1925a0dd0c1",
  "MaxDistance": 75,
  "MaxSizeBlocksBoundingBoxes": 1000,
  "MaxBlocksPreciseAABB": 5000,
  "BuildCollisionCheckSeparatingDistance": 0.01,
  "MaximumMergeDeviationDistance": 0.01,
  "GridPrefab": "672d6382-207a-498f-a51c-58b370aa96cb",
  "ProjectionPrefab": "813cc896-507f-4f61-b69f-1198e5a80eb6",
  "MaxSupportDistance": 100,
  "SupportBlock": "cbf262b4-5d9f-4375-a94e-9df078ec0a20",
  "SupportGravityType": "7ef3901a-3517-4e92-b766-92b556861ab8",
  "AutoRotateGravityType": "6290b4c6-99f6-42dd-9425-bcd72170e6bc",
  "DefaultSizeGroup": "ec8fad91-ffdc-4d54-b403-a6a07fd5cce9",
  "DefaultBlockSymmetry": "e62c6bf0-8da4-45f4-a55d-25e6acadab4a",
  "DebrisClearLayers": "534036a8-c470-44c4-bd48-821bfa83be66",
  "CollisionCheckLayers": "735b6752-3855-4525-966f-5eecae9a3579"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockPlacerConfigurationObjectBuilder')
search_content('', type_contains='BlockPlacerConfigurationObjectBuilder')
```
