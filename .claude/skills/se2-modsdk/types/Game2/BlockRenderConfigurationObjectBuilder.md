# BlockRenderConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Render.BlockRenderConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Render`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConstructionColorOverride` | If defined will override block coloring when it is under construction |

## A real one

`Vanilla\Assets\Blocks\BlockRenderConfiguration.def`

```json
{
  "Guid": "18930c16-2bb6-4f58-9706-3271b482c22a",
  "ConstructionColorOverride": {
    "PackedValue": 4283782485
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockRenderConfigurationObjectBuilder')
search_content('', type_contains='BlockRenderConfigurationObjectBuilder')
```
