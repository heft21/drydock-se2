# DoorAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Doors.DoorAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Doors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DoorClosedValue` | Parameter value indicating the door finished closing. |
| `DoorClosingValue` | Parameter value indicating the door started closing. |
| `DoorOpenedValue` | Parameter value indicating the door finished opening. |
| `DoorOpeningValue` | Parameter value indicating the door started opening. |
| `DoorStateParameterName` | Name of the parameter that defines the current door state. |
| `OnDoorStateChangeAudio` | Audio event containing sounds related to door state changes. Actual door state is passed as a parameter . |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DoorAudioDefinition.def`

```json
{
  "Guid": "e7c75a4b-e25c-4101-b3c2-a3d383c68986",
  "OnDoorStateChangeAudio": null,
  "DoorStateParameterName": "DoorState",
  "DoorOpenedValue": "Opened",
  "DoorOpeningValue": "Opening",
  "DoorClosedValue": "Closed",
  "DoorClosingValue": "Closing"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DoorAudioDefinitionObjectBuilder')
search_content('', type_contains='DoorAudioDefinitionObjectBuilder')
```
