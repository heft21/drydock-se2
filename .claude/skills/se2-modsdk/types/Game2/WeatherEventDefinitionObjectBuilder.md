# WeatherEventDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Weather.WeatherEventDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Weather`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DurationMax` | Maximum possible duration of the weather event. |
| `DurationMin` | Minimum possible duration of the weather event. |
| `RadiusMax` | Maximum possible radius of the weather event bounding sphere. |
| `RadiusMin` | Minimum possible radius of the weather event bounding sphere. |
| `TransitionMax` | Maximum possible duration of the fade in/out of the weather event. |
| `TransitionMin` | Minimum possible duration of the fade in/out of the weather event. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\WeatherEventDefinition.def`

```json
{
  "Guid": "e735558a-dcbd-4c8a-9107-9e14095f3571",
  "RadiusMin": 1000,
  "RadiusMax": 10000,
  "DurationMin": 600000000,
  "DurationMax": 6000000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WeatherEventDefinitionObjectBuilder')
search_content('', type_contains='WeatherEventDefinitionObjectBuilder')
```
