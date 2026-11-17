# VoxelToolbarHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Game.ToolbarHandlers.VoxelToolbarHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.ToolbarHandlers`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\ToolbarHandlers\VoxelToolbarHandler.def`

```json
{
  "Guid": "162e7bf3-c35c-460a-980e-00a65fbd6921",
  "HandlerPrefab": "202f0c00-6496-48cf-883f-d5c43ff9b3d5",
  "DeactivationDelay": 0,
  "ToolTransform": {
    "Transform": {
      "Position": {
        "X": 0,
        "Y": 0,
        "Z": 0
      },
      "Orientation": {
        "X": 0,
        "Y": 0,
        "Z": 0,
        "W": 1
      }
    },
    "EulerHint": {
      "X": 0,
      "Y": 0,
      "Z": 0
    }
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelToolbarHandlerDefinitionObjectBuilder')
search_content('', type_contains='VoxelToolbarHandlerDefinitionObjectBuilder')
```
