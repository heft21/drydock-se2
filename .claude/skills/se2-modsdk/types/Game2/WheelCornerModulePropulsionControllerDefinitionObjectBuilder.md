# WheelCornerModulePropulsionControllerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.WheelCornerModulePropulsionControllerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **1**

## What it is

Auto-generated object-builder partial for migration hooks. See .

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DifferentialLockSlack` | Extra headroom the diff-lock cap allows above the slowest grounded peer's spin (target ≤ slowestPeerSpin + VelocityDelta + DifferentialLockSlack). Absorbs legitimate inter-wheel differences from cornering and suspension travel. Larger is more tolerant of normal wheel-rate spread; smaller means tighter coupling, airborne wheels held closer to peers. |
| `MaxAccelerationRate` | Maximum linear acceleration rate of the wheel propulsion, agnostic to the wheel radius. Larger wheels should generally allow higher acceleration. |
| `PropulsionSpeedLimit` | Cannot accelerate the wheel beyond that using propulsion. However, external forces can still make the wheel rotate faster. |
| `RampTime` | How long sustained "stuck" must hold for the torque cap to walk from BaseTorqueFraction * MaxPropulsionTorque all the way to MaxPropulsionTorque. Also acts as the integrator's upper bound. Larger is more conservative, less likely to over-torque on a transient bump; smaller punches through obstacles faster. |
| `SkidBleedHysteresis` | Skid-intensity hysteresis. Skid (the [0,1] loss-of-grip indicator) above this value actively bleeds the torque cap; the same threshold also gates the "stuck" branch (skid must stay below it for the integrator to wind). Larger is more tolerant of slipping; smaller means earlier intervention. |
| `StuckErrorThreshold` | Velocity-gap the wheel must lag its target by before "stuck" can be flagged. Prevents the integrator from winding up on tiny tracking errors. Larger means only large shortfalls (real obstacles) trigger ramp-up; smaller is more sensitive. |
| `VelocityDelta` | Velocity-target carrot length. The motor target is referenceSpin + VelocityDelta (in the throttle-direction frame), so the solver is only ever pulled this far ahead of where the wheel "should" be. Larger means snappier acceleration, more spin headroom before the cap kicks in; smaller means less wheelspin when grip drops out. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\WheelPropulsionControllerDefinition.def`

```json
{
  "Guid": "9a1c42ac-8254-4cdb-b676-8fbca7b931f3",
  "VelocityDelta": 4,
  "DifferentialLockSlack": 1,
  "RampTime": 20000000,
  "StuckErrorThreshold": 2,
  "SkidBleedHysteresis": 0.05,
  "PropulsionSpeedLimit": 50,
  "MaxAccelerationRate": 10
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WheelCornerModulePropulsionControllerDefinitionObjectBuilder')
search_content('', type_contains='WheelCornerModulePropulsionControllerDefinitionObjectBuilder')
```
