# TradingStationDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Economy.TradingStationDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Economy`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Inventories` | Inventories available at different sector progression levels. When an inventory is unlocked by reaching its , the baseline stock values fully replace those of the previous inventory. |
| `SellModifier` | Modifier applied to the item price when selling to this trading station. |
| `StockRecoveryHalfLife` | Time required for the station’s stock and credit balance to return half-way towards their baseline value. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\Trading\TradingStationDefinition.def`

```json
{
  "Guid": "2bfddb5b-bfdf-4733-9050-408aa236a3ec",
  "Inventories": [],
  "SellModifier": 0.5,
  "StockRecoveryHalfLife": 3000000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TradingStationDefinitionObjectBuilder')
search_content('', type_contains='TradingStationDefinitionObjectBuilder')
```
