# ResourceTypeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources.ResourceTypeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Resources`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FlowRateUnits` | Units in which this resource is presented to the player (e.g. kW, liters per second, etc.) Used for flow, such as reactor output or input for thrusters. |
| `Name` | A unique name of the resource |
| `RequiresConveyors` | Whether resource is omnipresent on the grid (Electricity) or supplied only via Conveyors (Gases, Water). Blocks using Conveyorable resources must be conveyor-capable. |
| `StorageUnits` | Units in which this resource is presented to the player (e.g. Newtons, Liters, Bytes, etc.). Used for storage, such as containers or tanks. |

## A real one

`Vanilla\Assets\System\ResourceTypes\Water.def`

```json
{
  "Guid": "aae86c3c-0405-47c7-acf2-b4d9baf9a182",
  "Name": "ResourceWater",
  "FlowRateUnits": "LitersPerSecond",
  "StorageUnits": "Liters",
  "RequiresConveyors": true
}
```

Others: `Oxygen`, `Hydrogen`

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourceTypeDefinitionObjectBuilder')
search_content('', type_contains='ResourceTypeDefinitionObjectBuilder')
```
