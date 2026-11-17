# ItemToResourceConverterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters.ItemToResourceConverterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.ItemConverters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ItemConsumed` | The item consumed as fuel to produce resources. When configured for a Single Resource, the maximum amount consumed is calculated as: / . When configured for Multiple Resources, instead is used. |
| `MaxItemsPerSecondConsumed` | Maximum rate (units/second) at which items can be consumed to produce resources. |
| `MaxResourceProduction` | Maximum amount of the Single Resource that can be produced per second. |
| `PowerableBlockResourceRequiredToOperate` | Amount of resources/second (of the type used by ) that is required for this converter to function. Has no effect if null, 0, or no is found. Otherwise, will try to consume this amount of resources when actively converting, and stop converting if that demand is not met. |
| `ProductionPriority` | Priority at which the Single Resource is provided to the resource distribution system. |
| `ResourceProduced` | The resource produced. If null, all other Single Resource properties are ignored. |
| `ResourcesPerItem` | Resource production conversion rate for the Single Resource. |
| `ResourcesProduced` | One or more resources that are produced when consuming . Uses as input rate and to calculate maximum production. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ItemToResourceConverter.def`

```json
{
  "Guid": "4f49af74-f6cb-4dc5-93b6-8ed1686688f3",
  "ItemConsumed": null,
  "ResourceProduced": "bcded093-f5c0-4997-af3a-a6fbd853ad66",
  "ProductionPriority": {
    "Priority": 6
  },
  "MaxResourceProduction": 10,
  "ResourcesPerItem": 50
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ItemToResourceConverterDefinitionObjectBuilder')
search_content('', type_contains='ItemToResourceConverterDefinitionObjectBuilder')
```
