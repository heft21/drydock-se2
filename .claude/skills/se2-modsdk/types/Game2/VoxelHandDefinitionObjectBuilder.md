# VoxelHandDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Toolbars.VoxelHand.VoxelHandDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Toolbars.VoxelHand`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AdvancedSettingsHoverIcon` | Icon for the advanced settings |
| `AdvancedSettingsIcon` | Icon for the advanced settings |
| `BrushDistanceDefault` | Default brush distance, in meters |
| `BrushDistanceMax` | Maximum brush distance, in meters |
| `BrushDistanceMin` | Minimum brush distance, in meters |
| `BrushDistanceScaling` | Scales the brush distance sensitivity by the current brush distance. Makes the sensitivity exponential with distance when used Disabled when at 0 |
| `BrushMaterialGroups` | List of material groups that can be used to paint with |
| `BrushShapes` | Supported brush shapes |
| `BrushSizeDefault` | Default brush size (each brush shape interprets this differently) |
| `BrushSizeHoverIcon` | Hover Icon for the brush size selection |
| `BrushSizeIcon` | Icon for the brush size selection |
| `BrushSizeMax` | Maximum brush size |
| `BrushSizeMin` | Minimum brush size |
| `BrushSizes` | Selections of different brush sizes for UI |
| `CapsuleBrushMaxRadius` | Maximum radius of the capsule brush, in meters |
| `CapsuleBrushMinRadius` | Minimum radius of the capsule brush, in meters |
| `ChangeBrushDistance` | Input for adjusting brush distance |
| `ChangeBrushDistanceCoefficient` | Sensitivity modifier for changing the brush distance when projection mode is disabled |
| `ChangeBrushShape` | Input to cycle to next brush shape |
| `ChangeBrushSize` | Input for adjusting brush size |
| `ChangeBrushSizeCoefficient` | Sensitivity modifier for changing the size of the brush |
| `CloseSettings` | Input to close the tool settings panel |
| `ConsumedInputKinds` | Inputs consumed by voxel hand component |
| `CycleBrushMaterial` | Input to cycle to next brush material |
| `InputContextDefinition` | VoxelHand tool input context |
| `OpenSettings` | Input to open the tool settings |
| `PassedInputKinds` | Inputs ignored/passed-through by voxel hand component |
| `PickVoxelMaterial` | Input to pick/select the material of the currently targeted voxel |
| `ProjectedBrushActivationInterval` | How often the brush is activated when the trigger is held down |
| `QuickMenuDefinition` | Definition for the quick menu |
| `QuickMenuHoldTime` | Timeout until quick menu opens when input is being held |
| `RotatePitchNegative` | Input for rotating pitch in the negative direction |
| `RotatePitchPositive` | Input for rotating pitch in the positive direction |
| `RotateRollNegative` | Input for rotating roll in the negative direction |
| `RotateRollPositive` | Input for rotating roll in the positive direction |
| `RotateYawNegative` | Input for rotating yaw in the negative direction |
| `RotateYawPositive` | Input for rotating yaw in the positive direction |
| `RotationPerSecond` | The maximum rotation of the brush per second |
| `TerrainSculptorPrimary` | Input for primary tool action |
| `TerrainSculptorSecondary` | Input for secondary tool action |
| `ToggleFreeMode` | Input for toggling free voxel hand mode (disables snapping when intersecting with voxel) |
| `TransparencyDefault` | Default transparency of the brush display 100 is fully solid while 0 is completely invisible |

## A real one

`Vanilla\Assets\System\Creative Tools\Voxel Hand\TerrainSculptor.def`

Too large to inline. Fields present:

`AdvancedSettingsHoverIcon`, `AdvancedSettingsIcon`, `BrushDistanceDefault`, `BrushDistanceMax`, `BrushDistanceMin`, `BrushDistanceScaling`, `BrushMaterialGroups`, `BrushShapes`, `BrushSizeDefault`, `BrushSizeHoverIcon`, `BrushSizeIcon`, `BrushSizeLabel`, `BrushSizeMax`, `BrushSizeMin`, `BrushSizes`, `CapsuleBrushMaxRadius`, `CapsuleBrushMinRadius`, `ChangeBrushDistance`, `ChangeBrushDistanceCoefficient`, `ChangeBrushShape`, `ChangeBrushSize`, `ChangeBrushSizeCoefficient`, `CloseSettings`, `ConsumedInputKinds`, `ControlGroupHint`, `CycleBrushMaterial`, `Guid`, `HintsTitle`, `InputContextDefinition`, `OpenSettings`, `OpenSettingsHint`, `OperationHints`, `PassedInputKinds`, `PickVoxelMaterial`, `ProjectedBrushActivationInterval`, `QuickMenuDefinition`, `QuickMenuHoldTime`, `RotateHint`, `RotatePitchNegative`, `RotatePitchPositive`, `RotateRollNegative`, `RotateRollPositive`, `RotateYawNegative`, `RotateYawPositive`, `RotationPerSecond`, `ShiftGroupHint`, `TerrainSculptorPrimary`, `TerrainSculptorSecondary`, `ToggleFreeMode`, `TransparencyDefault`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelHandDefinitionObjectBuilder')
search_content('', type_contains='VoxelHandDefinitionObjectBuilder')
```
