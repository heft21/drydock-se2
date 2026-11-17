# InteractedEntityProviderServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.InteractedEntityProviderServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InteractionEpsilon` | Adds small length to the initial raycast length when validating. |

## A real one

`Vanilla\Assets\Characters\System\Character_InteractedEntityProviderServerDefinition.def`

```json
{
  "Guid": "d0b87426-7ae1-444f-8076-ee749b7ae6b8",
  "InteractionEpsilon": 0.05
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InteractedEntityProviderServerDefinitionObjectBuilder')
search_content('', type_contains='InteractedEntityProviderServerDefinitionObjectBuilder')
```
