# WheelCornerModuleDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.WheelCornerModuleDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AxleFriction` | Friction applied to the spinning wheel. Slows down rotation even when the wheel is not in contact with anything. |
| `BrakeDecelerationMultiplier` | Active-brake deceleration rate multiplier. |
| `BrakeGroundSpeedThreshold` | Speed threshold above which the opposite propulsion input is treated as a brake. |
| `MaxSteeringAngle` | Maximum torque applied to the wheel. With ideal traction this represents the acceleration force on the vehicle. |
| `MaxTorque` | Maximum torque applied to the wheel. With ideal traction this represents the acceleration force on the vehicle. |
| `ParkingAngularVelocityThreshold` | The angular velocity below which the parking brake can be engaged for the wheel. |
| `PropulsionController` | When specified, enables the Propulsion Controller — picks the motor velocity target and adapts the torque cap per step based on grip, peer wheels, and configured acceleration rate. |
| `PropulsionResourceConsumption` | Amount of resources consumed while the corner module applies propulsion torque. |
| `SteeringSpeed` | Steering speed, with lower values it takes longer for the wheel to reach max steering angle on steering input. |
| `WheelPivotDummy` | Type of dummy specifying the pivot for physics constraints on both the suspension and the wheel. |
| `WheelPrefab` | Prefab to spawn as a wheel entity. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\WheelCornerModuleDefinition.def`

```json
{
  "Guid": "68685707-cb7e-447a-923b-faf2d659fc84",
  "WheelPrefab": null,
  "WheelPivotDummy": "d1365bc4-d1ca-4280-a3ba-cda3e559a01d",
  "SteeringLimit": 0.5235988,
  "AxleFriction": 500,
  "MaxTorque": 10000,
  "MaxSteeringAngle": 0.34906584,
  "ParkingAngularVelocityThreshold": 0.1,
  "PropulsionController": "9a1c42ac-8254-4cdb-b676-8fbca7b931f3"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WheelCornerModuleDefinitionObjectBuilder')
search_content('', type_contains='WheelCornerModuleDefinitionObjectBuilder')
```
