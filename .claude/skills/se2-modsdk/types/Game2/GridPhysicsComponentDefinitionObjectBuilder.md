# GridPhysicsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Physicss.GridPhysicsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Physicss`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HeavyGridEntityLayer` | What entity layer the grid should be if it is a heavy grid |
| `HeavyGridMassThreshold` | How much weight the grid must be to be considered a heavy grid |
| `HitEpsilon` | Epsilon value for pushing raycast result into grid to sample the correct block. |
| `MinimalMassPropertiesUpdateDeviation` | Mass properties deviations under this threshold will be ignored to improve perf |

## A real one

`Vanilla\Assets\System\Grid\GridPhysicsDefinition.def`

```json
{
  "Guid": "25c695fa-fbcd-4d35-ad70-30823298c499",
  "QualityType": "High",
  "DestructionLayer": "a02aebf9-2641-4823-ad2d-edfdc6e3e6de",
  "Material": "2cd1ac9d-c356-44ab-bd8c-156fc04df396",
  "EntityLayer": "Grids",
  "ActivationControl": "Automatic",
  "MaxDepenetrationSpeed": 1,
  "HeavyGridMassThreshold": 50000,
  "HeavyGridEntityLayer": "HeavyGrids"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridPhysicsComponentDefinitionObjectBuilder')
search_content('', type_contains='GridPhysicsComponentDefinitionObjectBuilder')
```
