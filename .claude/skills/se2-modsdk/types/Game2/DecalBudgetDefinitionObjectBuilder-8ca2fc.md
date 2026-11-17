# DecalBudgetDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.DecalBudgetDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxDecalsInTheBudget` | When the number of decals in the budget surpass older decals are faded out |

## A real one

`Vanilla\Assets\System\Decals\Budgets\ParallaxDecalsBuget.def`

```json
{
  "Guid": "c8d28275-560a-4a2c-a606-6a9cde600ecd",
  "MaxDecalsInTheBudget": 200
}
```

Others: `ExplosionDecalBudget`, `WheelTracksDecalBudget`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalBudgetDefinitionObjectBuilder')
search_content('', type_contains='DecalBudgetDefinitionObjectBuilder')
```
