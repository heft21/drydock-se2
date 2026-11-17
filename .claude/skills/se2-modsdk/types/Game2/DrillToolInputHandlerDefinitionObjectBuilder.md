# DrillToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.DrillToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ToolPrimaryHint` | Hint shown for action |
| `ToolSecondaryHint` | Hint shown for action |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\DrillToolInputAdapter\DrillToolInputAdapter.def`

```json
{
  "Guid": "cbac0006-a605-44b4-86e6-2f414ec4ad5f",
  "InputContextDefinition": "c9a80415-b6aa-4b05-8daf-8403c2a26ac0",
  "ToolPrimary": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "ToolSecondary": "f1789abd-986b-464a-9c2a-7ebd13c53c25",
  "ToolTertiary": null,
  "ToolPrimaryHint": "DrillToolPrimaryHint",
  "ToolSecondaryHint": "DrillToolSecondaryHint"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='DrillToolInputHandlerDefinitionObjectBuilder')
```
