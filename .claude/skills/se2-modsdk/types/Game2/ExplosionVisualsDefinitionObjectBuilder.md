# ExplosionVisualsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Explosions.ExplosionVisualsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Explosions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ExplosionVisualTimeout` | How long the explosion effect will stay on the screen. |

## A real one

`Vanilla\Assets\System\Explosions\ExplosionVisuals.def`

```json
{
  "Guid": "01b1e1b9-cb92-4277-bf66-820d08da3387",
  "ExplosionVisualTimeout": 40000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ExplosionVisualsDefinitionObjectBuilder')
search_content('', type_contains='ExplosionVisualsDefinitionObjectBuilder')
```
