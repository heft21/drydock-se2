# BlockPlacerEntityComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.BlockPlacement.BlockPlacer.BlockPlacerEntityComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.BlockPlacement.BlockPlacer`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlighmentModeChangeMessageDuration` | How long the alignment mode change message will be shown after changing the alignment mode. |
| `BlockCountText` | Localized text id of the block count text that shows when building a line or plane |
| `BlockCountTextColor` | Color of the text used when drawing the block count when line/plane building |
| `BlockLineDimensionsText` | Localized text id of the text that shows along a line/plane to show the length of it |
| `BlockPlacementMessageTitle` | Localized text id of the user message title used when the player is notified about changes related to block placement |
| `BlockSlidingMode` | Input action to toggle "block sliding mode" which lets player slide the preview block along the surface of the targeted block |
| `BlockVariantDecrease` | Input action to cycle backward through the different variants of the selected block |
| `BlockVariantIncrease` | Input action to cycle forward through the different variants of the selected block |
| `BuildDimensionsFont` | Font that is used for the text shown when line/plane building |
| `BuildDistanceThreshold` | Percentage of the active build distance that the preview will snap to grid. Makes building on far away things more forgiving. EX: When 0, the preview's raycast must be within the build distance. When 0.5 with a build distance of 10 meters, the block will snap to any looked-at grids within 15 meters. x = 10 + (10 * 0.5) |
| `BuildLengthInvalidColor` | The color of the build length text when the build length is invalid (too long) |
| `BuildLengthValidColor` | The color of the build length text when the length is valid |
| `ChangeBuildAlignment` | Input action to cycle between the different |
| `ChangeBuildDistance` | Input action to adjust the placement distance of the block from player |
| `ChangeBuildDistanceCoefficient` | How much the build distance will change on each input. One scroll step adds + to the current build distance |
| `CollisionCheckCacheCapacity` | Initial size of the collision cache |
| `ConsumedInputKinds` | InputKinds consumed by the BlockPlacer |
| `CopyMode` | Defines how connected grids will be handled when copying a grid. See the connection groups of mechanical blocks |
| `CopyPivotType` | Describes how unaligned rotation will be handled for pasting grids |
| `CriticalBuildReasons` | While building, if any failure occurs for the source block, the entire build will be prevented (including line/plane) |
| `DefaultPlacementDefinition` | The default settings used for placing blocks when they do not have a of their own. |
| `DefaultPrefabGrid` | Grid prefab to spawn on client side (only used by Editor scene at the moment) |
| `DefaultPrefabServerGrid` | Grid prefab spawned on server side to host the previewed block(s) |
| `DeleteBlock` | Input action to delete the target block |
| `DeletionColor` | Outline color of the block currently being deleted |
| `EnterSymmetrySetup` | Enter symmetry setup mode |
| `FailureNotifications` | Notification shown when the player fails to build something |
| `FreeAlignmentModeText` | Localized text id of the text that shows when setting the alignment mode to free alignment |
| `GravityAlignmentModeText` | Localized text id of the text that shows when setting the alignment mode to aligned by gravity |
| `GridAlignmentModeText` | Localized text id of the text that shows when setting the alignment mode to be aligned with grids |
| `HighlightInflation` | Inflation amount in meters around selected blocks. Helps prevent z-fighting between the selected block and block highlight |
| `HighlightThickness` | Maximum thickness of the preview block's outlines |
| `HologramCornerLengthPercent` | Length of the corners in the placement preview outline, as a percentage of the length of the shortest side |
| `HologramDashLengthPercent` | Length of the dashes in the placement preview outline, as a percentage of the length of the shortest side TODO: SE2-22687 None of these are Percent. Fix naming and add Range Validation |
| `HologramHighlightLengthPercent` | Length of the corners in the block highlight outline, as a percentage of the length of the shortest side |
| `HologramOutlineDots` | Whether to draw dots along the preview outline's borders |
| `HologramVolumeDotSize` | Whether to draw dots inside the volume of the preview when building volumes |
| `InputContextDefinition` | Main input context used during tools manipulation |
| `LineHelperColor` | The color of the line direction helper |
| `LineHelperDepth` | When true, the line direction helper will be hidden by other blocks |
| `LineMode` | Optional keybind. When null/not provided, the default build mode will be line mode. When provided, the default build mode will be "single", and the key must be pressed to build a line. |
| `LocKeyBlockPlacerAlignment` | Localized text id of the control hint text for block placement alignment |
| `LocKeyBlockPlacerControlGroup` | Hint for control group |
| `LocKeyBlockPlacerDistance` | Hint for changing distance |
| `LocKeyBlockPlacerNewGrid` | Hint for toggle to new grid mode |
| `LocKeyBlockPlacerPartialCopy` | Hint for partial copy |
| `LocKeyBlockPlacerPlace` | Hint for placing block |
| `LocKeyBlockPlacerPlaneMode` | Hint for plane mode |
| `LocKeyBlockPlacerRemove` | Hint for block removing |
| `LocKeyBlockPlacerSize` | Hint for changing size |
| `LocKeyChangeSymmetryPlane` | Hint for changing symmetry plane |
| `LocKeyCreateBlueprint` | Hint for create blueprint |
| `LocKeyEnterSymmetry` | Hint for entering symmetry |
| `LocKeyExitSymmetry` | Hint for exiting symmetry |
| `LocKeyExitSymmetrySetup` | Hint for exiting symmetry setup |
| `LocKeyPlaceSymmetryPlane` | Hint for placing symmetry plane |
| `LocKeyRemoveSymmetryPlane` | Hint for removing symmetry plane |
| `LocKeySymmetryPlaneSetupHint` | Hint for symmetry plane setup |
| `LocKeyToolControlRotate` | Hint for rotation |
| `LockKeyBlockPlacerCancel` | Hint for canceling |
| `MaxAlignedAngularSpeed` | Maximum angular speed that a ship can be before grid-alignment mode resets |
| `MaxAlignedSpeed` | Maximum linear speed that a ship can be before grid-alignment mode resets |
| `MaxBlocks` | The maximum number of blocks that can be built in a line/plane shape |
| `MaxBuildLength` | The maximum length in block cells a line can be built. When in plane mode, decides the maximum length for each dimension |
| `MaxDistanceMultiplier` | The multiplier to increase max distance, based on BB of the block/blueprint |
| `MaxMountPointDistanceFromPrimary` | When the primary mount point is occluded, neighboring mount points are searched. This is the maximum distance (in cells) a neighboring mount point can be from the primary mount point to be a valid option. Large values can impact performance on large blocks |
| `MaxMountPointScanSteps` | Max number of cells the preview can be pushed in from the edge of the AABB to check for a valid mount point |
| `MinBuildDistance` | The minimum distance in meters the block preview can be from the controller. |
| `MinDistanceMultiplier` | The multiplier to increase the minimum build distance, based on BB of the block/blueprint |
| `MinInheritedSpeed` | The minimum speed the controller has to be moving before the velocity becomes inherited |
| `MountableTargetCellHighlight` | Outline color of the quad displayed on the target cell face when a valid mount point is present |
| `NewGridHighlightColor` | Outline color of previewed block when current placement location would result in the creation of a new grid e.g. when the location is not obstructed but no mount points are available |
| `NewGridModeHintText` | Localized text id of the control hint text that shows when not in new grid mode |
| `NewGridModeText` | Localized text id of the text that shows when in new grid mode |
| `NoPersonalPCUNotification` | Notification that is shown when the user tries to build when there is no PCU left |
| `NonMountableTargetCellHighlight` | Outline color of the quad displayed on the target cell face when a valid mount point is missing |
| `ObstructedHighlightColor` | Outline color of the previewed block when placement is obstructed/not possible |
| `OneClickGridMode` | Input action for toggling new grid mode |
| `OneClickMinGridDistance` | Minimum distance the preview grid can be from another grid when in new grid mode |
| `OpenColorMenu` | Open the color selection menu |
| `PassedInputKinds` | InputKinds forwarded to other IControllers |
| `PickColorMenu` | Definition of the color menu opened by |
| `PlaceBlock` | Input action to place/spawn the block being previewed |
| `PlaneMode` | Activates the plane building mode |
| `PrecisionGridColor` | Color of the precision grid that is shown when in precision mode |
| `PrecisionGridFalloff` | How quickly the snap grid fades out. 1 = Linear, 2 = Exponential, etc |
| `PrecisionGridPadding` | The amount of times the snap grid is repeated around a highlighted area. It's the number of cells drawn, not lines |
| `PrecisionGridThickness` | Thickness of the precision grid |
| `PrecisionModeHighlightColor` | Fill color of the previewed block when in precision mode |
| `PrecisionModeHighlightThickness` | Thickness of the preview block's outlines when in precision mode |
| `PreviewHidingReasons` | All possible reasons the block placer preview can be hidden |
| `PreviewerPrefab` | Prefab of the block preview host entity with a |
| `RotateBlockPitchNegative` | Input action to rotate previewed block pitch angle clockwise |
| `RotateBlockPitchPositive` | Input action to rotate previewed block pitch angle counter-clockwise |
| `RotateBlockRollNegative` | Input action to rotate previewed block roll angle clockwise |
| `RotateBlockRollPositive` | Input action to rotate previewed block roll angle counter-clockwise |
| `RotateBlockYawNegative` | Input action to rotate previewed block yaw angle clockwise |
| `RotateBlockYawPositive` | Input action to rotate previewed block yaw angle counter-clockwise |
| `RotationAnimationDuration` | The amount of time the block rotation animation takes to complete when aligned to a grid |
| `RotationCoefficient` | When not aligned to a grid, the speed of rotation in radians per second |
| `RotationInputContextDefinition` | Input context used while in block rotation mode |
| `RotationMode` | Input action to toggle block rotation mode |
| `SelectedBlockHighlightColor` | Outline color of the previewed block |
| `ShowGizmoAfterAngleMovementThreshold` | The threshold angle in degrees under which the gizmo will not appear. |
| `SnapGridColor` | Color of the snap grid shown during placement |
| `SnapGridDepth` | When true, lines along the snap grid will be hidden by other blocks |
| `SnapGridThickness` | Thickness of the snap grid |
| `SnapSizeDecrease` | Input action to decrease block grid snapping distance |
| `SnapSizeIncrease` | Input action to increase block grid snapping distance |
| `SnapSizeText` | Localized text id of the snap size text that shows when adjusting snap size |
| `SnapSizeVariants` | Collection of available snap sizes in block cells |
| `SomeBlocksNotBuiltNotification` | Notification that is shown when the user is building a line or plane and some of the blocks could not be placed |
| `TargetedBlockHighlightColor` | Outline color of the block currently aimed at |
| `ThicknessFarScale` | Scale of the outlines when it is at the far distance or beyond |
| `ThicknessScaleFarDistance` | Distance at which outline thickness will reach the far scale |
| `ThicknessScaleNearDistance` | Distance at which outline thickness will start scaling |
| `TimeBeforeLinePlaneBuild` | The minimum time in seconds for a block to be detected as a single add/removal instead of line/plane |
| `ToggleSymmetryMode` | Activates the symmetry mode |
| `TooltipsTitle` | Title of the tooltips |
| `WarningUnsupportedProjection` | Text localization id of the text warning used when building an unsupported projection |
| `WarningUnsupportedProjectionTitle` | Text localization id of the text warning used when building an unsupported projection |

