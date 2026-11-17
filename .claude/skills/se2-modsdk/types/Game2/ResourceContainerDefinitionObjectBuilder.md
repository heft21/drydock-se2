# ResourceContainerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources.ResourceContainerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ChargeLevelInCreative` | What charge level should this container get when switching to creative mode |
| `InfiniteSourceInCreative` | Should this container supply infinite amount of resources in creative mode |
| `MaxCapacity` | Max capacity of stored resource |
| `MaxChargingRate` | Max rate at which container can be filled (Unit/s) |
| `MaxDischargeRate` | Max rate at which container can be emptied (Unit/s) |
| `ProductionPriority` | Priority of this container in the resource distribution system. The block will act as a buffer for higher priority producers, i.e.: The block will fill from producers with higher priority than itself, and will be used before producers with lower priority to supply consumers when needed. |
| `ResourceType` | Type of stored resource |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\ResourceContainerComponent.def`

```json
{
  "Guid": "0165791c-ece1-4cec-8752-a7c871c66ed4",
  "ResourceType": "bcded093-f5c0-4997-af3a-a6fbd853ad66",
  "ProductionPriority": {
    "Priority": 0
  },
  "MaxCapacity": 0.0005,
  "MaxChargingRate": 0.0003,
  "MaxDischargeRate": 0.0005,
  "InfiniteSourceInCreative": true,
  "ChargeLevelInCreative": null,
  "DisplaySemantics": "ChargeDischarge"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourceContainerDefinitionObjectBuilder')
search_content('', type_contains='ResourceContainerDefinitionObjectBuilder')
```
