# DatapadConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Datapads.DatapadConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Datapads`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `NonDiscoverables` | Datapads excluded from discovery counts (e.g., base definitions, test data). |

## A real one

`Vanilla\Assets\Items\Datapads\System\DatapadConfiguration.def`

```json
{
  "Guid": "17c2b45d-d36c-4943-9e31-24825755876d",
  "NonDiscoverables": [
    "879dee46-3e17-449a-a7fb-3eeb0864077a",
    "a205b61c-caa8-4df6-8824-f4ccd56cd758"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DatapadConfigurationObjectBuilder')
search_content('', type_contains='DatapadConfigurationObjectBuilder')
```
