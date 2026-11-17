# InventoryStockpileDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Items.InventoryStockpileDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Items`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FillRatioPull` | The fill ratio (0-1) of the inventory. Stockpiler is trying to keep inventory above this threshold If not set, no pulling will be done |
| `FillRatioPullMargin` | Percentage of of how much to try and fill the inventory above when it falls below. E.g. set to 0 to fill exactly to the ratio, or 0.5 to fill 50% higher. |
| `FillRatioPush` | The fill ratio (0-1) of the inventory. Stockpiler is trying to keep inventory below this threshold. If not set, no pushing will be done |
| `Items` | Collection of items this Stockpiler is reacting to. Pull requests will pull in these items. Push requests will push everything else. |

## A real one

`Vanilla\Assets\Blocks\Welder\350\Welder350InventoryStockpileDefinition.def`

```json
{
  "Guid": "1d389292-3075-4237-a278-0aad0191d493",
  "Items": [],
  "FillRatioPull": null,
  "FillRatioPush": 0.75
}
```

Others: `Grinder350InventoryStockpileDefinition`, `InventoryStockpileDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryStockpileDefinitionObjectBuilder')
search_content('', type_contains='InventoryStockpileDefinitionObjectBuilder')
```
