# CubeBlockFragilityDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.CubeBlockFragilityDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxHPMassMultiplier` | Multiplier to calculate max health from mass |

## A real one

`Vanilla\Assets\Blocks\Shared\Fragility\Functional.def`

```json
{
  "Guid": "eaaa3a8d-d04c-461f-a7f5-00e8cabd27bd",
  "MaxHPMassMultiplier": 0.8,
  "ProjectileDamage": {
    "FlatDamageReduction": 2.4,
    "DamageMultiplier": 0.5
  },
  "ExplosionDamage": {
    "FlatDamageReduction": 0,
    "DamageMultiplier": 1
  }
}
```

Others: `HeavyArmor`, `LightArmor`

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeBlockFragilityDefinitionObjectBuilder')
search_content('', type_contains='CubeBlockFragilityDefinitionObjectBuilder')
```
