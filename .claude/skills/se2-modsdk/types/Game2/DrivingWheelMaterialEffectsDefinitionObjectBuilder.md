# DrivingWheelMaterialEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.DrivingWheelMaterialEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **7**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxRollingSpeed` | Speed at which the rolling particle effects will be played at full intensity. |
| `MinRollingSpeedThreshold` | Speed threshold for rolling particle effects to start playing. |
| `RollingParticleEffect` | Particle effect played while the wheel is rolling normally over the surface with full grip. |
| `SlidingParticleEffect` | Particle effect played during sliding, situations where the wheel loses traction. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\DrivingWheel\DrivingOnGrid.def`

```json
{
  "Guid": "dcc04071-7f2c-4410-86eb-448e1be73034",
  "RollingParticleEffect": "8b6affcf-b96c-47ff-a36e-c3e6d8c8a1ac",
  "SlidingParticleEffect": "2f293a1c-0221-4656-9baf-a99e22a05486",
  "MinRollingSpeedThreshold": 1,
  "MaxRollingSpeed": 20
}
```

Others: `DrivingOnSand`, `DrivingOnSnow`

---

Read it with the MCP server rather than by hand:

```
describe_type('DrivingWheelMaterialEffectsDefinitionObjectBuilder')
search_content('', type_contains='DrivingWheelMaterialEffectsDefinitionObjectBuilder')
```
