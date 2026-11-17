# EventControllerAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar.EventControllerAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Toolbar`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FalseAudio` | Audio event played when the event controller activates the "false" toolbar |
| `TrueAudio` | Audio event played when the event controller activates the "true" toolbar |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\EventController_Client_EventControllerAudioDefinition.def`

```json
{
  "Guid": "699ee417-0349-446b-bc36-745c27af3216",
  "TrueAudio": "event:/SFX/Block/EventControllerTrue",
  "FalseAudio": "event:/SFX/Block/EventControllerFalse"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EventControllerAudioDefinitionObjectBuilder')
search_content('', type_contains='EventControllerAudioDefinitionObjectBuilder')
```
