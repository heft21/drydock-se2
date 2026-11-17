# CubeGridSplitterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.CubeGridSplitterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlockGridPrefab` | Grid prefab to use when creating the split grid instance |

## A real one

`Vanilla\Assets\System\Grid\BlockGridSplitter.def`

```json
{
  "Guid": "5d7d3c24-05bf-487c-aa72-c15ff8218f74",
  "BlockGridPrefab": "672d6382-207a-498f-a51c-58b370aa96cb"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeGridSplitterDefinitionObjectBuilder')
search_content('', type_contains='CubeGridSplitterDefinitionObjectBuilder')
```
