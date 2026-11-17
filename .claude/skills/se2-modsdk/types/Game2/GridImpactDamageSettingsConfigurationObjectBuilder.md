# GridImpactDamageSettingsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Physicss.GridImpactDamageSettingsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Physicss`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BreakFractureThreshold` | Minimum damage threshold required to cause the block to suffer fracture damage, in percent of the block's max health |
| `DamageDeformationCoefficient` | Deformation strength from impact damage |
| `DamageDeformationFractureThreshold` | Minimum impact damage threshold required to cause the block to deform, in percent of the block's max health |
| `EnableCosmeticDeformations` | Enable cosmetic deformations from impacts |
| `EnableLowQualityCollisionDebugDraw` | Enables or disables debug draw (only visible on the VDB) for low quality destructions. |
| `HealthToBreachImpulse` | Force required to deal damage. |
| `LoddedPenetrationMultiplier` | Penetration multiplier when using Grid Shape Lodding to move planes based on penetration. Planes decide how much destruction there is on each side. |
| `LowQualityCollisionBlockQueryHalfExtents` | Represents the extents of a plane to get all the intersecting blocks from a manifold. When a low LOD collision is processed, a query is dispatched to get the affected blocks for each low detail manifold. This regulates the size of the box that is used to cast a box across the space to find blocks. |
| `MaxCosmeticDeformationImpulse` | The maximum impulse required to trigger the largest cosmetic armor deformation |
| `MinCosmeticDeformationImpulse` | The minimum impulse required to trigger the smallest cosmetic armor deformation |
| `MinCosmeticDeformationSeparationSpeed` | The minimum separation speed to trigger the smallest cosmetic armor deformation |
| `MinimumDestructionSeparationSpeed` | The minimum speed in which destruction can start happening. |
| `PenetrationProportionToDamage` | Proportional damage to deal for penetration. This means that if penetration is equal to "PenetrationToDamage", the full block health is dealt as damage. Damage is calculated as `blockHealth * (penetration / penetrationProportionToDamage)` |
| `SegmentHealthMultiplier` | Temporary multiplier usable until MK4 destructions are done. Health multiplier to apply to armor blocks when computing their breach impulse |

## A real one

`Vanilla\Assets\System\Configurations\GridImpactDamageSettingsConfiguration.def`

```json
{
  "Guid": "19a4beb5-a28f-4ea9-a864-e322fca9e17e",
  "PenetrationProportionToDamage": 0.05,
  "HealthToBreachImpulse": 325,
  "BreakFractureThreshold": 0.02,
  "SegmentHealthMultiplier": 1,
  "MinCosmeticDeformationImpulse": 10000000000000.0,
  "MaxCosmeticDeformationImpulse": 1000000000000000.0,
  "MinCosmeticDeformationSeparationSpeed": 100000000,
  "MinimumDestructionSeparationSpeed": -1,
  "EnableCosmeticDeformations": false,
  "DamageDeformationFractureThreshold": 0.02,
  "DamageDeformationCoefficient": 10,
  "LowQualityCollisionBlockQueryHalfExtents": {
    "X": 10,
    "Y": 10,
    "Z": 0.5
  },
  "EnableLowQualityCollisionDebugDraw": false,
  "LoddedPenetrationMultiplier": 2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridImpactDamageSettingsConfigurationObjectBuilder')
search_content('', type_contains='GridImpactDamageSettingsConfigurationObjectBuilder')
```
