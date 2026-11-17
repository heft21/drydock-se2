# UseItemSlotDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseItemSlotDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FallbackTitle` | Title used for hints. If the action is attached to a block, the block's name will be used instead. |
| `HoverSlotEmpty` | Text shown when the slot does not have an item |
| `HoverSlotHasItem` | Text hint shown when the slot has an item already |

## A real one

`Vanilla\Assets\System\UseActions\UseItemSlotDefinition.def`

```json
{
  "Guid": "32dcafce-fc08-4661-84da-b874a2afba9d",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UseItemSlotAction",
  "HighlightText": "BlankUseActionHighlightText",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "PrimaryScreen": {
    "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+GridScreenSelection",
    "Panel": "Inventory"
  },
  "SecondaryScreen": null,
  "HoverSlotHasItem": "UseItemSlotHasItem",
  "HoverSlotEmpty": "UseItemSlotEmpty",
  "FallbackTitle": "UseItemSlotTitle"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UseItemSlotDefinitionObjectBuilder')
search_content('', type_contains='UseItemSlotDefinitionObjectBuilder')
```
