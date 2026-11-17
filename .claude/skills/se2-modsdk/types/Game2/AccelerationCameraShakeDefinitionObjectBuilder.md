# AccelerationCameraShakeDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Shake.AccelerationCameraShakeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Shake`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AccelerationShakePowerCap` | Maximum power than can be applied to the shake effect by the acceleration shakes on any given tick. |
| `AccelerationShakeSettings` | to be used when the camera shakes as a result of acceleration. If left empty, default settings will be used. |
| `AccelerationToShakePowerMultiplier` | The higher this value is, the more the shake effect will be powerful for a given acceleration. |
| `DecelerationShakePowerCap` | Maximum power than can be applied to the shake effect by the deceleration shakes on any given tick. |
| `DecelerationShakeSettings` | to be used when the camera shakes as a result of deceleration. If left empty, default settings will be used. |
| `DecelerationToShakePowerMultiplier` | The higher this value is, the more the shake effect will be powerful for a given deceleration. |
| `SpeedDeltaThreshold` | Speed average delta threshold necessary to be reached to trigger a camera shake response. |
| `SpeedSamplingWindow` | Number of seconds over which the speed will be sampled each tick in order to be averaged out before being processed for camera shakes. The higher the value is, the less the acceleration-based camera shakes will be sensible to instantaneous changes from one instant to another. Minimum value is the duration of one tick. Example: when the character starts walking or running, its speed changes instantaneously, for a lower value, this will trigger shakes. |

## A real one

`Vanilla\Assets\System\Camera\GridFirstPersonCameraAccelerationCameraShakeDefinition.def`

```json
{
  "Guid": "15347f80-0aa5-4286-b58a-a88488c4223d",
  "AccelerationShakeSettings": "baeed0e3-020b-451d-a689-69e37fcd1d64",
  "DecelerationShakeSettings": "a56ad2a8-9c99-4508-8ee3-ff0dd287c097",
  "AccelerationToShakePowerMultiplier": 5,
  "AccelerationShakePowerCap": 1,
  "DecelerationToShakePowerMultiplier": 2,
  "DecelerationShakePowerCap": 1,
  "SpeedSamplingWindow": 0.16,
  "SpeedDeltaThreshold": 0
}
```

Others: `GridThirdPersonCameraAccelerationCameraShakeDefinition`, `CharacterFirstPersonCameraAccelerationCameraShakeDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('AccelerationCameraShakeDefinitionObjectBuilder')
search_content('', type_contains='AccelerationCameraShakeDefinitionObjectBuilder')
```
