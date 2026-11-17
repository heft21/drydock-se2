# CubeBlockRecipeRoundingConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.CubeBlockRecipeRoundingConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Thresholds` | Must contain exactly 4 rounding thresholds. The starting threshold must have an amount of 0. |

## A real one

`Vanilla\Assets\Blocks\Shared\Recipes\RecipeRoundingThresholds.def`

```json
{
  "Guid": "d8563d25-3ede-4964-8c0e-b36560bd15e7",
  "Thresholds": [
    {
      "Key": "62b39c80-23ef-4dd5-9cc9-43064c20e8ed",
      "Value": {
        "Amount": 0,
        "Multiple": 1
      }
    },
    {
      "Key": "b664ad88-7e84-4ab2-b150-72e3767a2690",
      "Value": {
        "Amount": 20,
        "Multiple": 5
      }
    },
    {
      "Key": "ac265940-ed7a-4cda-bdea-98fb3c956e70",
      "Value": {
        "Amount": 100,
        "Multiple": 10
      }
    },
    {
      "Key": "9777c78a-3409-48ba-8ff5-2dc50bf5042b",
      "Value": {
        "Amount": 1000,
        "Multiple": 100
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeBlockRecipeRoundingConfigurationObjectBuilder')
search_content('', type_contains='CubeBlockRecipeRoundingConfigurationObjectBuilder')
```
