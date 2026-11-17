# WaterToolbarHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Game.ToolbarHandlers.WaterToolbarHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.ToolbarHandlers`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\ToolbarHandlers\WaterToolbarHandler.def`

```json
{
  "Guid": "1f1d836b-be5c-48cd-90e2-dd93bb16894b",
  "HandlerPrefab": "842902b5-a899-4b98-abee-1f27405d65ab",
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
describe_type('WaterToolbarHandlerDefinitionObjectBuilder')
search_content('', type_contains='WaterToolbarHandlerDefinitionObjectBuilder')
```
