# ModelPhysicsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Game.EntityComponents.ModelPhysicsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.EntityComponents`
- definitions using it: **7**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InheritMotionType` | Set the MotionType in the runtime based on client (Static type) or server (Dynamic type) |

## A real one

`Vanilla\Assets\System\ColonizationMap\ModelPhysicsComponentDefinition.def`

```json
{
  "Guid": "13cd735a-64c6-4fbe-9b00-e6d64c7a36b2",
  "QualityType": "Default",
  "DestructionLayer": "6a9dfefe-2b7b-4bee-b767-cba4b5f54d0e",
  "Material": "a58ad71c-b642-4b3a-a973-86cd61923367",
  "EntityLayer": "ColonizationMapObjects",
  "ActivationControl": "Automatic",
  "MaxDepenetrationSpeed": 1,
  "MotionType": "Static",
  "InheritMotionType": false
}
```

Others: `DamagedBlockDebris_ModelPhysics`, `ServerFloatingObjectsPhysicsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ModelPhysicsComponentDefinitionObjectBuilder')
search_content('', type_contains='ModelPhysicsComponentDefinitionObjectBuilder')
```
