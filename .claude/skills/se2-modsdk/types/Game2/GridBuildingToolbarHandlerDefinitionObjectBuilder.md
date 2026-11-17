# GridBuildingToolbarHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Game.ToolbarHandlers.GridBuildingToolbarHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.ToolbarHandlers`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\ToolbarHandlers\GridBuildingToolbarHandler.def`

```json
{
  "Guid": "6dae2e0c-a82c-4aa7-9c8b-2ffee227dea0",
  "HandlerPrefab": "14d02646-2e29-4078-ba54-43d00a5cc173",
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
describe_type('GridBuildingToolbarHandlerDefinitionObjectBuilder')
search_content('', type_contains='GridBuildingToolbarHandlerDefinitionObjectBuilder')
```
