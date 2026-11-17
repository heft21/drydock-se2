# VoxelDebugScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.Debugging.Screens.Voxels.VoxelDebugScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.Debugging.Screens.Voxels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AsteroidFieldsRenderDefinitions` | List of models that can be used to visualize asteroid rings |
| `ChangeAsteroidDistance` | Input to adjust placement distance |
| `ChangeAsteroidDistanceCoefficient` | Sensitivity of the placement distance input |
| `EntityAreaTemplates` | List of volumes that can be used for creating entity areas. |
| `InputContextDefinition` | Input context settings, active during placement |
| `PlaceAsteroid` | Input to place asteroid/planet |
| `PlanetPreviewer` | Prefab of the preview version of the planet to spawn |
| `PlanetSpawner` | Planet configurator that can build a planet based on the given values |
| `ProceduralVolumePrefab` | Prefab for the manually placed field / ring. |
| `VoxelAsteroid` | Default asteroid to spawn when using asteroid placement |
| `VoxelDynamic` | Default dynamic voxel prefab used in Activate Map Placer |
| `VoxelMap` | Default voxel map used in Activate Map Placer |
| `VoxelMapPresets` | List of voxel maps that can be spawned by the MapPlacer |
| `VoxelMaterialPresets` | List of materials that can be used by the dynamic storage placer. |

## A real one

`Vanilla\Assets\UI\Screens\VoxelDebugSettingsConfiguration.def`

Too large to inline. Fields present:

`AsteroidFieldsRenderDefinitions`, `ChangeAsteroidDistance`, `ChangeAsteroidDistanceCoefficient`, `EntityAreaTemplates`, `Guid`, `InputContextDefinition`, `PlaceAsteroid`, `PlanetPreviewer`, `PlanetSpawner`, `ProceduralVolumePrefab`, `VoxelAsteroid`, `VoxelDynamic`, `VoxelMap`, `VoxelMapPresets`, `VoxelMaterialPresets`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelDebugScreenConfigurationObjectBuilder')
search_content('', type_contains='VoxelDebugScreenConfigurationObjectBuilder')
```
