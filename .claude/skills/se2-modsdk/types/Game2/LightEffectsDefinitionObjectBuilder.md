# LightEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Shared.Render.Lights.Effects.LightEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Shared.Render.Lights.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OnStateChangeAudio` | Audio event to play when light is on/off. One shot sound |
| `StateChangeAudioParameter` | Parameter to change to set on or off |
| `StateChangeAudioParameterOff` | Parameter value for when light is off |
| `StateChangeAudioParameterOn` | Parameter value for when light is on |

## A real one

`Vanilla\Assets\Characters\System\CharacterLightEffectsDefinition.def`

```json
{
  "Guid": "58e75231-abde-4a28-8eb0-0ecf48a31daa",
  "OnStateChangeAudio": "event:/SFX/Character/SuitLight",
  "StateChangeAudioParameter": "OnOff",
  "StateChangeAudioParameterOn": "On",
  "StateChangeAudioParameterOff": "Off"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LightEffectsDefinitionObjectBuilder')
search_content('', type_contains='LightEffectsDefinitionObjectBuilder')
```
