# SeatEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.SeatEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OnEnterOrExitSeatAudio` | Audio event to play when player enters and exits seat One shot sound |
| `OnOffAudioParameter` | Audio event parameter to control if enter or exit is played. |
| `OnOffAudioParameterOffValue` | Value sent to FMOD Studio to play exit seat. |
| `OnOffAudioParameterOnValue` | Value sent to FMOD Studio to play enter seat. |

## A real one

`Vanilla\Assets\Templates\Blocks\BlockEffects\Cockpit_SeatEffectsComponentDefinition.def`

```json
{
  "Guid": "0930a116-67c2-458f-9b8a-acf70a98d322",
  "OnEnterOrExitSeatAudio": "event:/SFX/Block/Cockpit",
  "OnOffAudioParameter": "OnOff",
  "OnOffAudioParameterOnValue": "On",
  "OnOffAudioParameterOffValue": "Off"
}
```

Others: `ControllableSeat_SeatEffectsComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('SeatEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='SeatEffectsComponentDefinitionObjectBuilder')
```
