# JetpackFuelComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.JetpackFuelComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoostFlightFuel` | Character stat used as a fuel source for jetpack boost flight mode |
| `PrecisionFlightFuel` | Character stat used as a fuel source for jetpack precision flight mode |
| `StationaryFuel` | Character stat used as a fuel source for jetpack stationary flight mode |

## A real one

`Vanilla\Assets\Characters\System\JetpackFuelComponentDefinition.def`

```json
{
  "Guid": "c634cbaa-2ab6-424f-a129-99c1428ac2c7",
  "StationaryFuel": {
    "Stat": "675206d7-7a7a-445c-946c-e0a74bbcd862",
    "Amount": 0.285
  },
  "PrecisionFlightFuel": {
    "Stat": "675206d7-7a7a-445c-946c-e0a74bbcd862",
    "Amount": 0.475
  },
  "BoostFlightFuel": {
    "Stat": "fec470a5-43de-4c0d-a712-1bcffd731373",
    "Amount": 3.33
  }
}
```

Others: `NPCJetpackFuelComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('JetpackFuelComponentDefinitionObjectBuilder')
search_content('', type_contains='JetpackFuelComponentDefinitionObjectBuilder')
```
