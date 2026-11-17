# EconomyConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Economy.EconomyConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Economy`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultItemPrices` | Fallback prices for tradable items. Used when a station offers an item that is not set up in its . Items not defined here or in the station's cannot be traded at that station. |
| `DefaultSellModifier` | Default modifier applied to the sell price of an item when sold to a trading station. |

## A real one

`Vanilla\Assets\System\Configurations\EconomyConfiguration.def`

```json
{
  "Guid": "674c9f86-23b1-48b6-b370-0b31271cff6a",
  "DefaultSellModifier": 0.8,
  "DefaultItemPrices": {
    "b51dc4d7-aaeb-4116-9f82-d54a33fe4b0a": 5,
    "c584e5cf-7640-47a1-851f-8b72cdfdb5f3": 14,
    "4cd573d9-f760-47f8-bdfd-0c998136f301": 20
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EconomyConfigurationObjectBuilder')
search_content('', type_contains='EconomyConfigurationObjectBuilder')
```
