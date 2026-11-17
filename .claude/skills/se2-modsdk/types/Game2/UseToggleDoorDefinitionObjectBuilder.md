# UseToggleDoorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseToggleDoorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HoverDoorClosed` | Interaction hint when the door is closed or closing. |
| `HoverDoorDisabled` | Interaction hint when the door is not working. |
| `HoverDoorOpen` | Interaction hint when the door is open or opening. |

## A real one

`Vanilla\Assets\System\UseActions\UseToggleDoorDefinition.def`

```json
{
  "Guid": "40de9e71-2e4c-4251-a27a-9e5c3448b718",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UseToggleDoorAction",
  "HighlightText": "UseToggleDoor",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "HoverDoorOpen": "UseDoorClose",
  "HoverDoorClosed": "UseDoorOpen",
  "HoverDoorDisabled": "UseDoorDisabled"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UseToggleDoorDefinitionObjectBuilder')
search_content('', type_contains='UseToggleDoorDefinitionObjectBuilder')
```
