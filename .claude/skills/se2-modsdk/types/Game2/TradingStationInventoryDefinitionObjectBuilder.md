# TradingStationInventoryDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Economy.TradingStationInventoryDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Economy`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BaseCredits` | Baseline credits that the trading station has. |
| `Items` | Items available in this inventory and their trading parameters. |
| `Stage` | The minimum sector progression required for this inventory to become active. Once the sector's progression reaches or exceeds this value, the items defined in become the station's active inventory, replacing the ones from earlier inventories. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\Trading\TradingStation0nventoryDefinition.def`

Too large to inline. Fields present:

`BaseCredits`, `Guid`, `Items`, `SectorProgressionThreshold`

Others: `TradingStation25InventoryDefinition`, `TradingStation50InventoryDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('TradingStationInventoryDefinitionObjectBuilder')
search_content('', type_contains='TradingStationInventoryDefinitionObjectBuilder')
```
