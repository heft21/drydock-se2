# RadialMenuAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Controls.RadialMenu.RadialMenuAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Controls.RadialMenu`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PaintToolSkinHoverIcon` | Hover icon for Skins on Paint Tool |
| `PaintToolSkinIcon` | Icon for Skins on Paint Tool |
| `QuickMenuReturnHoverIcon` | Hover icon for returning up one level in the quick menu |
| `QuickMenuReturnIcon` | Icon for returning up one level in the quick menu |

## A real one

`Vanilla\Assets\UI\RadialMenuAvaloniaConfiguration.def`

```json
{
  "Guid": "ce358a76-de9e-4117-b2a4-5a28569412ee",
  "QuickMenuReturnIcon": "{G}5e42b1b2-6319-403d-9099-ff76a76a1616",
  "QuickMenuReturnHoverIcon": "{G}5e42b1b2-6319-403d-9099-ff76a76a1616",
  "PaintToolSkinIcon": "{G}f07eda89-27f7-4d23-8073-00b72b3e7397",
  "PaintToolSkinHoverIcon": "{G}f07eda89-27f7-4d23-8073-00b72b3e7397"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RadialMenuAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='RadialMenuAvaloniaConfigurationObjectBuilder')
```
