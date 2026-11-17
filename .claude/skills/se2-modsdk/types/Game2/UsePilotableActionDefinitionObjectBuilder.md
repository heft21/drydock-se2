# UsePilotableActionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UsePilotableActionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\UseActions\UsePilotableAction.def`

```json
{
  "Guid": "a3412971-c399-4aac-a1c0-51318f411c7f",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UsePilotableAction",
  "HighlightText": "UsePilotable",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "OccupiedText": "UsePilotableOccupied"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UsePilotableActionDefinitionObjectBuilder')
search_content('', type_contains='UsePilotableActionDefinitionObjectBuilder')
```
