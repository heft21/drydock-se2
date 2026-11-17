# ConditionalSubPartsDoorPartsProviderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Doors.ConditionalSubPartsDoorPartsProviderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Doors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConditionalSubPartsDefinition` | Definition the subparts are extracted from. |

## A real one

`Vanilla\Assets\Blocks\Doors\SlideDoorNarrow\250\SlidingDoorNarrow250_ConditionalSubPartsDoorPartsProviderDefinition.def`

```json
{
  "Guid": "4f1b003d-304a-4736-b839-7d2d33d3526f",
  "ConditionalSubPartsDefinition": "41d66f39-aedb-4818-954b-1183ba199c65"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ConditionalSubPartsDoorPartsProviderDefinitionObjectBuilder')
search_content('', type_contains='ConditionalSubPartsDoorPartsProviderDefinitionObjectBuilder')
```
