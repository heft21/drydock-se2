# ColonizationConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Colonization.ColonizationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Colonization`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SectorPrefab` | Default colonization sector prefab definition. |

## A real one

`Vanilla\Assets\System\Colonization\ColonizationConfiguration.def`

```json
{
  "Guid": "1300972b-0153-4d04-8d05-0d966b5c8dc9",
  "SectorPrefab": "3366dc2e-84ed-412e-bb38-7bc49da4fa91"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ColonizationConfigurationObjectBuilder')
search_content('', type_contains='ColonizationConfigurationObjectBuilder')
```
