# SaveSessionComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.RuntimeSystems.Saves.SaveSessionComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.RuntimeSystems.Saves`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AutosaveTime` | Time how often the session will autosave |

## A real one

`Vanilla\Assets\System\Session\SaveSessionComponentDefinition.def`

```json
{
  "Guid": "7688f750-e775-4433-99b2-511e57078f6c",
  "AutosaveTime": 3000000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SaveSessionComponentDefinitionObjectBuilder')
search_content('', type_contains='SaveSessionComponentDefinitionObjectBuilder')
```
