# UsePlayerActionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UsePlayerActionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\UseActions\UsePlayerActionDefinition.def`

```json
{
  "Guid": "8179c15b-3760-4e0d-98b2-b32204daab72",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UsePlayerAction",
  "HighlightText": "UsePlayer",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "WorkWhenDisabled": true,
  "RequireFacingPlayer": false,
  "Inflation": {
    "X": 0,
    "Y": 0,
    "Z": 0
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UsePlayerActionDefinitionObjectBuilder')
search_content('', type_contains='UsePlayerActionDefinitionObjectBuilder')
```
