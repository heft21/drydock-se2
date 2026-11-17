# SphereShapeEntityDetectorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.EntityDetection.SphereShapeEntityDetectorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.EntityDetection`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `QueryRadius` | Radius of the sphere query |

## A real one

`Vanilla\Assets\Blocks\Welder\350\Welder350SphereShapeEntityDetectorDefinition.def`

```json
{
  "Guid": "96acc475-c9b8-4158-b2cb-aeecb3fbd561",
  "QueryDummy": "fb621cb9-438c-4141-9751-f4a59196658f",
  "MaxSeparatingDistance": 0,
  "QueryRadius": 1.5
}
```

Others: `Welder400SphereShapeEntityDetectorDefinition`, `Grinder350SphereShapeEntityDetectorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('SphereShapeEntityDetectorDefinitionObjectBuilder')
search_content('', type_contains='SphereShapeEntityDetectorDefinitionObjectBuilder')
```
