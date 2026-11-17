# GridPrefabProviderSessionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.GridPrefabs.GridPrefabProviderSessionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.GridPrefabs`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GridPrefab` | Default grid prefab (e.g. used as base for ) |

## A real one

`Vanilla\Assets\System\Session\GridPrefabProviderSessionDefinition.def`

```json
{
  "Guid": "60565856-1ca1-41fb-b231-32fdd7f4d757",
  "GridPrefab": "672d6382-207a-498f-a51c-58b370aa96cb"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridPrefabProviderSessionDefinitionObjectBuilder')
search_content('', type_contains='GridPrefabProviderSessionDefinitionObjectBuilder')
```
