# InventoryDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Items.InventoryDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Items`
- definitions using it: **20**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ExcludeFromCapacityStats` | If true, this inventory will not contribute to capacity/fullness statistics displayed in the HUD. Useful for secondary inventories like consumables or datapads that shouldn't affect the main capacity indicator. |
| `InventoryName` | Optional name for the inventory to display in terminal. Use {Entity} as placeholder for entity name. |
| `MaxMass` | Max mass of the Inventory |
| `MaxStacks` | If not null, limit the total number of stacks for this inventory |
| `PreventStockpilingFromAddingItems` | If true, will not push items to this inventory. Recommended for output inventories, so that competing blocks do not push into it. |
| `PreventStockpilingFromRemovingItems` | If true, will not take items from this inventory. Recommended for input inventories, so that competing blocks do not steal each other's resources. |
| `WhitelistedItems` | Static item filter. If empty, all items can fit. If not empty, only items with matching definitions can fit in. |
| `WhitelistedTypes` | Static item filter. Items are filtered based on their type |

## A real one

`Vanilla\Assets\Characters\System\CharacterInventory.def`

```json
{
  "Guid": "fe9df47f-5673-4253-b797-54635d4f3f42",
  "MaxStacks": null,
  "MaxMass": 8400,
  "WhitelistedItems": [],
  "WhitelistedTypes": "Ore, Material, Component, Item",
  "InventoryName": "CharacterInventoryName",
  "PreventStockpilingFromRemovingItems": false,
  "PreventStockpilingFromAddingItems": false,
  "ExcludeFromCapacityStats": false
}
```

Others: `DatapadInventoryDefinition`, `QuestItemInventoryDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryDefinitionObjectBuilder')
search_content('', type_contains='InventoryDefinitionObjectBuilder')
```
