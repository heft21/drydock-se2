# GameProceduralGenerationConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProceduralGeneration.GameProceduralGenerationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProceduralGeneration`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SectorGeneration` | Definition to use for new world. |

## A real one

`Vanilla\Assets\Procedural\VS1_5\System\Data\GameProceduralGenerationConfiguration.def`

```json
{
  "Guid": "c41f9d1b-fadf-4fd0-8cb2-a13939e83f04",
  "SectorGeneration": "d0d42029-7458-464a-8250-6451ae469a1a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GameProceduralGenerationConfigurationObjectBuilder')
search_content('', type_contains='GameProceduralGenerationConfigurationObjectBuilder')
```
