# RaycastEntityDetectorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.EntityDetection.RaycastEntityDetectorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.EntityDetection`
- definitions using it: **3**

## What it is

Object builder for

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DummyOcclusionEpsilon` | Offset to apply to the raycast hit position, away from the surface, when detecting dummies or taking into account physics occlusion. Used to prevent raycast from detecting an eventual dummy overlapping with the block model at this location. |
| `MaxLength` | Maximum raycast travel distance, in meters. |
| `Transform` | Linear and angular offset that will be applied to the origin of the ray used for detection. |

## A real one

`Vanilla\Assets\System\Spectator\DetectorRaycastSpectator.def`

```json
{
  "Guid": "ecb79963-35e6-456e-8941-e3945bd024d5",
  "MaxLength": 5,
  "DummyOcclusionEpsilon": 0.0001,
  "Transform": {
    "Transform": {
      "Position": {
        "X": 0,
        "Y": 0,
        "Z": 0
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
  }
}
```

Others: `DetectorRaycastCharacter`, `FarDetectorRaycastSpectator`

---

Read it with the MCP server rather than by hand:

```
describe_type('RaycastEntityDetectorDefinitionObjectBuilder')
search_content('', type_contains='RaycastEntityDetectorDefinitionObjectBuilder')
```
