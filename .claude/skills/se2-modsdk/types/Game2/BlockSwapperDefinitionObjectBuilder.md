# BlockSwapperDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.BlockSwapperDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `IntegrityThreshold` | Block build progress threshold above or under which swap can happen. |
| `SwappedBlock` | Prefab to replace the block by when swap condition is met |
| `TriggerAboveThreshold` | Specifies how to interpret . True: swap condition is reached whenever block build progress is above False: swap condition is reached whenever block build progress is below or equal to |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\BlockSwapperDefinition.def`

```json
{
  "Guid": "13be8917-239b-43ec-b6df-ed3559ae4fd4",
  "SwappedBlock": null,
  "TriggerAboveThreshold": false,
  "IntegrityThreshold": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockSwapperDefinitionObjectBuilder')
search_content('', type_contains='BlockSwapperDefinitionObjectBuilder')
```
