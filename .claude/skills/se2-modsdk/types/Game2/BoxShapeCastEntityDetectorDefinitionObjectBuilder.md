# BoxShapeCastEntityDetectorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.EntityDetection.BoxShapeCastEntityDetectorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.EntityDetection`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `QueryHalfExtents` | Half extents of the box used for detection. |

## A real one

`Vanilla\Assets\Characters\System\CharacterObstacleDetectorComponent.def`

```json
{
  "Guid": "65f97e0b-3260-41aa-8d06-bac1f937cc07",
  "Transform": {
    "Transform": {
      "Position": {
        "X": 0,
        "Y": 1.5,
        "Z": -0.4
      },
      "Orientation": {
        "X": 0,
        "Y": 0,
        "Z": 0,
        "W": 1
      }
    },
    "EulerHint": {
      "X": 0,
      "Y": 0,
      "Z": 0
    }
  },
  "MaxLength": 0.66,
  "DetectNearest": false,
  "QueryHalfExtents": {
    "X": 0.2,
    "Y": 0.2,
    "Z": 0.01
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BoxShapeCastEntityDetectorDefinitionObjectBuilder')
search_content('', type_contains='BoxShapeCastEntityDetectorDefinitionObjectBuilder')
```
