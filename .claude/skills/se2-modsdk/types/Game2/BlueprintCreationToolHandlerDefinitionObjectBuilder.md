# BlueprintCreationToolHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.BlueprintCreationToolHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\BlueprintCreationToolHandlerDefinition.def`

```json
{
  "Guid": "992edcf0-d2e1-44d4-b84a-a8d9717f6d26",
  "HandlerPrefab": "a786ca76-4d7d-4065-a148-4036fc72896b",
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
describe_type('BlueprintCreationToolHandlerDefinitionObjectBuilder')
search_content('', type_contains='BlueprintCreationToolHandlerDefinitionObjectBuilder')
```
