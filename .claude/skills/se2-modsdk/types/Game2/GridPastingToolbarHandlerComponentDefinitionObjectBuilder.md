# GridPastingToolbarHandlerComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Game.ToolbarHandlers.GridPastingToolbarHandlerComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.ToolbarHandlers`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\GridPasting\CharacterPrefabInputAdapter_GridPastingToolbarHandlerComponentDefinition.def`

```json
{
  "Guid": "0bf99a56-de52-4d82-8e1f-bc91a819d98d",
  "HandlerPrefab": "e5bfd05f-9651-4905-8d52-3289736f4fa2",
  "DeactivationDelay": 2500000,
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
describe_type('GridPastingToolbarHandlerComponentDefinitionObjectBuilder')
search_content('', type_contains='GridPastingToolbarHandlerComponentDefinitionObjectBuilder')
```
