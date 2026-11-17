# ProductionBlockProgressionCheckpointDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Progression.ProductionBlockProgressionCheckpointDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Progression`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `UnlockingBlocks` | For stringification via , use block indices or -1 for all blocks. |

## A real one

`Vanilla\Assets\System\Progression\SmelterProgressionCheckpoint.def`

```json
{
  "Guid": "21c0af93-e087-473b-b600-b90ebd3d9fbd",
  "DisplayString": "SmelterProgression",
  "DisplayStringConcise": "SmelterProgressionConcise",
  "UnlockingBlocks": [
    {
      "Key": "d478462e-d5be-4559-a997-0a0fbf2e3bd1",
      "Value": "92b17abc-6ce2-4e33-b917-64e9b847ce5d"
    }
  ]
}
```

Others: `RefineryProgressionCheckpoint`, `AssemblerProgressionCheckpoint`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProductionBlockProgressionCheckpointDefinitionObjectBuilder')
search_content('', type_contains='ProductionBlockProgressionCheckpointDefinitionObjectBuilder')
```
