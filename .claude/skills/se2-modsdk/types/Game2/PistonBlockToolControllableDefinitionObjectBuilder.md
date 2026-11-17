# PistonBlockToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Tools.PistonBlockToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Tools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\BlockTools\Piston\PistonBlockTool_PistonBlockToolControllableDefinition.def`

```json
{
  "Guid": "1cbbbaa3-7a1e-4f12-8f09-6913dcecffef",
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
describe_type('PistonBlockToolControllableDefinitionObjectBuilder')
search_content('', type_contains='PistonBlockToolControllableDefinitionObjectBuilder')
```
