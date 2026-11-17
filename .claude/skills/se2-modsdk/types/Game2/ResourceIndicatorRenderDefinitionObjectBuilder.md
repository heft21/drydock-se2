# ResourceIndicatorRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Render.ResourceIndicatorRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Render`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Indicators` | Collection of resources and the materials they will affect |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\OxygenHydrogen_ResourceIndicatorRenderDefinition.def`

```json
{
  "Guid": "3ba0cc4a-7581-408b-936b-8f93bcbb85fd",
  "ReplacementModels": [],
  "Indicators": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourceIndicatorRenderDefinitionObjectBuilder')
search_content('', type_contains='ResourceIndicatorRenderDefinitionObjectBuilder')
```
