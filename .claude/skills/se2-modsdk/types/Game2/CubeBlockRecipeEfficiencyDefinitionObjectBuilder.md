# CubeBlockRecipeEfficiencyDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.CubeBlockRecipeEfficiencyDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Coefficient` | Coefficient of the amounts of all items required by the associated , must be positive. Example: For a with 10 steel plates and 6 batteries, - an efficiency of 0.2 will give a final recipe of 5 steel plates and 1 batteries, - an efficiency of 2 will give a final recipe of 20 steel plates and 12 batteries. |

## A real one

`Vanilla\Assets\Blocks\Shared\Recipes\Efficiency\EfficiencyLvl1.def`

```json
{
  "Guid": "5e4dbe0e-5e85-4b4e-a93b-e1fd21e2e892",
  "Coefficient": 2.5
}
```

Others: `EfficiencyLvl2`, `EfficiencyLvl3`

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeBlockRecipeEfficiencyDefinitionObjectBuilder')
search_content('', type_contains='CubeBlockRecipeEfficiencyDefinitionObjectBuilder')
```
