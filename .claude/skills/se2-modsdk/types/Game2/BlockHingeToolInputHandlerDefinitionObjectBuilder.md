# BlockHingeToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.BlockTools.BlockHingeToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.BlockTools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\BlockHingeToolInputAdapter\BlockHingeToolInputHandlerDefinition.def`

```json
{
  "Guid": "40527fae-7f88-4283-aa8d-e48187ee469a",
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
describe_type('BlockHingeToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='BlockHingeToolInputHandlerDefinitionObjectBuilder')
```
