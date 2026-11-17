# SectorStageDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Colonization.SectorStageDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Colonization`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Name` | Stage name. |

## A real one

`Vanilla\Assets\Colonization\VS2-3\Sectors\Survival_SectorStage_Settled.def`

```json
{
  "Guid": "dda10f29-89a1-403f-8611-9aed4c9bdaf4",
  "Name": "StageSettled"
}
```

Others: `Survival_SectorStage_Explored`, `Survival_SectorStage_Colonized`

---

Read it with the MCP server rather than by hand:

```
describe_type('SectorStageDefinitionObjectBuilder')
search_content('', type_contains='SectorStageDefinitionObjectBuilder')
```
