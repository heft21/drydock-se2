# PaintToolEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.Effects.PaintToolEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BrushActiveParticle` | Particle that is applied when the tool is active |
| `ColorBlockAudioParameter` | Audio event parameter to control if color loop is played or not. |
| `ColorBlockAudioParameterOffValue` | Value sent to FMOD Studio to stop color loop. |
| `OnColorBlockAudio` | Audio event to play on coloring a block. Looping as long as tool is active |

## A real one

`Vanilla\Assets\CharacterTools\PaintGun\PaintGun_Client_PaintToolEffectsDefinition.def`

```json
{
  "Guid": "10863bd2-0d39-4974-bf7f-33d42f6845e2",
  "BrushActiveParticle": {
    "ParticleEffect": "46fbfc78-41ae-4fce-8605-5909ca846064",
    "Dummy": "6fc9829d-3ee4-4735-b229-e00157f67a42",
    "Scale": 1
  },
  "ColorBlockAudioParameter": "End",
  "ColorBlockAudioParameterOffValue": 1,
  "OnColorBlockAudio": "event:/SFX/Tool/PaintTool"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PaintToolEffectsDefinitionObjectBuilder')
search_content('', type_contains='PaintToolEffectsDefinitionObjectBuilder')
```
