# CameraShakeSettingsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraShakeSettingsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **7**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxFalloffDistance` | Distance from camera at which shake intensity will be attenuated down to zero |
| `MaxShakePos` | Max relative offset applied to camera position on each axis |

## A real one

`Vanilla\Assets\System\Weather\WeatherCameraShakeSettingsDefinition.def`

```json
{
  "Guid": "82ac2e73-052c-49c8-af64-6f775be3e523",
  "MaxShakePos": {
    "X": 0.4,
    "Y": 0.08,
    "Z": 0.2
  },
  "MaxFalloffDistance": 50
}
```

Others: `FirstPersonCameraAccelerationShakeSettings`, `FirstPersonCameraDecelerationShakeSettings`

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraShakeSettingsDefinitionObjectBuilder')
search_content('', type_contains='CameraShakeSettingsDefinitionObjectBuilder')
```
