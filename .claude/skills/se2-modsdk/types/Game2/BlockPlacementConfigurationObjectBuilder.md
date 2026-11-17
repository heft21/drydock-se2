# BlockPlacementConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.BlockPlacement.BlockPlacementConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.BlockPlacement`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MultipleBlocksEffectBlocksCountThreshold` | Number of blocks at which we spawn a single particle effect instead of spawning a particle effect per block |
| `MultipleBlocksEffectEnabled` | Controls if the multi block placement effect is enabled |

## A real one

`Vanilla\Assets\System\Configurations\BlockPlacementConfiguration.def`

```json
{
  "Guid": "b1c6e8b9-12e6-4bee-8e7f-e59e04d5e27b",
  "MultipleBlocksEffectEnabled": true,
  "MultipleBlocksEffectBlocksCountThreshold": 10
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockPlacementConfigurationObjectBuilder')
search_content('', type_contains='BlockPlacementConfigurationObjectBuilder')
```
