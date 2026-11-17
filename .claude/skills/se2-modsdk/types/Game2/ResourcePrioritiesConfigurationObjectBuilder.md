# ResourcePrioritiesConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources.ResourcePrioritiesConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxConsumerPriority` | Maximum priority value for consumers. Minimum is always 0. Higher values mean higher priority. High-priority consumers will be supplied before lower-priority ones. |
| `MaxProducerPriority` | Maximum priority value for producers. Minimum is always 0. Higher values mean higher priority. High-priority producers will be used before lower-priority ones. |

## A real one

`Vanilla\Assets\System\Configurations\ResourcePrioritiesConfiguration.def`

```json
{
  "Guid": "7b18ac8b-dca3-40cb-b5db-e1cbe20fbe8c",
  "MaxProducerPriority": 10,
  "MaxConsumerPriority": 10
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourcePrioritiesConfigurationObjectBuilder')
search_content('', type_contains='ResourcePrioritiesConfigurationObjectBuilder')
```
