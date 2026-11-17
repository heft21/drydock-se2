# MechanicalBlockAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.MechanicalBlockAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EndAudio` | Audio event to play when mechanical block stops One shot |
| `MaxDistanceAudio` | Audio event to play when mechanical block reaches limit One shot |
| `NegativeMoveAudio` | Audio event to play on mechanical block negative movement Looped |
| `PositiveMoveAudio` | Audio event to play on mechanical block positive movement Looped |
| `StartAudio` | Audio event to play when mechanical block starts One shot |

## A real one

`Vanilla\Assets\Blocks\Hinge\50\Hinge50_Client_MechanicalBlockAudioDefinition.def`

```json
{
  "Guid": "845dc019-bea7-4d64-97f9-395cd7fcb993",
  "PositiveMoveAudio": "event:/SFX/Block/Hinge/Hinge50Move",
  "NegativeMoveAudio": "event:/SFX/Block/Hinge/Hinge50Move",
  "MaxDistanceAudio": "event:/SFX/Block/Hinge/Hinge50MaxDistance",
  "EndAudio": "event:/SFX/Block/Hinge/Hinge50MoveEnd"
}
```

Others: `Hinge_MechanicalBlockAudioDefinition`, `Rotors_MechanicalBlockAudioDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalBlockAudioDefinitionObjectBuilder')
search_content('', type_contains='MechanicalBlockAudioDefinitionObjectBuilder')
```
