# RenderModelDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Render.RenderModelDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Render`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ModelHandle` | Model asset. |
| `Presets` | Presets available for this model. |

## A real one

`Vanilla\Assets\Characters\System\ModelMiroslavSokol.def`

```json
{
  "Guid": "877651a4-174f-42c3-98a9-a99a059efef8",
  "ModelHandle": "{G}eaf399a4-6c21-4127-9030-d574e30de47b",
  "Presets": "34349ab7-8fed-4597-bb5d-3da7e47a3577"
}
```

Others: `VeteranMale_RenderModelDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('RenderModelDefinitionObjectBuilder')
search_content('', type_contains='RenderModelDefinitionObjectBuilder')
```
