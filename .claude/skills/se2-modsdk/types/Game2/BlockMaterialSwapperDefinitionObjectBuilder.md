# BlockMaterialSwapperDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Render.BlockMaterialSwapperDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Render`
- definitions using it: **20**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `WorkingReplacementModels` | Collection of Models to which the replacements should be applied. will be applied only to Models in this list. |
| `WorkingReplacementsMeshParts` | Collection of Material-Meshpart pairs to be used as replacement. They will be used for all of Models when Working state of block changes. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\BlockMaterialSwapperDefinition.def`

```json
{
  "Guid": "c7218de7-7a48-4954-ba34-e19627f5020a",
  "WorkingReplacementModels": [],
  "WorkingReplacementsMeshParts": []
}
```

Others: `Button25_BlockMaterialSwapperDefinition`, `Smelter250_Client_BlockMaterialSwapperDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockMaterialSwapperDefinitionObjectBuilder')
search_content('', type_contains='BlockMaterialSwapperDefinitionObjectBuilder')
```
