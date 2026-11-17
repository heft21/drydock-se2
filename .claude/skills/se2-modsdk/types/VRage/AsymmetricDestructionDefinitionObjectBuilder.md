# AsymmetricDestructionDefinitionObjectBuilder

`VRage:Keen.VRage.Physics.BreakHandler.AsymmetricDestructionDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.BreakHandler`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LayersInvulnerableToThisEntity` | Layer filter that matches the entities that will be invulnerable to the entity while it is within the extra safe speed. Entities in these layers will not receive any damage from the entity, if the same layer is not listed in it is possible the entity will receive more damage from these entities. |
| `LayersThisEntityIsInvulnerableTo` | Layer filter that matches the entities the entity will be invulnerable to while in the SafeVelocity. Entities in these layers are still damaged normally (and in fact may receive more damage). |
| `SafeVelocity` | Contact separation velocity up to which the entity is invulnerable, according to the layer filters below. |

## A real one

`Vanilla\Assets\System\Configurations\Flora\Flora AsymmetricDestruction.def`

```json
{
  "Guid": "2bb3ea5a-f7fe-4118-8714-366a7ebf17e7",
  "SafeVelocity": 20,
  "LayersThisEntityIsInvulnerableTo": "3f6993a9-3848-418f-9200-3a93c6412da5",
  "LayersInvulnerableToThisEntity": "af90e171-2da1-4847-8176-041a9ee318fb"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AsymmetricDestructionDefinitionObjectBuilder')
search_content('', type_contains='AsymmetricDestructionDefinitionObjectBuilder')
```
