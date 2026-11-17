# UsePowerableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UsePowerableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DisableText` | Localization id of hint text to display when the block is currently enabled (and will be disabled by performing this action) |
| `EnableText` | Localization id of hint text to display when the block is currently disabled (and will be enabled by performing this action) |

## A real one

`Vanilla\Assets\System\UseActions\UsePowerableAction.def`

```json
{
  "Guid": "a514581d-b771-4d51-9f37-abf0130000f1",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UsePowerableAction",
  "HighlightText": "BlankUseActionHighlightText",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "EnableText": "UseFunctionalEnable",
  "DisableText": "UseFunctionalDisable"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UsePowerableDefinitionObjectBuilder')
search_content('', type_contains='UsePowerableDefinitionObjectBuilder')
```
