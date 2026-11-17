# ThrustEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Shared.Movement.Effects.ThrustEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Shared.Movement.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AudioPlaysWhenNoThrust` | If true, thrust audio will not be stopped when the thrust stops. This is useful for ships which have idle engine sounds |
| `MaxThrust` | Thrust to consider for maximum volume |
| `OnActivationAudio` | Audio event to play when thrusters are activated. This event responds to thrust value updates to modulate its sound. Looped sound. Uses parameter to stop itself when jetpack or thrusters are turned off |
| `OnBoostActivationAudio` | Audio event to play when thrusters boost is activated. |
| `ThrustBoostEndAudioParameter` | Audio event parameter to signify end of thrust audio loop. |
| `ThrustBoostEndAudioParameterValue` | Value sent to FMOD Studio to end thrust audio. |
| `ThrustEndAudioParameter` | Audio event parameter to signify end of thrust audio loop. |
| `ThrustEndAudioParameterValue` | Value sent to FMOD Studio to end thrust audio. |

## A real one

`Vanilla\Assets\Characters\System\Character_ThrustEffectsComponentDefinition.def`

```json
{
  "Guid": "0c9cec79-1d49-46da-957e-dc246eef32d5",
  "MaxThrust": 10,
  "ThrustEndAudioParameter": "JetpackRunEnd",
  "ThrustEndAudioParameterValue": 1,
  "OnActivationAudio": "event:/SFX/Character/JetpackRun",
  "OnBoostActivationAudio": "event:/SFX/Character/JetpackPush",
  "AudioPlaysWhenNoThrust": false
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ThrustEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='ThrustEffectsComponentDefinitionObjectBuilder')
```
