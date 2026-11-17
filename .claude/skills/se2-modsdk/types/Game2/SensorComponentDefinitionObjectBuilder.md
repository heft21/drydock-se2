# SensorComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Detectors.SensorComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Detectors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FloatingObjectsLayer` | The Entity Layer that corresponds to floating objects. |
| `GridLayers` | The Entity Layers that correspond to grids. |
| `InitialDetectionBoxSize` | The initial size of the box that will be used for detection when the block is placed. |
| `MaxDetectionBoxSize` | The maximum extents on each axis that the detection box is able to be expanded on each direction. |
| `PlayersLayer` | The Entity Layer that corresponds to player characters. |
| `VoxelsLayer` | The Entity Layer that corresponds to voxels (planet, asteroids, boulders). |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Sensor_SensorComponentDefinition.def`

```json
{
  "Guid": "80c9a04a-7a67-49ae-94c6-1c91b57594d1",
  "InitialDetectionBoxSize": {
    "X": 1,
    "Y": 1,
    "Z": 1
  },
  "MaxDetectionBoxSize": {
    "X": 50,
    "Y": 50,
    "Z": 50
  },
  "GridLayers": [
    {
      "Key": "99190a45-d20d-42ba-8231-c74b7de4bb9f",
      "Value": "Grids"
    },
    {
      "Key": "eb93c25f-ac0e-40f4-9e4c-4b760d10462b",
      "Value": "HeavyGrids"
    }
  ],
  "FloatingObjectsLayer": "FloatingObjects",
  "VoxelsLayer": "Voxels",
  "PlayersLayer": "Characters"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SensorComponentDefinitionObjectBuilder')
search_content('', type_contains='SensorComponentDefinitionObjectBuilder')
```
