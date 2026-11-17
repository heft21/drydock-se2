# ConditionalSubPartsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.ConditionalSubPartsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **30**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MeshPartsToHideWhenActive` | Parts to hide on base models when dynamic parts are shown |
| `SubParts` | Parts and their locations designated by dummies |

## A real one

`Vanilla\Assets\Blocks\Gyroscopes\Gyroscopes\250\SubParts.def`

Too large to inline. Fields present:

`Guid`, `MeshPartsToHideWhenActive`, `SubParts`

Others: `Warhead50_ConditionalSubPartsDefinition`, `Grinder350_ConditionalSubPartsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ConditionalSubPartsDefinitionObjectBuilder')
search_content('', type_contains='ConditionalSubPartsDefinitionObjectBuilder')
```
