# ColonizationMapConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.ColonizationMap.ColonizationMapConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.ColonizationMap`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AddMarker` | Input to add a new GPS Marker |
| `BunchIcon` | Icon to use when markers are bunched |
| `CameraDistanceAnimationSpeedFactor` | Affects how quickly the camera will animate towards its target distance |
| `CameraFOV` | Custom camera field of view override when rendering map view. Helps mitigate perspective distortion on the map 3D elements. Changes to this value may require reviewing and . |
| `CameraFocusPointOffset` | Camera focus point offset |
| `CameraModeKey` | Camera mode key |
| `ColonizationMapPrefab` | Prefab of the colonization map visuals |
| `ColonizedSectorGradientColor` | Sector gradient color when colonized |
| `ColonizedSectorMainColor` | Sector main color when colonized |
| `DefaultCameraAngle` | Default camera angle |
| `DefaultCameraPercentageDistance` | Percentage value between 0-100. Indicates at what percentage between max and min distances the camera will be placed at by default. E.g. if set to 0, the camera will be placed at the min distance, and if at 100 it will be placed at the max distance. |
| `DefaultIcon` | Default icon to use for markers |
| `DeleteMarker` | Input to delete selected GPS Marker |
| `FocusFontSize` | Focus font size for GPS Markers on map. |
| `Font` | Font to use to render GPS markers. |
| `GPSMarkersDefinition` | Definition of GPS Markers settings on world. |
| `HighlightEffect` | Optional highlight effect to apply on the affected sectors |
| `InputContextDefinition` | Context for colonization map toggle |
| `Interact` | Input to interact with colonization map objects |
| `InteractionsContextDefinition` | Context for colonization map interactions |
| `LockedIcon` | Default icon to use for locked lanes |
| `LockedSectorGradientColor` | Sector gradient color when locked |
| `LockedSectorMainColor` | Sector main color when locked |
| `MaxCameraDistance` | Maximum camera distance |
| `MinCameraDistance` | Minimum camera distance |
| `MinCameraDistanceIncrementPercent` | Percentage of camera distance to add to current camera distance during a single zoom tick, for smallest scroll input |
| `MoonBiasScale` | Extra multiplier applied to when biasing moon positions away from their parent planet. Higher values push moons farther from the planet on the map. |
| `MoonVisibilityZoomLevel` | Maximum zoom level percentage (0-100) at which moon labels remain visible. |
| `MoveBackward` | Move backward input |
| `MoveDown` | Move down input |
| `MoveForward` | Move forward input |
| `MoveLeft` | Move left input |
| `MoveRight` | Move right input |
| `MoveUp` | Move up input |
| `MovementSpeed` | Baseline movement speed |
| `OreDetector` | Defines ore materials that can be detected and mined by the player |
| `PlanetInfluenceScale` | Controls the size of the markers zone of influence for planets, as a multiplier of the . Positions of GPS Markers within the zone are translated along the planet radial direction based on the planet scale and marker distance to center. I.e: If a marker is on the planet surface in the world, it will be translated on the map to visually appear on the visually scaled planet surface. |
| `PlanetNameSize` | Font size of the planet name labels |
| `PlanetScale` | Multiplier of the planet scale on the map |
| `PlanetVisibilityZoomLevel` | Maximum zoom level percentage (0-100) at which planet labels remain visible. |
| `PlayerIcon` | Icon to use for the player location |
| `RegularFontSize` | Regular font size for GPS Markers on map. |
| `RenameMarker` | Input to rename selected GPS Marker |
| `SkyboxBrightness` | Override of the skybox intensity while on the map |
| `SkyboxOrientation` | Orientation of the skybox relative to the map visuals. Can be used to visually alter the position of the sun on the map screen. |
| `StarVisualPrefab` | Prefab of the main star map object visuals |
| `ToggleMap` | Input to transition to and out of colonization map |
| `ToggleUIVisibility` | Input to toggle UI visibility (GPS Markers) |
| `UnlockedSectorGradientColor` | Sector gradient color when unlocked |
| `UnlockedSectorMainColor` | Sector main color when unlocked |
| `ZoomChange` | Zoom change input |

## A real one

`Vanilla\Assets\System\Configurations\ColonizationMapConfiguration.def`

Too large to inline. Fields present:

`AddMarker`, `AsteroidFieldScale`, `AsteroidHighlightBoost`, `AsteroidLabelSize`, `AsteroidVolumeMinThickness`, `AsteroidVolumeScale`, `BackpackMarkersVisibilityZoomLevel`, `BunchIcon`, `CameraDistanceAnimationSpeedFactor`, `CameraFOV`, `CameraFocusPointOffset`, `CameraModeKey`, `CameraMovementAnimationSpeedFactor`, `ColonizationMapPrefab`, `ColonizedSectorGradientColor`, `ColonizedSectorMainColor`, `DefaultCameraAngle`, `DefaultCameraPercentageDistance`, `DefaultIcon`, `DeleteMarker`, `FieldSeparationFactor`, `FocusFontSize`, `Font`, `GPSMarkersDefinition`, `Guid`, `HighlightEffect`, `InputContextDefinition`, `Interact`, `InteractionsContextDefinition`, `LockedIcon`, `LockedSectorGradientColor`, `LockedSectorMainColor`, `MarkerFadeOpacity`, `MarkersVisibilityFadeZoomRange`, `MaxCameraDistance`, `MinCameraDistance`, `MinCameraDistanceIncrementPercent`, `MissionMarkersVisibilityZoomLevel`, `MoonBiasScale`, `MoonVisibilityZoomLevel`, `MoveBackward`, `MoveDown`, `MoveForward`, `MoveLeft`, `MoveRight`, `MoveUp`, `MovementSpeed`, `OreDetector`, `PlanetInfluenceScale`, `PlanetNameSize`, `PlanetScale`, `PlanetVisibilityZoomLevel`, `PlayerIcon`, `RegularFontSize`, `RenameMarker`, `SkyboxBrightness`, `SkyboxOrientation`, `StarVisualPrefab`, `ToggleMap`, `ToggleUIVisibility`, `UnlockedSectorGradientColor`, `UnlockedSectorMainColor`, `ZoomChange`

---

Read it with the MCP server rather than by hand:

```
describe_type('ColonizationMapConfigurationObjectBuilder')
search_content('', type_contains='ColonizationMapConfigurationObjectBuilder')
```
