# ColonizationSectorProceduralGenerationDataDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProceduralGeneration.ColonizationSectorProceduralGenerationDataDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProceduralGeneration`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SectorEncounters` | Link a name to procedural encounters. |
| `SectorVolumes` | Link a name to procedural volume. |

## A real one

`Vanilla\Assets\Procedural\VS1_5\System\Data\ColonizationSectorProceduralGenerationDataDefinition.def`

```json
{
  "Guid": "d0d42029-7458-464a-8250-6451ae469a1a",
  "SectorVolumes": {
    "Verdure Sector": "6ec00bfc-2fe1-4716-8a64-f1d8a61cb13e",
    "Kemik Sector": "d2b5bd84-8ec6-4d48-a791-379b95709a6c",
    "Helionis": "3fa3c2dd-c7c6-40f7-ae1d-792a0151807c"
  },
  "SectorEncounters": {
    "Verdure Sector": "680501d2-bc43-417c-8f49-0ab209e3a982",
    "Kemik Sector": "680501d2-bc43-417c-8f49-0ab209e3a982",
    "Helionis": "680501d2-bc43-417c-8f49-0ab209e3a982"
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ColonizationSectorProceduralGenerationDataDefinitionObjectBuilder')
search_content('', type_contains='ColonizationSectorProceduralGenerationDataDefinitionObjectBuilder')
```
