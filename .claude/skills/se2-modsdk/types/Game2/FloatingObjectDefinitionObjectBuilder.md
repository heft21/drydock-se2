# FloatingObjectDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.FloatingObjects.FloatingObjectDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.FloatingObjects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoundingBoxDummyType` | Dummy that will be used for computing this object's bounding box. The bounding box is necessary to be affected by gravity with the spatial trigger system. |
| `GravityType` | Gravity type used by this floating object |

## A real one

`Vanilla\Assets\System\FloatingObject.def`

```json
{
  "Guid": "3ca1d421-8159-4c49-976a-edf42f1df05f",
  "BoundingBoxDummyType": "ec312376-e391-4426-8df3-1a894d5a305c",
  "GravityType": "c575aff2-f829-47d2-8315-c81029239ccf"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloatingObjectDefinitionObjectBuilder')
search_content('', type_contains='FloatingObjectDefinitionObjectBuilder')
```
