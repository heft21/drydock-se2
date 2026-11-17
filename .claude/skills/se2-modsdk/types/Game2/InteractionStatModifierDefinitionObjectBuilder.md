# InteractionStatModifierDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Shared.InteractionStatModifierDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Shared`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FilledEpsilon` | Epsilon value when approaching the max or min value of a stat. When the value is within this range the value is automatically set to the max/min. |
| `Stats` | Collection of all stats that can be modified and their rates |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\InteractionStatModifierDefinition.def`

```json
{
  "Guid": "3fe120d3-d52e-4ef1-b69a-3348323e289d",
  "Stats": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InteractionStatModifierDefinitionObjectBuilder')
search_content('', type_contains='InteractionStatModifierDefinitionObjectBuilder')
```
