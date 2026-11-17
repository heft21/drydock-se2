# GridProjectionsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.BlockPlacement.Projections.GridProjectionsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.BlockPlacement.Projections`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ResetGeneratedWhenMaterializing` | When true, the state will be reset when a block is materialized. This will make it so generated supports become permanent parts of the grids (included in copy/paste) after welding. |

## A real one

`Vanilla\Assets\System\Configurations\GridProjectionsConfiguration.def`

```json
{
  "Guid": "af47729a-bd30-4974-a76d-fc4ae5fabeec",
  "ResetGeneratedWhenMaterializing": false
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridProjectionsConfigurationObjectBuilder')
search_content('', type_contains='GridProjectionsConfigurationObjectBuilder')
```