## A real one

`Vanilla\Assets\System\BlockPlacer\BlockPlacer.def`

Too large to inline. Fields present:

`AlighmentModeChangeMessageDuration`, `BlockCountText`, `BlockCountTextColor`, `BlockLineDimensionsText`, `BlockPlacementMessageTitle`, `BlockSlidingMode`, `BlockVariantDecrease`, `BlockVariantIncrease`, `BuildDimensionsFont`, `BuildDistanceThreshold`, `BuildLengthInvalidColor`, `BuildLengthValidColor`, `ChangeBuildAlignment`, `ChangeBuildDistance`, `ChangeBuildDistanceCoefficient`, `CollisionCheckCacheCapacity`, `ConsumedInputKinds`, `CopyMode`, `CopyPivotType`, `CriticalBuildReasons`, `DefaultPlacementDefinition`, `DefaultPrefabGrid`, `DefaultPrefabServerGrid`, `DeleteBlock`, `DeletionColor`, `EmptyPositionSearchRefiningSamples`, `EmptyPositionSearchSamples`, `EnterSymmetrySetup`, `FailureNotifications`, `FreeAlignmentModeText`, `GravityAlignmentModeText`, `GridAlignmentModeText`, `Guid`, `HighlightInflation`, `HighlightThickness`, `HologramCornerLengthPercent`, `HologramDashLengthPercent`, `HologramHighlightLengthPercent`, `HologramOutlineDots`, `HologramVolumeDotSize`, `InputContextDefinition`, `LineHelperColor`, `LineHelperDepth`, `LineMode`, `LocKeyBlockPlacerAlignment`, `LocKeyBlockPlacerControlGroup`, `LocKeyBlockPlacerDistance`, `LocKeyBlockPlacerNewGrid`, `LocKeyBlockPlacerPartialCopy`, `LocKeyBlockPlacerPlace`, `LocKeyBlockPlacerPlaneMode`, `LocKeyBlockPlacerRemove`, `LocKeyBlockPlacerSize`, `LocKeyChangeSymmetryPlane`, `LocKeyCreateBlueprint`, `LocKeyEnterSymmetry`, `LocKeyExitSymmetry`, `LocKeyExitSymmetrySetup`, `LocKeyPlaceSymmetryPlane`, `LocKeyRemoveSymmetryPlane`, `LocKeySymmetryPlaneSetupHint`, `LocKeyToolControlRotate`, `LockKeyBlockPlacerCancel`, `MaxAlignedAngularSpeed`, `MaxAlignedSpeed`, `MaxBlocks`, `MaxBuildLength`, `MaxDistanceMultiplier`, `MaxMountPointDistanceFromPrimary`, `MaxMountPointScanSteps`, `MinBuildDistance`, `MinDistanceMultiplier`, `MinInheritedSpeed`, `MountableTargetCellHighlight`, `NewGridHighlightColor`, `NewGridModeHintText`, `NewGridModeText`, `NoPersonalPCUNotification`, `NonMountableTargetCellHighlight`, `ObstructedHighlightColor`, `OneClickGridMode`, `OneClickMinGridDistance`, `OpenColorMenu`, `PassedInputKinds`, `PickColorMenu`, `PlaceBlock`, `PlaneMode`, `PrecisionGridColor`, `PrecisionGridFalloff`, `PrecisionGridPadding`, `PrecisionGridThickness`, `PrecisionModeHighlightColor`, `PrecisionModeHighlightThickness`, `PreviewHidingReasons`, `PreviewerPrefab`, `RotateBlockPitchNegative`, `RotateBlockPitchPositive`, `RotateBlockRollNegative`, `RotateBlockRollPositive`, `RotateBlockYawNegative`, `RotateBlockYawPositive`, `RotationAnimationDuration`, `RotationCoefficient`, `RotationInputContextDefinition`, `RotationMode`, `SelectedBlockHighlightColor`, `ShowGizmoAfterAngleMovementThreshold`, `SnapGridColor`, `SnapGridDepth`, `SnapGridThickness`, `SnapSizeDecrease`, `SnapSizeIncrease`, `SnapSizeText`, `SnapSizeVariants`, `SomeBlocksNotBuiltNotification`, `TargetedBlockHighlightColor`, `ThicknessFarScale`, `ThicknessScaleFarDistance`, `ThicknessScaleNearDistance`, `TimeBeforeLinePlaneBuild`, `ToggleSymmetryMode`, `TooltipsTitle`, `WarningUnsupportedProjection`, `WarningUnsupportedProjectionTitle`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockPlacerEntityComponentDefinitionObjectBuilder')
search_content('', type_contains='BlockPlacerEntityComponentDefinitionObjectBuilder')
```
