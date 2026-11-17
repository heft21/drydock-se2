# ItemConverterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters.ItemConverterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumedResource` | Additional amount of that is applied when a recipe is running. |
| `EfficiencyMultiplier` | Modifer that alters the amount of items produced |
| `MaxQueueSize` | The maximum amount of item recipes that can be queued |
| `RecipeDefinitions` | Collection of tabs and recipes definitions the item converter can produce. Lets you combine the recipes of basic refinery and advanced refinery, for example. |
| `RemoveImpossibleRecipes` | If true, any recipe that can't be completed will be removed from the queue |
| `SpeedMultiplier` | Modifier that alters the speed items are converted |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ItemConverterDefinition.def`

```json
{
  "Guid": "cb369927-350d-4a32-9e61-1b31bf69cb48",
  "SpeedMultiplier": 1,
  "EfficiencyMultiplier": 1,
  "RecipeDefinitions": {},
  "MaxQueueSize": 0,
  "RemoveImpossibleRecipes": false,
  "ConsumedResource": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ItemConverterDefinitionObjectBuilder')
search_content('', type_contains='ItemConverterDefinitionObjectBuilder')
```
