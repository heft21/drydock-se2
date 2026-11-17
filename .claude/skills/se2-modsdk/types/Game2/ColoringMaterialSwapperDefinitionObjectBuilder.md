# ColoringMaterialSwapperDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Render.ColoringMaterialSwapperDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Render`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BrightnessMultiplier` | How much the brightness of the light should be multiplied to get the emissive amount. Best left at 1 in most cases. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ColoringMaterialSwapperDefinition.def`

```json
{
  "Guid": "545836c3-b5fe-489f-baf1-fc14d8b26a77",
  "WorkingReplacementModels": [],
  "WorkingReplacementsMeshParts": [],
  "BrightnessMultiplier": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ColoringMaterialSwapperDefinitionObjectBuilder')
search_content('', type_contains='ColoringMaterialSwapperDefinitionObjectBuilder')
```
