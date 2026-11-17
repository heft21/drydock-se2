# ConvertGridToDynamicWhenNotAnchoredDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Physicss.ConvertGridToDynamicWhenNotAnchoredDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Physicss`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AnchorLayers` | Entity layers for valid anchors. |
| `MaxBlocksToTest` | Max number of blocks on grid, before the test will be skipped (for perf reasons) |

## A real one

`Vanilla\Assets\System\Grid\ConvertGridToDynamicWhenNotAnchored.def`

```json
{
  "Guid": "377aecb7-0fcf-4e33-a59b-07ecf37ea90d",
  "MaxBlocksToTest": 100000,
  "AnchorLayers": [
    {
      "Key": "e1ddf775-f8d8-4b27-8511-43edc3c51b47",
      "Value": "Voxels"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ConvertGridToDynamicWhenNotAnchoredDefinitionObjectBuilder')
search_content('', type_contains='ConvertGridToDynamicWhenNotAnchoredDefinitionObjectBuilder')
```
