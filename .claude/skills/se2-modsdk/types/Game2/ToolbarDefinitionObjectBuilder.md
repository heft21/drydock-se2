# ToolbarDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Toolbar.ToolbarDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Toolbar`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InputContextLayer` | Control layer for toolbar inputs |
| `SelectAdjacentTile` | Input action to navigate to next or previous block based on input (e.g. mouse wheel) |
| `SelectEmptyTile` | Input action to clear current block tile selection (e.g. 0) |
| `SelectNextTile` | Input action to select the next block tile |
| `SelectPreviousTile` | Input action to select the previous block tile |
| `SelectTile` | Input action to select specific block tile in the active toolbar (e.g. 1, 2, 3, 4...) |
| `SelectToolbar` | Input action to switch to a specific toolbar (e.g. CTRL + 1, 2, 3, 4...) |
| `SelectToolbarAdjacent` | Input action to navigate to next or previous toolbar based on input (e.g. CTRL + mouse wheel) |
| `SelectToolbarNext` | Input action to switch to next toolbar tab |
| `SelectToolbarPrevious` | Input action to switch to previous toolbar |

## A real one

`Vanilla\Assets\UI\UIToolbar.def`

Others: `CharacterToolbarDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolbarDefinitionObjectBuilder')
search_content('', type_contains='ToolbarDefinitionObjectBuilder')
```
