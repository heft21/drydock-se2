# ProjectionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Render.ProjectionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Render`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Changes` | Pairs of material state swaps that should be applied to the previewed object |
| `DefaultHologramState` | Default hologram state |

## A real one

`Vanilla\Assets\System\Previews\PreviewerProjection.def`

Too large to inline. Fields present:

`Changes`, `DefaultHologramState`, `Guid`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectionDefinitionObjectBuilder')
search_content('', type_contains='ProjectionDefinitionObjectBuilder')
```
