# GridExplosionEffectComponentConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeGrids.GridExplosionEffectComponentConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeGrids`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AABBScaleExtent` | Controls which extent of grid AABB is used to be multiplied by . At 0 - minimal grid extent is used At 1 - maximal grid extent is used Values in between will be interpolated |
| `ExplosionEffect` | Effect to be played when grid is manually exploded; |
| `ScaleMultiplier` | Scale of the effect. Depends on th |

## A real one

`Vanilla\Assets\System\Configurations\GridExplosionEffectComponentConfiguration.def`

```json
{
  "Guid": "0b47e552-5991-4242-945d-a1a7aab8a123",
  "ExplosionEffect": "689a9963-ef10-4e80-af1b-6abd87bf8960",
  "ScaleMultiplier": 0.25,
  "AABBScaleExtent": 0.5
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridExplosionEffectComponentConfigurationObjectBuilder')
search_content('', type_contains='GridExplosionEffectComponentConfigurationObjectBuilder')
```
