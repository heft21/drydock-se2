# RigidBodyComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Physics.Components.RigidBodyComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Components`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActivationControl` | Specifies how the body’s activation state is controlled during simulation. |
| `DestructionLayer` | The physical layer the entity belongs to. Determines how it interacts and breaks in response to physical forces. |
| `EntityLayer` | The layer this entity belongs to, used when determining how it interacts with other physical objects. A list of valid entity layers is configured in the . |
| `Material` | Material properties directly influence how the entity behaves during collisions. |
| `MaxDepenetrationSpeed` | Speed limit for the penetration recovery. When objects end up overlapping due to due to simulation inaccuracies or high-speed interactions, penetration recovery is used to correct this by separating them. This value sets the maximum speed at which such objects are separated. Higher values result in faster separation, but may cause visible "snapping" of objects. Lower values make the correction smoother but may allow overlaps to persist for longer periods. A value of zero disables penetration recovery feature completely. |
| `QualityType` | Collision quality for the rigid body. Higher values reduce simulation artifacts but increase performance costs. |

## A real one

`Vanilla\Assets\System\FractureDebris\RigidBodyComponentDefinition.def`

```json
{
  "Guid": "1937eccc-f372-40ad-a343-e272f721ed86",
  "QualityType": "Default",
  "DestructionLayer": "6a9dfefe-2b7b-4bee-b767-cba4b5f54d0e",
  "Material": "ef57fb74-ea03-438a-84db-ddfc284725ab",
  "EntityLayer": "Debris",
  "ActivationControl": "Automatic",
  "MaxDepenetrationSpeed": 1000000
}
```

Others: `FloraRigidBodyComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('RigidBodyComponentDefinitionObjectBuilder')
search_content('', type_contains='RigidBodyComponentDefinitionObjectBuilder')
```
