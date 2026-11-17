# GridInventoryConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.Inventory.GridInventoryConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen.Inventory`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AllConnectedInventoriesKey` | Lockey for the "All connected inventories" secondary filter |
| `AllInventoriesKey` | Lockey for "All Inventories" secondary filter |
| `AllSourcesKey` | Lockey for the "Character + Grids" inventory source |
| `CharacterInventoryKey` | Lockey for the character inventory tag. |
| `CharacterSourceKey` | Lockey for the "Character + Grids" inventory source |
| `DisabledInventoryTooltip` | A tooltip key for the not-connected /not accessible inventories |
| `FilteredInventoryKey` | Lockey indicating no accepting inventory was found on drop target |
| `FullInventoryKey` | Lockey indicating no empty inventory was found on drop target |
| `InventoryMissingKey` | Lockey indicating no inventory was found |
| `NoneFilterKey` | Lockey for the "None" inventory source |
| `ShowAllInventoriesKey` | Lockey for hide empty filter |
| `ShowConnectedInventoriesOnlyKey` | Lockey for show empty filter |
| `ToggleHideEmptyKey` | Lockey for hide empty filter |
| `ToggleShowEmptyKey` | Lockey for show empty filter |

## A real one

`Vanilla\Assets\UI\Screens\GridInventoryConfiguration.def`

```json
{
  "Guid": "fe3a2dbb-0acc-4e93-affc-71a4d8abf255",
  "AllConnectedInventoriesKey": "AllConnectedInventories",
  "CharacterInventoryKey": "CharacterInventory",
  "FilteredInventoryKey": "InventoryFiltered",
  "FullInventoryKey": "InventoryFull",
  "InventoryMissingKey": "InventoryMissing",
  "ToggleShowEmptyKey": "InventoryToggleShowEmpty",
  "ToggleHideEmptyKey": "InventoryToggleHideEmpty"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridInventoryConfigurationObjectBuilder')
search_content('', type_contains='GridInventoryConfigurationObjectBuilder')
```
