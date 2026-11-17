# TargetingGridDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Weapons.TargetingGridDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Weapons`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DetectionRange` | How far away from the grid to detect potential targets. |
| `DetectionTriggerTagTypes` | Entity tag that mark potential targets. |
| `TriggerDefinition` | Artificial delay to detection trigger updates. |

## A real one

`Vanilla\Assets\System\Grid\Grid_TargetingGridDefinition.def`

```json
{
  "Guid": "7970edaf-f250-41e6-a572-be0e82b21a25",
  "DetectionRange": 1000,
  "DetectionTriggerTagTypes": [],
  "TriggerDefinition": "bcfba9fb-ad3e-4529-a3d9-c54ff35e7dfc"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TargetingGridDefinitionObjectBuilder')
search_content('', type_contains='TargetingGridDefinitionObjectBuilder')
```
