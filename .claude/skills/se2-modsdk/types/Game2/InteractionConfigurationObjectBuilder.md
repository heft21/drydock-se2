# InteractionConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Interaction.InteractionConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxInteractionDistance` | Max allowed distance between interacted entities |

## A real one

`Vanilla\Assets\System\Configurations\InteractionConfiguration.def`

```json
{
  "Guid": "717fa882-5757-46a5-b579-983e700020f9",
  "MaxInteractionDistance": 5,
  "SubpartAllowedDummies": [
    "4511a2ef-912d-4980-adf2-47b1e8898190"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InteractionConfigurationObjectBuilder')
search_content('', type_contains='InteractionConfigurationObjectBuilder')
```
