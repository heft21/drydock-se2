# IntegrityBlockToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Tools.IntegrityBlockToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Tools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\BlockTools\Integrity\IntegrityBlockTool_Client_IntegrityBlockToolControllableDefinition.def`

```json
{
  "Guid": "c1b99b20-93bf-42ba-ab1a-5fe67ae80dfa",
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
describe_type('IntegrityBlockToolControllableDefinitionObjectBuilder')
search_content('', type_contains='IntegrityBlockToolControllableDefinitionObjectBuilder')
```
