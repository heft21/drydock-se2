# ResourceContainerInventoryDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources.ResourceContainerInventoryDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Battery_ResourceContainerInventoryDefinition.def`

```json
{
  "Guid": "ee213cd7-34c7-4cfc-8c0d-586c28a6e2d9",
  "ResourceType": "bcded093-f5c0-4997-af3a-a6fbd853ad66",
  "ProductionPriority": {
    "Priority": 5
  },
  "MaxCapacity": 1000,
  "MaxChargingRate": 998,
  "MaxDischargeRate": 999,
  "InfiniteSourceInCreative": true,
  "ChargeLevelInCreative": null,
  "DisplaySemantics": "ChargeDischarge"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourceContainerInventoryDefinitionObjectBuilder')
search_content('', type_contains='ResourceContainerInventoryDefinitionObjectBuilder')
```
