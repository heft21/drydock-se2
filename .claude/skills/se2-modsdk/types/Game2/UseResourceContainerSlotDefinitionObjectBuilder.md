# UseResourceContainerSlotDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseResourceContainerSlotDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HoverSlotEmptyRecharge` | Text shown when the slot does not have an item and the container is in recharge mode. |
| `PushBestError` | Text shown when an item could not be pushed into the slot |

## A real one

`Vanilla\Assets\System\UseActions\UseBatterySlot(PowerModules)Definition.def`

```json
{
  "Guid": "be2867f3-78b8-4a8d-95cc-9d35d788b68b",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UseResourceContainerSlotAction",
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
  "HoverSlotEmpty": "UsePowerModuleSlotEmpty",
  "FallbackTitle": "UsePowerCellSlotTitle",
  "HoverSlotEmptyRecharge": "UsePowerModuleSlotEmptyRecharge",
  "PushBestError": "UsePowerModuleSlotPushError"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UseResourceContainerSlotDefinitionObjectBuilder')
search_content('', type_contains='UseResourceContainerSlotDefinitionObjectBuilder')
```
