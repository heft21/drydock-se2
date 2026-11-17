# BlockIntegrityToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.BlockTools.BlockIntegrityToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.BlockTools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\BlockIntegrityToolInputAdapter\BlockIntegrityToolInputAdapter_BlockIntegrityToolInputHandlerDefinition.def`

```json
{
  "Guid": "89a54cfa-57de-4562-9994-be63714da224",
  "InputContextDefinition": "c9a80415-b6aa-4b05-8daf-8403c2a26ac0",
  "ToolPrimary": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "ToolSecondary": null,
  "ToolTertiary": null,
  "ToolPrimaryHint": "IntegrityToolPrimaryHint",
  "ToolSecondaryHint": "",
  "ToolTertiaryHint": ""
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockIntegrityToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='BlockIntegrityToolInputHandlerDefinitionObjectBuilder')
```
