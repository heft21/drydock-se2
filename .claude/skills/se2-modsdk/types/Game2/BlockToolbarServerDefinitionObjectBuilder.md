# BlockToolbarServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Toolbar.BlockToolbarServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Toolbar`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AllowDuplicateTiles` | When true, tiles with the same action + reference are allowed on the toolbar. |
| `Name` | Name of the toolbar, shown in terminal when there are multiple on a single entity. |
| `TilesCount` | Number of toolbar tiles/slots within each group |
| `ToolbarsCount` | Number of toolbar groups |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\TimerBlockToolbarServerDefinition.def`

```json
{
  "Guid": "e7eb40b5-7f1c-443b-9d3b-f77846dbdc4a",
  "ToolbarsCount": 9,
  "TilesCount": 10
}
```

Others: `Button25_Client_BlockToolbarServerDefinition`, `SoundBlock_BlockToolbarServerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockToolbarServerDefinitionObjectBuilder')
search_content('', type_contains='BlockToolbarServerDefinitionObjectBuilder')
```
