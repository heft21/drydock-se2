# HingeBlockToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Tools.HingeBlockToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Tools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\BlockTools\Hinge\HingeBlockTool_HingeBlockToolControllableDefinition.def`

```json
{
  "Guid": "ccb3bcbb-96a4-4130-8ea0-a3ef95200bc9",
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
describe_type('HingeBlockToolControllableDefinitionObjectBuilder')
search_content('', type_contains='HingeBlockToolControllableDefinitionObjectBuilder')
```
