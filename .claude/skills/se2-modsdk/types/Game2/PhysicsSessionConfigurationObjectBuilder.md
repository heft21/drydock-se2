# PhysicsSessionConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Physicss.PhysicsSessionConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Physicss`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AngularDamping` | Angular velocity damping factor |
| `GravityMultiplier` | Gravity multiplier for all physics rigid-bodies excepting characters. Characters use their own gravity multiplier. |
| `LinearDamping` | Linear velocity damping factor |
| `MaximumCharacterSpeedLinear` | The maximum linear speed that is allowed for characters. |
| `MaximumSpeedAngular` | The maximum angular speed that is allowed for all physics bodies except characters. |
| `MaximumSpeedLinear` | The maximum linear speed that is allowed for all physics bodies except characters. |
| `MaximumWheelSpeedAngular` | Maximum angular speed of wheel bodies. Define the max speed the wheeled vehicles can move relative to the surface they roll over. |

## A real one

`Vanilla\Assets\System\Configurations\PhysicsSessionConfiguration.def`

```json
{
  "Guid": "a41c4422-566f-4d10-b51d-a1cce7ed3fbe",
  "MaximumSpeedLinear": 300,
  "MaximumSpeedAngular": 6.28,
  "MaximumCharacterSpeedLinear": 310,
  "LinearDamping": 0,
  "AngularDamping": 0.025,
  "GravityMultiplier": 2,
  "LayersToExcludeFromQueries": [
    {
      "Key": "d984768b-8fff-4998-9089-84ad5ed40aad",
      "Value": "Ragdolls"
    },
    {
      "Key": "3721ade5-9797-4441-a353-9555a6d492ea",
      "Value": "DeadRagdolls"
    }
  ],
  "MassConverterRatio": 1000,
  "PacejkaTireParameters": {
    "LongitudinalCoefficients": {
      "B": 10,
      "C": 1.9,
      "D": 1,
      "E": 0.97
    },
    "LateralCoefficients": {
      "B": 8,
      "C": 1.9,
      "D": 1,
      "E": 0.97
    },
    "LongitudinalPeakFrictionCoefficient": 1,
    "LateralPeakFrictionCoefficient": 1.1
  },
  "MaximumWheelSpeedAngular": 600
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PhysicsSessionConfigurationObjectBuilder')
search_content('', type_contains='PhysicsSessionConfigurationObjectBuilder')
```
