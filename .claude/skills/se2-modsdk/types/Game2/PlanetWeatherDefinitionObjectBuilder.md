# PlanetWeatherDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Weather.PlanetWeatherDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Weather`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BaseSpawnChance` | Baseline probability of spawning a weather event each frame. |
| `DefaultWeatherProbability` | Default weather set for planet. Values are *relative* probabilities, not normalized. |
| `MaxConcurrentEvents` | Maximum number of concurrent weather events on this planet. |
| `MinEventDistance` | Minimum distance between simultaneously active events of any type. |
| `SamePointCooldown` | Minimum time between events at the same lattice point. |
| `SpawnChancePerBiome` | Probability of spawning weather events at a specific biome each frame. |
| `TargetWeatherEventsSpacing` | Drives distances of the points on spawning lattice (approx spacing in meters along surface). |
| `WeatherProbabilityPerBiome` | Weather set to be used on biome - overrides . Values are again relative probabilities. |

## A real one

`Vanilla\Assets\Templates\Planets\PlanetWeatherDefinition.def`

```json
{
  "Guid": "9feb5b0d-1175-48fd-9c19-2a5aed097c55",
  "TargetWeatherEventsSpacing": 10000,
  "BaseSpawnChance": 0.05,
  "SpawnChancePerBiome": {},
  "DefaultWeatherProbability": {
    "_data": []
  },
  "WeatherProbabilityPerBiome": {},
  "SamePointCooldown": 9000000000,
  "MinEventDistance": 6000,
  "MaxConcurrentEvents": 16
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetWeatherDefinitionObjectBuilder')
search_content('', type_contains='PlanetWeatherDefinitionObjectBuilder')
```
