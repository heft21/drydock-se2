# WeatherResourceEffectorGeneratorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.RangedAffectGenerators.Weather.WeatherResourceEffectorGeneratorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.RangedAffectGenerators.Weather`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SolarOutputModifier` | The solar output modifier when weather intensity is at maximum (1.0). Value of 0.0 means solar panels produce no power during peak weather. Value of 0.5 means solar panels produce 50% power during peak weather. Value of 1.0 means weather has no effect on solar output. |
| `WindIntensityModifier` | The wind intensity modifier when weather intensity is at maximum (1.0). This quantifies how intense the wind is during weather events, and affects systems that depend on weather like wind turbines. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\WeatherResourceEffectorGeneratorDefinition.def`

```json
{
  "Guid": "e6d819e5-4d68-4ee6-9a7d-ea3969e105fa",
  "MaxAffectDistance": 100000,
  "SolarOutputModifier": 1,
  "WindIntensityModifier": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WeatherResourceEffectorGeneratorDefinitionObjectBuilder')
search_content('', type_contains='WeatherResourceEffectorGeneratorDefinitionObjectBuilder')
```
