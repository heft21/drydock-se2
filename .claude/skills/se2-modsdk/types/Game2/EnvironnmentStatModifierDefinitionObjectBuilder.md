# EnvironnmentStatModifierDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.EnvironnmentStatModifierDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AirModifiers` | Collection of modifiers to apply to stats based on environmental factors. |

## A real one

`Vanilla\Assets\Characters\System\EnvironnmentStatModifierDefinition.def`

```json
{
  "Guid": "173b91fc-6159-472e-8dfc-6516808e5a55",
  "AirModifiers": [
    {
      "Key": "9d4c9ca6-2a1e-4722-b9ec-7ff1b0da8875",
      "Value": {
        "Resource": "d129d38e-116d-4424-a1a8-bbb298ac9dba",
        "Stat": "c162f32f-75ab-4d17-8a49-696dc6caf1ff",
        "Delta": 1
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EnvironnmentStatModifierDefinitionObjectBuilder')
search_content('', type_contains='EnvironnmentStatModifierDefinitionObjectBuilder')
```
