# DrillBlockToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Tools.DrillBlockToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Tools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\BlockTools\Drill\DrillBlockTool_Client_DrillBlockToolControllableDefinition.def`

```json
{
  "Guid": "e14a31f5-934c-4b14-b816-47dcdf0ddee7",
  "ConsumedInputKinds": [
    "Tools"
  ],
  "PassedInputKinds": [
    "Movement",
    "Rotation",
    "Utility",
    "Toolbar"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillBlockToolControllableDefinitionObjectBuilder')
search_content('', type_contains='DrillBlockToolControllableDefinitionObjectBuilder')
```
