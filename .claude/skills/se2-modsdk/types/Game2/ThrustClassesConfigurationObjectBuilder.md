# ThrustClassesConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Movement.ThrustClassesConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Movement`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ThrustClasses` | Defines different thruster classes that are used to describe thrusters behaviour |

## A real one

`Vanilla\Assets\System\Configurations\ThrustClassesConfiguration.def`

```json
{
  "Guid": "586e1207-50df-4982-9afd-63a15f5d0d1f",
  "ThrustClasses": [
    {
      "$Key": "Ion",
      "$Value": {
        "MaxThrustAirDensity": 0.2,
        "MinThrustAirDensity": 0.8,
        "WaterSubmersionTolerance": 1,
        "WaterOnly": false
      }
    },
    {
      "$Key": "Atmospheric",
      "$Value": {
        "MaxThrustAirDensity": 0.8,
        "MinThrustAirDensity": 0.2,
        "WaterSubmersionTolerance": 1,
        "WaterOnly": false
      }
    },
    {
      "$Key": "Hydrogen",
      "$Value": {
        "MaxThrustAirDensity": 0,
        "MinThrustAirDensity": -1,
        "WaterSubmersionTolerance": 1,
        "WaterOnly": false
      }
    },
    {
      "$Key": "Water",
      "$Value": {
        "MaxThrustAirDensity": 0,
        "MinThrustAirDensity": -1,
        "WaterSubmersionTolerance": 1,
        "WaterOnly": true
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ThrustClassesConfigurationObjectBuilder')
search_content('', type_contains='ThrustClassesConfigurationObjectBuilder')
```
