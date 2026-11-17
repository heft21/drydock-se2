# GridPastingToolComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.BlockPlacement.BlockPlacer.GridPastingToolComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.BlockPlacement.BlockPlacer`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BannerTitle` | Text displayed in the banner when pasting |
| `Cancel` | Cancel pasting |
| `CaptureBlueprint` | Captures a blueprint of the grid being pasted |
| `CutGridDialog` | Dialog shown when the user attempts to cut a grid |
| `SurvivalCutGridFailureNotification` | Notification shown in survival when a grid can't be cut due a block being welded |

## A real one

`Vanilla\Assets\System\GridPasting\GridPasting.def`

Too large to inline. Fields present:

`AlighmentModeChangeMessageDuration`, `BannerTitle`, `BlockCountText`, `BlockCountTextColor`, `BlockLineDimensionsText`, `BlockPlacementMessageTitle`, `BlockSlidingMode`, `BlockVariantDecrease`, `BlockVariantIncrease`, `BuildDimensionsFont`, `BuildDistanceThreshold`, `BuildLengthInvalidColor`, `BuildLengthValidColor`, `Cancel`, `CaptureBlueprint`, `ChangeBuildAlignment`, `ChangeBuildDistance`, `ChangeBuildDistanceCoefficient`, `CollisionCheckCacheCapacity`, `ConsumedInputKinds`, `CopyMode`, `CopyPivotType`, `CriticalBuildReasons`, `CutGridDialog`, `DefaultPlacementDefinition`, `DefaultPrefabGrid`, `DefaultPrefabServerGrid`, `DeleteBlock`, `DeletionColor`, `EmptyPositionSearchRefiningSamples`, `EmptyPositionSearchSamples`, `EnterSymmetrySetup`, `FailureNotifications`, `FreeAlignmentModeText`, `GravityAlignmentModeText`, `GridAlignmentModeText`, `Guid`, `HighlightInflation`, `HighlightThickness`, `HologramCornerLengthPercent`, `HologramDashLengthPercent`, `HologramHighlightLengthPercent`, `HologramOutlineDots`, `HologramVolumeDotSize`, `InputContextDefinition`, `LineHelperColor`, `LineHelperDepth`, `LineMode`, `LocKeyBlockPlacerAlignment`, `LocKeyBlockPlacerControlGroup`, `LocKeyBlockPlacerDistance`, `LocKeyBlockPlacerNewGrid`, `LocKeyBlockPlacerPartialCopy`, `LocKeyBlockPlacerPlace`, `LocKeyBlockPlacerPlaneMode`, `LocKeyBlockPlacerRemove`, `LocKeyBlockPlacerSize`, `LocKeyChangeSymmetryPlane`, `LocKeyCreateBlueprint`, `LocKeyEnterSymmetry`, `LocKeyExitSymmetry`, `LocKeyExitSymmetrySetup`, `LocKeyPlaceSymmetryPlane`, `LocKeyRemoveSymmetryPlane`, `LocKeySymmetryPlaneSetupHint`, `LocKeyToolControlRotate`, `LockKeyBlockPlacerCancel`, `MaxAlignedAngularSpeed`, `MaxAlignedSpeed`, `MaxBlocks`, `MaxBuildLength`, `MaxDistanceMultiplier`, `MaxMountPointDistanceFromPrimary`, `MaxMountPointScanSteps`, `MinBuildDistance`, `MinDistanceMultiplier`, `MinInheritedSpeed`, `MountableTargetCellHighlight`, `NewGridHighlightColor`, `NewGridModeHintText`, `NewGridModeText`, `NoPersonalPCUNotification`, `NonMountableTargetCellHighlight`, `ObstructedHighlightColor`, `OneClickGridMode`, `OneClickMinGridDistance`, `OpenColorMenu`, `PassedInputKinds`, `PickColorMenu`, `PlaceBlock`, `PlaneMode`, `PrecisionGridColor`, `PrecisionGridFalloff`, `PrecisionGridPadding`, `PrecisionGridThickness`, `PrecisionModeHighlightColor`, `PrecisionModeHighlightThickness`, `PreviewHidingReasons`, `PreviewerPrefab`, `RotateBlockPitchNegative`, `RotateBlockPitchPositive`, `RotateBlockRollNegative`, `RotateBlockRollPositive`, `RotateBlockYawNegative`, `RotateBlockYawPositive`, `RotationAnimationDuration`, `RotationCoefficient`, `RotationInputContextDefinition`, `RotationMode`, `SelectedBlockHighlightColor`, `ShowGizmoAfterAngleMovementThreshold`, `SnapGridColor`, `SnapGridDepth`, `SnapGridThickness`, `SnapSizeDecrease`, `SnapSizeIncrease`, `SnapSizeText`, `SnapSizeVariants`, `SomeBlocksNotBuiltNotification`, `SurvivalCutGridFailureNotification`, `TargetedBlockHighlightColor`, `ThicknessFarScale`, `ThicknessScaleFarDistance`, `ThicknessScaleNearDistance`, `TimeBeforeLinePlaneBuild`, `ToggleSymmetryMode`, `TooltipsTitle`, `WarningUnsupportedProjection`, `WarningUnsupportedProjectionTitle`

---

Read it with the MCP server rather than by hand:

```
describe_type('GridPastingToolComponentDefinitionObjectBuilder')
search_content('', type_contains='GridPastingToolComponentDefinitionObjectBuilder')
```
