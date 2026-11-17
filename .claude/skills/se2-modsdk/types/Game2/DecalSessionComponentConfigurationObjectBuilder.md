# DecalSessionComponentConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.DecalSessionComponentConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BigDecalLifetime` | How big decals should fade out on grids |
| `DecalFadeOutTime` | How much time it takes for the decal to fade out |
| `DefaultDecalLifetime` | If not specified otherwise, all decals will disappear after this period. |
| `FadeOutBudget` | Budget for decals that are faded out before destruction |
| `FloatingObjectsDecalZOffset` | Offset from the hit point to the decal center in Z-direction 0 - decal Z == 0 is at the hit point 1 - decal Z == 1 is at the hit point |
| `MaxLinearSizeForBigDecals` | After what size the decal is considered big |
| `ParallaxDecalBudget` | Budget for decals that are using parallax material |
| `UntrackedBudget` | A special kind of budget that is not being tracked by budgeting system. Used for special cases where we don't want the decal to be removed by budgets |
| `VoxelsFilter` | Entity filter for voxel entities. Used to correctly apply decals on voxels |

## A real one

`Vanilla\Assets\System\Decals\DecalSessionComponentConfiguration.def`

```json
{
  "Guid": "19ca5d59-d944-4899-9a31-4eb0b4256c64",
  "UntrackedBudget": "a1320f3e-6849-4382-8a7b-46e4f40682bd",
  "FadeOutBudget": "b9fe0379-6f1d-47c5-b26b-4a12b7afd056",
  "ParallaxDecalBudget": "c8d28275-560a-4a2c-a606-6a9cde600ecd",
  "DecalFadeOutTime": 50000000,
  "MaxLinearSizeForBigDecals": 1.5,
  "BigDecalLifetime": {
    "LifeTime": 600000000,
    "FadeOutTime": null
  },
  "DefaultDecalLifetime": {
    "LifeTime": 1800000000,
    "FadeOutTime": null
  },
  "VoxelsFilter": "58e106fe-ab5e-4e66-a9b8-10fd46ba786d",
  "FloatingObjectsDecalZOffset": 0.15
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalSessionComponentConfigurationObjectBuilder')
search_content('', type_contains='DecalSessionComponentConfigurationObjectBuilder')
```
