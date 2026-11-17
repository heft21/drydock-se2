# SpotlightStyleDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Tutorial.Spotlights.SpotlightStyleDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Tutorial.Spotlights`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Chamfer` | Diagonal corner chamfer size in UI design-space pixels; zero or less disables it |
| `Color` | Border color |
| `Thickness` | Border thickness |

## A real one

`Vanilla\Assets\UI\Tutorials\Styles\DefaultSpotlightStyle.def`

```json
{
  "Guid": "b8f9a111-b269-4d07-a949-47145c264138",
  "Color": {
    "PackedValue": 4278251775
  },
  "Thickness": 3
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SpotlightStyleDefinitionObjectBuilder')
search_content('', type_contains='SpotlightStyleDefinitionObjectBuilder')
```
