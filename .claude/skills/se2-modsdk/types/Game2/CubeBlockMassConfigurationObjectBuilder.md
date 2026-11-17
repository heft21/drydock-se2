# CubeBlockMassConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.CubeBlockMassConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MinBlockMass` | The minimum mass for the block, which serves as the baseline for the mass calculation. This value is used in the mass computation formula and ensures that the block has a minimum weight, even if the calculated mass based on grid cells and density is lower than this value. |

## A real one

`Vanilla\Assets\System\Configurations\CubeBlockMassConfiguration.def`

```json
{
  "Guid": "a924daac-f893-4fea-922d-cd7abf7d0f04",
  "MinBlockMass": 5
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeBlockMassConfigurationObjectBuilder')
search_content('', type_contains='CubeBlockMassConfigurationObjectBuilder')
```
