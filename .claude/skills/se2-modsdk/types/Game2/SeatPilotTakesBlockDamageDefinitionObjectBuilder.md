# SeatPilotTakesBlockDamageDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Pilotable.SeatPilotTakesBlockDamageDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Pilotable`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DamageMultiplier` | How much of damage dealt to the block is also dealt to the pilot. This multiplier is applied after subtracting from the incoming damage. |
| `DamageSource` | Damage source description for damage dealt to a pilot when the block takes damage. |
| `MinimumDamage` | Minimum damage the block needs to take in a single event (like a collision, projectile hit, or explosion) for the pilot to also take damage. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\SeatPilotTakesBlockDamageDefinition.def`

```json
{
  "Guid": "4f085ded-4032-4c6f-b9f2-95c059bc8542",
  "MinimumDamage": 100,
  "DamageMultiplier": 0.1,
  "DamageSource": "71f8b73e-6081-4bd4-95ed-4437802150e3"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SeatPilotTakesBlockDamageDefinitionObjectBuilder')
search_content('', type_contains='SeatPilotTakesBlockDamageDefinitionObjectBuilder')
```
