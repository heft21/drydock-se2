# MechanicalConveyorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Conveyors.MechanicalConveyorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.ResourceDistribution.Conveyors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SubgraphNodeId` | Id of the node in the conveyor subgraph that will be used for linking. |

## A real one

`Vanilla\Assets\Blocks\MechanicalConveyor.def`

```json
{
  "Guid": "1926d161-dab1-46c9-8cb7-9c52235d6940",
  "SubgraphNodeId": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalConveyorDefinitionObjectBuilder')
search_content('', type_contains='MechanicalConveyorDefinitionObjectBuilder')
```
