# RadialSliceAudioConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Controls.RadialMenu.RadialSliceAudioConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Controls.RadialMenu`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OnClickAudio` | Audio event to play when clicking the slice One-shot sound |
| `OnHoverAudio` | Audio event to play when hovering the slice One-shot sound |

## A real one

`Vanilla\Assets\System\Configurations\RadialSliceAudioConfiguration.def`

```json
{
  "Guid": "bb29eeb2-d586-44a5-96f8-afba8d694d65",
  "OnClickAudio": "event:/UI/ColorTool_menu_click",
  "OnHoverAudio": "event:/UI/ColorTool_menu_over"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RadialSliceAudioConfigurationObjectBuilder')
search_content('', type_contains='RadialSliceAudioConfigurationObjectBuilder')
```
