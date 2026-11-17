# BreakableBlocksConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.BreakableBlocksConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CriticalFractureHealthShareMultiplier` | Multiplier applied to the share of a block's total HP allocated to critical fractures |

## A real one

`Vanilla\Assets\System\Configurations\BreakableBlocksConfiguration.def`

```json
{
  "Guid": "73cc0e26-76ab-4efd-ac55-428ab95ba740",
  "CriticalFractureHealthShareMultiplier": 2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BreakableBlocksConfigurationObjectBuilder')
search_content('', type_contains='BreakableBlocksConfigurationObjectBuilder')
```
