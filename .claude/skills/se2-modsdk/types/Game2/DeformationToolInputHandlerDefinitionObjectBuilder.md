# DeformationToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.DeformationToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\DeformationToolInputAdapter\DeformationToolInputAdapter.def`

```json
{
  "Guid": "c1acddb8-1473-47de-a45e-bf72dfb3b2a4",
  "InputContextDefinition": "c9a80415-b6aa-4b05-8daf-8403c2a26ac0",
  "ToolPrimary": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "ToolSecondary": "f1789abd-986b-464a-9c2a-7ebd13c53c25",
  "ToolTertiary": "ba689cc1-83f3-4473-aef6-882607dd3467"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DeformationToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='DeformationToolInputHandlerDefinitionObjectBuilder')
```
