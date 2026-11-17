# DrillShakeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillShakeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Impulse` | Impulse applied by the shake |
| `PeriodA` | Time multiplier for the up/down movement of the drill. Higher number means slower change of shakes |
| `PeriodB` | Time multiplier for the left/right movement of the drill. Higher number means slower change of shakes |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DrillShakeDefinition.def`

```json
{
  "Guid": "720231c4-6d0e-4b8c-b887-a64ab19448b2",
  "PeriodA": 2670,
  "PeriodB": 3630.7998,
  "Impulse": 25000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillShakeDefinitionObjectBuilder')
search_content('', type_contains='DrillShakeDefinitionObjectBuilder')
```
