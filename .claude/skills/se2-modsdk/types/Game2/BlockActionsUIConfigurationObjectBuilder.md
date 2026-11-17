# BlockActionsUIConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Toolbar.BlockActionsUIConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Toolbar`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActionTypeLabels` | Map of action types (button, set, etc) to a specialized loc key. 'Set {Enabled}' for example |
| `ActionTypeParameterLabels` | Map of action types (button, set, etc) to a specialized loc key with the ability to display their parameters through {Parameter} 'Set {Enabled} to {Parameter}' for example |
| `DefaultActionHighlightIcon` | Highlight variant of . |
| `DefaultActionHighlightOverlay` | Highlight variant of . |
| `DefaultActionIcon` | Default icon of an action when no is defined. |
| `DefaultActionOverlay` | Default overlay of an action when no is defined. Icon that is overlayed on top of the action icon. |
| `DefaultReferenceIcon` | Icon used when no specific icon can be used (like for group references). |
| `HighlightIcons` | Map of icon ids to highlight variant GUI assets. See /> for usage. |
| `HighlightOverlays` | Map of icon ids to highlight variant GUI assets. See /> for usage. |
| `Icons` | Map of icon ids to their GUI assets. See /> for usage. Shown in edit screen |
| `InvalidActionHighlightIcon` | Highlight variant of . |
| `InvalidActionHighlightOverlay` | Highlight variant of |
| `InvalidActionIcon` | Icon shown when the action is unknown. |
| `InvalidActionOverlay` | Icon overlayed on top of the reference icon when the action is unknown. |
| `InvalidReferenceIcon` | Icon used when the block reference is unknown. |
| `Overlays` | Map of icon ids to their GUI assets. See /> for usage. Shown in toolbar |
| `ToolTipLabel` | Tooltip used when mouse is hovering over a toolbar action tile |
| `UnknownActionLabel` | Name of action used in toolbar tile when the action is unknown. |

## A real one

`Vanilla\Assets\System\Configurations\BlockActionsUIConfiguration.def`

Too large to inline. Fields present:

`ActionTypeLabels`, `ActionTypeParameterLabels`, `DefaultActionHighlightIcon`, `DefaultActionHighlightOverlay`, `DefaultActionIcon`, `DefaultActionOverlay`, `DefaultReferenceIcon`, `Guid`, `HighlightIcons`, `HighlightOverlays`, `Icons`, `InvalidActionHighlightIcon`, `InvalidActionHighlightOverlay`, `InvalidActionIcon`, `InvalidActionOverlay`, `InvalidReferenceIcon`, `Overlays`, `UnknownActionLabel`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockActionsUIConfigurationObjectBuilder')
search_content('', type_contains='BlockActionsUIConfigurationObjectBuilder')
```
