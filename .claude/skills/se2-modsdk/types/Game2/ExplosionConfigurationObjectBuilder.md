# ExplosionConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Explosions.ExplosionConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Explosions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BaseVoxelDamageToProjectiles` | Base, damage voxels do to the projectile on impact, further modified by difference in hardness. |
| `DamageTypeToImpulseCoefficient` | Mapping of the impulse applied by explosions to coefficient that multiplies the damage to create impulse. |
| `VoxelHardnessFallOffExponent` | How much will the radius reduction fall off from effective material hardness. |

## A real one

`Vanilla\Assets\System\Configurations\ExplosionConfiguration.def`

```json
{
  "Guid": "d97af0ef-3aa8-4ec6-8d29-c786b2e3dc20",
  "DamageTypeToImpulseCoefficient": {
    "235c92de-c788-46f2-aab0-972b2e305115": 1,
    "a28e367b-9919-4601-99f6-d333fcbdb0ba": 25,
    "9fc2643b-1e26-4aa6-957d-e72b7292d505": 3,
    "1a83ac16-b2e3-4fa5-869f-fa1cd63b290e": 25
  },
  "VoxelHardnessFallOffExponent": 2,
  "BaseVoxelDamageToProjectiles": 50,
  "ExplosionStimulusIntensity": 1,
  "ExplosionStimulusRadiusMultiplier": 1.5,
  "ExplosionStimulusMinRadius": 15,
  "ExplosionStimulusCategory": "Audio"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ExplosionConfigurationObjectBuilder')
search_content('', type_contains='ExplosionConfigurationObjectBuilder')
```
