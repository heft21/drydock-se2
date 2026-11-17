# ScreenshotToolHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.ScreenshotToolHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\ScreenshotToolHandlerDefinition.def`

```json
{
  "Guid": "24311cef-0db9-4af6-95fb-ad1e8ef2c90d",
  "HandlerPrefab": "4b188cbe-3e12-4f89-9144-8f41c263d89a",
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
describe_type('ScreenshotToolHandlerDefinitionObjectBuilder')
search_content('', type_contains='ScreenshotToolHandlerDefinitionObjectBuilder')
```
