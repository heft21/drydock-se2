# PhysicsMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Physics.Definitions.PhysicsMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Definitions`
- definitions using it: **8**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DynamicFriction` | The resistance force that slows bodies down when they are in motion and in contact. Dynamic friction replaces static friction during movement and reverts to static friction when motion ceases. |
| `Restitution` | Determines how much kinetic energy is absorbed during collisions. |
| `StaticFriction` | The resistance force preventing motion when bodies are at rest. Represents how much force is required to overcome static friction and initiate movement. |

## A real one

`Vanilla\Assets\System\Explosions\ProjectileMaterial.def`

```json
{
  "Guid": "cb3c95ed-3d47-4cf7-bd3a-4c845a8a809a",
  "StaticFriction": 0.5,
  "DynamicFriction": 0.5,
  "Restitution": 0
}
```

Others: `GridPhysicsMaterialDefinition`, `MeteorProjectileMaterial`

---

Read it with the MCP server rather than by hand:

```
describe_type('PhysicsMaterialDefinitionObjectBuilder')
search_content('', type_contains='PhysicsMaterialDefinitionObjectBuilder')
```
