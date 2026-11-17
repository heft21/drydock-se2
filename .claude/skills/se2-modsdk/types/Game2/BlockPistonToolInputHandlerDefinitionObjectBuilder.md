# BlockPistonToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.BlockTools.BlockPistonToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.BlockTools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\BlockPistonToolInputAdapter\BlockPistonToolInputHandlerDefinition.def`

```json
{
  "Guid": "dfb5537e-7dc2-4b02-a07a-166fd8b81436",
  "InputContextDefinition": "c9a80415-b6aa-4b05-8daf-8403c2a26ac0",
  "ToolPrimary": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "ToolSecondary": "f1789abd-986b-464a-9c2a-7ebd13c53c25",
  "ToolTertiary": null,
  "ToolPrimaryHint": "",
  "ToolSecondaryHint": "",
  "ToolTertiaryHint": ""
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockPistonToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='BlockPistonToolInputHandlerDefinitionObjectBuilder')
```
