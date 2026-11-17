# CameraShakeConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.CameraShake.CameraShakeConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.CameraShake`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AccelerationShakeEnabled` | Enables camera shakes induced by changes in character or grid speed. |
| `AnimationEventShakes` | When an animation event of the given name is invoked, the shake will be applied. |
| `CharacterMaxContact` | Amount of character contact force that will produce the strongest camera shake response |
| `CharacterMaxDamage` | Amount of character damage that will produce the strongest camera shake response |
| `CharacterMinContactFlying` | Minimum character contact force required to generate a camera shake response when the character is flying/not grounded |
| `CharacterMinContactGrounded` | Minimum character contact force required to generate a camera shake response when the character is grounded |
| `CharacterMinDamage` | Minimum damage that the character should receive to produce a shake response. Instant damage values below this threshold will not shake the character's camera |
| `ChargeBoostMaxShake` | Shake applied when jetpack boost finishes charging, used for linear interpolation from during charge progress (percent of ) |
| `ChargeBoostMinShake` | Shake applied when jetpack boost starts charging, used for linear interpolation to during charge progress (percent of ) |
| `GridContactMassFalloff` | Mass of ship before contact shakes begin to fall off/fade out. Falloff occurs using inverse square root. For example: * A ship with half the mass of will have maximum shake power * A ship with mass equal to will have maximum shake power * A ship with double the mass of will have about 0.7x shake power (1/sqrt(2)) |
| `GridExplosionShakeIntensityModifier` | Modifier applied to all explosion shake intensity |
| `GridMaxContact` | Amount of grid vs grid contact force that will produce the strongest camera shake response |
| `GridMaxExplosionDamage` | Explosion damage to receive on grid that will result in maximum shake intensity |
| `GridMinContact` | Minimum grid contact force required to generate a camera shake response |
| `GridMinExplosionDamage` | Minimum explosion damage to receive on grid to cause shake |
| `RotationalShakeEnabled` | Enables rotational camera shake. |

## A real one

`Vanilla\Assets\System\Camera\CameraShakeConfiguration.def`

```json
{
  "Guid": "76701208-92a1-46c5-bbcf-84444e37c9fa",
  "CharacterMinDamage": 5,
  "CharacterMaxDamage": 90,
  "CharacterKickMaxDamage": 5,
  "CharacterDamageShakeMultiplier": 1,
  "GridMinExplosionDamage": 5,
  "GridMaxExplosionDamage": 750,
  "GridExplosionShakeIntensityModifier": 0.5,
  "ChargeBoostMinShake": 0,
  "ChargeBoostMaxShake": 1.75,
  "CharacterMinContactGrounded": 999999,
  "CharacterMinContactFlying": 2,
  "AnimationEventShakes": [
    {
      "$Key": "Landing",
      "$Value": {
        "ScaleByWeight": false,
        "MinWeight": 0,
        "BaseShake": 3
      }
    },
    {
      "$Key": "HeavyLanding",
      "$Value": {
        "ScaleByWeight": false,
        "MinWeight": 0,
        "BaseShake": 8
      }
    }
  ],
  "CharacterMaxContact": 30,
  "GridMinContact": 1,
  "GridMaxContact": 30,
  "GridContactMassFalloff": 100000,
  "AccelerationShakeEnabled": true,
  "RotationalShakeEnabled": true,
  "CharacterKickEnabled": true
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraShakeConfigurationObjectBuilder')
search_content('', type_contains='CameraShakeConfigurationObjectBuilder')
```
