# MechanicalBlockConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.MechanicalBlockConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PivotDummies` | List of dummy types that can be used as a pivot (point where the physical connection will originate from) of mechanical blocks. |

## A real one

`Vanilla\Assets\System\Configurations\MechanicalBlockConfig.def`

```json
{
  "Guid": "4c4d0fac-37f3-446c-b33d-46a2add0fe96",
  "PivotDummies": [
    "b80cb7d1-126f-406e-a1c7-6410109f3c1d"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalBlockConfigurationObjectBuilder')
search_content('', type_contains='MechanicalBlockConfigurationObjectBuilder')
```
