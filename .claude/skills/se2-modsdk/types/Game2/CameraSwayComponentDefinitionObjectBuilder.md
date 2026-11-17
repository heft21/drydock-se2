# CameraSwayComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraSwayComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BuffetAmplitude` | Buffet amplitude relative to the base sway (whose amplitude is 1.0 before normalization). |
| `BuffetFrequencyHz` | Per-axis frequency (Hz) of the higher-frequency "buffet" layer summed on top of the base sway to break its predictability and sell environmental chaos. |
| `BuffetPhase` | Per-axis phase offset (radians) of the buffet sine. |
| `Dampening` | Per-tick dampening applied to sway power. |
| `DefaultSettings` | Default shake settings used when no settings are provided on . |
| `StopThreshold` | Stop swaying when sway power drops below this threshold. |
| `SwayFrequencyHz` | Per-axis frequency (Hz) of the slow base "wind body" sway sine. |
| `SwayPhase` | Per-axis phase offset (radians) of the base sway sine. Used to break inter-axis correlation. |
| `UpwindFraction` | When a wind direction is provided to , the sway along that axis is asymmetric: the camera is pushed mostly downwind, with a small upwind excursion reading as inertia/spring rebound. |

## A real one

`Vanilla\Assets\System\Camera\RenderCamera\RenderCameraSwayComponentDefinition.def`

```json
{
  "Guid": "993e04fd-fa23-4f05-8328-f6e5c90f3002",
  "DefaultSettings": "5bd51886-5bfd-4f59-a937-b690a42bf4f5"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraSwayComponentDefinitionObjectBuilder')
search_content('', type_contains='CameraSwayComponentDefinitionObjectBuilder')
```
