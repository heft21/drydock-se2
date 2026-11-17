# TerminalScreenViewModelDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.TerminalScreenViewModelDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ContrHintsTitle` | Title of the control hints section |
| `InputLayer` | Input Layer to assign to the TerminalScreen InputContext |
| `ItemTransferAmount10` | Input to transfer 10 units of item to target inventory |
| `ItemTransferAmount100` | Input to transfer 100 units of item to target inventory |
| `ItemTransferDrag` | Input to enable transferring items by dragging between inventories |
| `ItemTransferDrop` | Input to drop an item from the inventory |
| `ItemTransferQuickMove` | Input for quickly moving an item to the target inventory with a double click |
| `MapFadeTransitionTime` | Map Screen duration of fade in and out transition |
| `PreciseItemTransfer` | Input to toggle price item mode transfer, showing the precise transfer window when transferring an item |
| `TerminalInteractPrimary` | Input for primary interaction, such as using an item. |

## A real one

`Vanilla\Assets\UI\Screens\TerminalScreen.def`

```json
{
  "Guid": "2d431a51-6077-49f2-bf64-bcedd362b9cb",
  "ItemTransferAmount10": "36dbabbd-0f8a-43b7-a008-ff4d84f392f5",
  "ItemTransferAmount100": "79fd4b1f-188f-4f2e-b372-2a3a1703ba70",
  "PreciseItemTransfer": "16bade33-69fa-447a-9d49-78196e4397ca",
  "TerminalInteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "ItemTransferDrag": "da3528cf-d157-4541-951d-c07e65afb10a",
  "ItemTransferQuickMove": "707ffbda-062a-4c45-95b6-c0fd870947df",
  "ItemTransferDrop": "eefa4672-f54a-4c29-a85c-9eb1001e908f",
  "UseItem": "cb75a606-2ec5-4b56-af7b-35d0ea9f7bed"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TerminalScreenViewModelDefinitionObjectBuilder')
search_content('', type_contains='TerminalScreenViewModelDefinitionObjectBuilder')
```
