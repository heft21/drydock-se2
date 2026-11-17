# DecalBudgetDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Decals.DecalBudgetDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Decals`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Decals\Budgets\FadeOutDecalBudgetDefinition.def`

```json
{
  "Guid": "b9fe0379-6f1d-47c5-b26b-4a12b7afd056",
  "MaxDecalsInTheBudget": 100
}
```

Others: `UntrackedDecalBudgetDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalBudgetDefinitionObjectBuilder')
search_content('', type_contains='DecalBudgetDefinitionObjectBuilder')
```
