# WeaponConvergeGridDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Weapons.WeaponConvergeGridDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Weapons`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConvergenceSmoothStepDistance` | Distance from or where convergence is smoothly transitioned |
| `HeadDummy` | Head dummy used to offset the raycast |
| `MaxConvergenceDistance` | Maximum distance to check for convergence |
| `MinConvergenceDistance` | Minimum distance to check for convergence |

## A real one

`Vanilla\Assets\System\Grid\Grid_WeaponConvergeGridDefinition.def`

```json
{
  "Guid": "08523c95-dffa-443e-8789-6e33de8204a9",
  "HeadDummy": "2f0f6710-3dc2-4ecb-bcc6-0719ad23bd07"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WeaponConvergeGridDefinitionObjectBuilder')
search_content('', type_contains='WeaponConvergeGridDefinitionObjectBuilder')
```
