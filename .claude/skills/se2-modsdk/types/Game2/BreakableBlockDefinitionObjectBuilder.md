# BreakableBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.BreakableBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CriticalFractures` | List of fractures deemed critical to the proper function of the block. If the block loses any fracture listed here, it will stop functioning. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\BreakableBlockDefinition.def`

```json
{
  "Guid": "a74c6fd1-fa39-4f24-89cb-17a46e65cfd7",
  "CriticalFractures": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BreakableBlockDefinitionObjectBuilder')
search_content('', type_contains='BreakableBlockDefinitionObjectBuilder')
```
