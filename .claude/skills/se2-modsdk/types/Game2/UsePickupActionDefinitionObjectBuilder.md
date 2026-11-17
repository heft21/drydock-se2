# UsePickupActionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UsePickupActionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InventoryFullLocKey` | Localization key for when the character inventory is full. |
| `InventoryInsufficientSlots` | Localization key for when there is no available slot in the inventory to recive the item. |

## A real one

`Vanilla\Assets\System\UseActions\UsePickupAction.def`

```json
{
  "Guid": "9a797703-5cab-43bb-840a-8fb9aa4a4013",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UsePickupAction",
  "HighlightText": "UsePickup",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "InventoryFullLocKey": "UsePickupInventoryFull",
  "InventoryInsufficientSlots": "UsePickupInsufficientFull"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UsePickupActionDefinitionObjectBuilder')
search_content('', type_contains='UsePickupActionDefinitionObjectBuilder')
```
