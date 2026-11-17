# ConsumablesToolHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.ConsumablesToolHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\ConsumablesToolHandlerDefinition.def`

```json
{
  "Guid": "2d1ee17c-315b-4a28-abf8-b13e688c9ab1",
  "HandlerPrefab": "a2891a96-fdb2-457d-93d2-880596c0df14",
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
describe_type('ConsumablesToolHandlerDefinitionObjectBuilder')
search_content('', type_contains='ConsumablesToolHandlerDefinitionObjectBuilder')
```
