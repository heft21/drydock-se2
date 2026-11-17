# CameraShakeComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraShakeComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Dampening` | Shake power dampening, applied every tick This controls the shake duration |
| `DefaultSettings` | Default shake settings used when shaking the camera if none are provided. |
| `Reduction` | Scalar applied to returned shake offset |
| `RotationSettings` | Settings of the shake rotation applied to camera upon camera shakes. |
| `ShakePowerMultiplier` | Global shake multiplier that applied to every shake request |
| `StopThreshold` | Stop shaking when shake power drops below this threshold |

## A real one

`Vanilla\Assets\System\Camera\RenderCamera\RenderCameraShakeComponent.def`

```json
{
  "Guid": "33a74648-882d-4fb6-ad8d-85a007e09a86",
  "DefaultSettings": "5bd51886-5bfd-4f59-a937-b690a42bf4f5",
  "Reduction": 0.6,
  "Dampening": 0.85,
  "StopThreshold": 0.01,
  "ShakePowerMultiplier": 1,
  "RotationSettings": {
    "MaxRollShakeAngle": 0.2618,
    "MinRollShakeFrequency": 17,
    "MaxRollShakeFrequency": 30,
    "MaxPitchShakeAngle": 0.3491,
    "MinPitchShakeFrequency": 12,
    "MaxPitchShakeFrequency": 30
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraShakeComponentDefinitionObjectBuilder')
search_content('', type_contains='CameraShakeComponentDefinitionObjectBuilder')
```
