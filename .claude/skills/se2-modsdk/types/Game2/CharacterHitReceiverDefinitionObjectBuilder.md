# CharacterHitReceiverDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.Damage.CharacterHitReceiverDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters.Damage`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ExplosiveDamageSource` | Kind of damage when the character receives damage from explosions |
| `ProjectileDamageSource` | Kind of damage when the character receives damage from projectiles |
| `ReceivedDamageTypeCritical` | Damage type that will be searched for in the projectile damage mapping for critical damage. |

## A real one

`Vanilla\Assets\Characters\System\CharacterHitReceiverDefinition.def`

```json
{
  "Guid": "b6cce423-73c6-47fb-901c-e73db714a328",
  "ReceivedDamageType": "a28e367b-9919-4601-99f6-d333fcbdb0ba",
  "ReceivedDamageTypeCritical": "086749bf-91d2-4089-b62e-71764eb54fc2",
  "ExplosiveDamageSource": "c786264d-41b4-4d21-9d1e-2fd96c6b2466",
  "ProjectileDamageSource": "19b07230-a7eb-400d-aa70-1a4eea2428e5"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterHitReceiverDefinitionObjectBuilder')
search_content('', type_contains='CharacterHitReceiverDefinitionObjectBuilder')
```
