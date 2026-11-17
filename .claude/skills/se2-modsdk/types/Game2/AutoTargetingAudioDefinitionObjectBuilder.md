# AutoTargetingAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.AutoTargetingAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlignAudioEndParameter` | Parameter name to send to when aligning is done |
| `AlignAudioEndValue` | Parameter value to send with when aligning is done |
| `AlignAudioStartValue` | Parameter value to send with when aligning starts |
| `OnAlignAudio` | Audio event to play when aligning with target. Looped sound |
| `OnIdleAudio` | Audio event to play when not moving. Looped sound |

## A real one

`Vanilla\Assets\Blocks\RocketTurret\600\RocketTurret600_Client_AutoTargetingAudioDefinition.def`

```json
{
  "Guid": "5cb2ef2b-6410-443e-b2f7-1bdc9362bf11",
  "OnAlignAudio": "event:/SFX/Weapons/Gatling/GatlingTurretMove",
  "OnIdleAudio": "event:/SFX/Weapons/Gatling/Turret600Idle",
  "AlignAudioEndParameter": "End",
  "AlignAudioEndValue": 1,
  "AlignAudioStartValue": 0
}
```

Others: `GatlingTurret600_Client_AutoTargetingAudioDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('AutoTargetingAudioDefinitionObjectBuilder')
search_content('', type_contains='AutoTargetingAudioDefinitionObjectBuilder')
```
