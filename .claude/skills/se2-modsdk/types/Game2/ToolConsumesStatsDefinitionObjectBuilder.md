# ToolConsumesStatsDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.ToolConsumesStatsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `StatsToConsume` | Stats to consume when tool runs |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\ToolConsumesStatsDefinition.def`

```json
{
  "Guid": "8100772b-deef-46e6-8b47-f0af99da36cb",
  "StatsToConsume": [
    {
      "Key": "680dd026-dcfa-4a90-95e4-389d0779ccf2",
      "Value": {
        "Stat": "675206d7-7a7a-445c-946c-e0a74bbcd862",
        "Amount": 0
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolConsumesStatsDefinitionObjectBuilder')
search_content('', type_contains='ToolConsumesStatsDefinitionObjectBuilder')
```
