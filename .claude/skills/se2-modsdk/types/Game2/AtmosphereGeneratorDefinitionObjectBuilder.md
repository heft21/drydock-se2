# AtmosphereGeneratorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.RangedAffectGenerators.Atmosphere.AtmosphereGeneratorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.RangedAffectGenerators.Atmosphere`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Density` | Density of the atmosphere |
| `Resource` | What resource is the atmosphere made of? E.g. Oxygen |

## A real one

`Vanilla\Assets\Procedural\VS1_5\System\Data\Planets\PlanetAtmosphereGenerator.def`

```json
{
  "Guid": "1aa2a8aa-3f70-4ed3-916f-edc5a213ff5d",
  "MaxAffectDistance": 3.4028235e+38,
  "Density": 1
}
```

Others: `Palatine_Client_AtmosphereGeneratorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('AtmosphereGeneratorDefinitionObjectBuilder')
search_content('', type_contains='AtmosphereGeneratorDefinitionObjectBuilder')
```
