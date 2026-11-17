# GravityGeneratorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.RangedAffectGenerators.Gravity.GravityGeneratorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.RangedAffectGenerators.Gravity`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxGravitationalAcceleration` | Max possible value of |
| `MinGravitationalAcceleration` | Min possible value of |

## A real one

`Vanilla\Assets\System\ComponentGravityGenerator.def`

```json
{
  "Guid": "53bae9d7-e0a5-4365-a187-76c49560dada",
  "MaxAffectDistance": 100,
  "MaxGravitationalAcceleration": 9.80665,
  "MinGravitationalAcceleration": -9.80665,
  "GeneratedGravityTypes": "694171c7-d77b-4ab7-aa75-bc20573b6b0a",
  "SupportedGravityShapes": [
    {
      "Key": "11ea1008-9d0e-4764-9a5f-e351427b10ff",
      "Value": "Field"
    },
    {
      "Key": "42ce342f-d4f0-4c8f-a22b-97f59bfe8401",
      "Value": "Spherical"
    },
    {
      "Key": "7898a6fd-e7fa-4827-9ff2-b86dc3643f46",
      "Value": "Cylindrical"
    }
  ]
}
```

Others: `SourceGravityGenerator`, `GravityGeneratorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('GravityGeneratorDefinitionObjectBuilder')
search_content('', type_contains='GravityGeneratorDefinitionObjectBuilder')
```
