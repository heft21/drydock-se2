# FontDefinitionObjectBuilder

`VRage:Keen.VRage.Render.UI.FontDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.UI`
- definitions using it: **19**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `File` | The file containing the font. |
| `Style` | Style of the font. If a style is not found when loading fonts, the closest smaller font style will be used. |
| `Weight` | Weight of the font. If a weight is not found when loading fonts, the closest smaller font weight will be used. |

## A real one

`Engine\Assets\Data\Fonts\NotoSans\NotoSans-Bold.def`

```json
{
  "Guid": "38c5488b-15e2-47de-bc42-73871f24a978",
  "File": "{G}5ab8a193-b032-4c0d-9338-e9273f1e3af8",
  "Style": "Regular",
  "Weight": "Bold"
}
```

Others: `NotoSans-Italic`, `NotoSans-Regular`

---

Read it with the MCP server rather than by hand:

```
describe_type('FontDefinitionObjectBuilder')
search_content('', type_contains='FontDefinitionObjectBuilder')
```
