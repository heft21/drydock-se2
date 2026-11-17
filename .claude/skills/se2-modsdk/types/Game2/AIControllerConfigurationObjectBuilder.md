# AIControllerConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.Definitions.AIControllerConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ControllerPrefab` | Prefab of the AI controller entity. |

## A real one

`Vanilla\Assets\System\AI\AIControllerConfiguration.def`

```json
{
  "Guid": "9f9ec302-396c-4d3f-9def-64a55709478a",
  "ControllerPrefab": "7986c7bc-7c06-438c-8db5-fd8b990ab7d9",
  "NPCCharacterPrefab": "f3f9fff0-e60e-4f76-b4ac-03e8759493ec",
  "PerceptionProfile": "eef3712d-27f4-4422-8fdd-fda61122c53e",
  "BlackboardStats": [
    {
      "Key": "c0995563-70b5-4637-ae33-d725cd7849e6",
      "Value": {
        "Stat": "3a40976e-7f57-46ea-a1a3-4d8124722e04",
        "Key": "stat_health",
        "Value": "Ratio"
      }
    }
  ],
  "AnimationBlackboardValues": [
    {
      "Key": "75e28acd-1644-43d4-8046-d055510052cc",
      "Value": {
        "Key": "alertness_level",
        "AnimationKey": "Alertness"
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AIControllerConfigurationObjectBuilder')
search_content('', type_contains='AIControllerConfigurationObjectBuilder')
```
