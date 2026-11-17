# MovementDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Shared.Movement.MovementDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Shared.Movement`
- definitions using it: **2**

## What it is

Migration for moving flat rotation properties into AngularGyroRotation and TargetGyroRotation structs.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AngularGyroRotation` | Rotation settings for the angular velocity-based gyroscope system. |
| `MinSpeed` | Absolute minimum speed the ship/character can be (per X/Y/Z direction) after thrust is applied. The speed gets set to zero if the speed is less than this. This is necessary due to floating point precision. |
| `MinThrusterAccelerationRatio` | The amount of acceleration when the character/ship is at the soft speed limit. Does not apply when there is not a soft speed limit. |
| `TargetGyroRotation` | Rotation settings for the target/reticle-based gyroscope system. |
| `ThrusterAccelerationBias` | Amount of bias given to the falloff. Does not apply when there is not a soft speed limit. If the speed limit is 10ms, and the bias is 0.25, the player will have max acceleration until they go past 2.5ms |
| `ThrusterAccelerationSpeedLimitFalloff` | Changes how the acceleration falls off (exponent) as the character/ship moves closer to the soft speed limit. Does not apply when there is not a soft speed limit. |
| `ThrusterBrakingPowerMultiplierMax` | Maximum value of the thrust power multiplier when braking in comparison to normal thrust. For example, a value of 2 will brake with twice as much power as the normal thrust. Braking is also affected by grid's current velocity in said direction, this multiplier is applied close to max speed. Linearly interpolated with for lower speeds. |
| `ThrusterBrakingPowerMultiplierMin` | Minimum value of the thrust power multiplier when braking in comparison to normal thrust. For example, a value of 2 will brake with twice as much power as the normal thrust. Braking is also affected by grid's current velocity in said direction, this multiplier is applied close to 0 speed. Linearly interpolated with for higher speeds. |
| `ThrusterDampenerCurveMinSpeed` | The minimum speed the character/ship can be before the dampening thrust curve applies. If the speed is below this value, the full thrust will be applied. This helps prevent the entity from thrusting/drifting forever. |
| `ThrusterDampenerMaxSpeedFactor` | Upper-bound speed factor used in thrust dampening smoothing calculation. This affects how quickly the dampening will reduce the speed of the entity The larger the value, the faster the entity will decelerate towers lower velocity range |
| `ThrusterDampenerMaxSpeedLimitFactor` | Affects how dampening occurs when reaching or above the soft speed limit, if there is one. |
| `ThrusterDampenerMinSpeedFactor` | Lower-bound speed factor used in thrust dampening smoothing calculation. This affects the "long tail" part of the dampening. The smaller the value, the longer the entity will slowly drift until it reaches full stop |
| `ThrusterDampenerMinSpeedLimitFactor` | Affects how dampening occurs when reaching or above the soft speed limit, if there is one. |
| `ThrusterDecelerationSpeedLimitFalloff` | Changes how the dampeners fall off (exponent) as the character/ship slows down. |
| `UseDampenersWorldOption` | When true, the dampener's ( and ) settings can be ignored by |

## A real one

`Vanilla\Assets\System\Grid\Grid_MovementDefinition.def`

```json
{
  "Guid": "4a112f9b-57f8-4d0c-9c52-078c364084f1",
  "ThrusterBrakingPowerMultiplierMin": 2,
  "ThrusterBrakingPowerMultiplierMax": 5,
  "ThrusterDampenerMinSpeedFactor": 1.75,
  "ThrusterDampenerMaxSpeedFactor": 65,
  "ThrusterDampenerCurveMinSpeed": 0.01,
  "ThrusterDecelerationSpeedLimitFalloff": 2,
  "ThrusterAccelerationSpeedLimitFalloff": 3,
  "ThrusterAccelerationBias": 0.1,
  "MinThrusterAccelerationRatio": 0.25,
  "ThrusterDampenerMinSpeedLimitFactor": 10,
  "ThrusterDampenerMaxSpeedLimitFactor": 300,
  "MinSpeed": 0.005,
  "TorqueDampenerPowerMultiplier": 0.25,
  "MaximumTorqueLimiterCoefficient": 0.01,
  "RollDampenerPowerMultiplier": 1,
  "MaximumAngularDeceleration": 6.28,
  "AngularEaseOutSpeedThreshold": 0.2,
  "AngularEaseOutMinimum": 0.8
}
```

Others: `Character_MovementDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('MovementDefinitionObjectBuilder')
search_content('', type_contains='MovementDefinitionObjectBuilder')
```
