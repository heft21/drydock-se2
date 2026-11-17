# TimerBlockAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar.TimerBlockAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TimerEnd` | Audio event played when the timer finishes counting down |
| `TimerLoop` | Audio event looped while the timer is counting down |
| `TimerStart` | Audio event played when the timer starts counting down |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Timers_Client_TimerBlockAudioDefinition.def`

```json
{
  "Guid": "899e374f-41a6-446a-a26c-446c6e658c73",
  "TimerStart": "event:/SFX/Block/TimerStart",
  "TimerLoop": "event:/SFX/Block/TimerRunning",
  "TimerEnd": "event:/SFX/Block/TimerEnd"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TimerBlockAudioDefinitionObjectBuilder')
search_content('', type_contains='TimerBlockAudioDefinitionObjectBuilder')
```
