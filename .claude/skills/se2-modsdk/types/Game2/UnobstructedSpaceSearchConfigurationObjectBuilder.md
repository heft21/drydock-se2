# UnobstructedSpaceSearchConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Physicss.UnobstructedSpaceSearchConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Physicss`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `IterationsPerDistance` | Number of iterations performed in each test on each distance step to find a valid position |
| `MaxTestCount` | Maximum count of tests to be performed to find a valid position. |
| `StepDistance` | Step distance between each test to find a valid position. |

## A real one

`Vanilla\Assets\System\UnobstructedSpaceSearchConfiguration.def`

```json
{
  "Guid": "02052d48-15b2-4246-bbda-e6588d69f2fc",
  "IterationsPerDistance": 100,
  "StepDistance": 0.25,
  "MaxTestCount": 100
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UnobstructedSpaceSearchConfigurationObjectBuilder')
search_content('', type_contains='UnobstructedSpaceSearchConfigurationObjectBuilder')
```
