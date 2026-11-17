# BoxShapeEntityDetectorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.EntityDetection.BoxShapeEntityDetectorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.EntityDetection`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `QueryHalfExtents` | Half size of the box used for Entity detection. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\BoxShapeEntityDetectorDefinition.def`

```json
{
  "Guid": "bb790a35-03fb-4c00-b94e-71b8602f933c",
  "QueryDummy": "0f691446-2a65-4c42-8c33-052d16cafb34",
  "MaxSeparatingDistance": 0,
  "QueryHalfExtents": {
    "X": 0,
    "Y": 0,
    "Z": 0
  }
}
```

Others: `Welder350DamageBoxShapeEntityDetectorDefinition`, `Welder400DamageBoxShapeEntityDetectorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BoxShapeEntityDetectorDefinitionObjectBuilder')
search_content('', type_contains='BoxShapeEntityDetectorDefinitionObjectBuilder')
```
