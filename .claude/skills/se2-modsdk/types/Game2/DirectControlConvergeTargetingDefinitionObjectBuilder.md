# DirectControlConvergeTargetingDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Weapons.DirectControlConvergeTargetingDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Weapons`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CameraAdditionalOffset` | Additional offset to the camera position. |
| `CameraDummyType` | Model dummy used for offsetting the camera. |
| `CameraModel` | Model containing the camera through . It usually is a subpart of the targeting block |
| `ConvergenceSmoothStepDistance` | Distance from or where convergence is smoothly transitioned |
| `MaxConvergenceDistance` | Maximum distance to check for convergence |
| `MinConvergenceDistance` | Minimum distance to check for convergence |

## A real one

`Vanilla\Assets\Blocks\RocketTurret\250\RocketTurret250_DirectControlConvergeTargetingDefinition.def`

```json
{
  "Guid": "b95e9c96-cff9-40f7-a407-2032daf9f619",
  "MaxConvergenceAngle": 30,
  "CameraModel": "c4d06104-46fa-4461-a07a-d5b7a4f52739",
  "CameraDummyType": "6fc9829d-3ee4-4735-b229-e00157f67a42",
  "CameraAdditionalOffset": {
    "X": 0.125,
    "Y": 1,
    "Z": 0.125
  },
  "MinConvergenceDistance": 10,
  "MaxConvergenceDistance": 100,
  "ConvergenceSmoothStepDistance": 5
}
```

Others: `RocketTurret600_DirectControlConvergeTargetingDefinition`, `GatlingTurret600_DirectControlConvergeTargetingDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DirectControlConvergeTargetingDefinitionObjectBuilder')
search_content('', type_contains='DirectControlConvergeTargetingDefinitionObjectBuilder')
```
