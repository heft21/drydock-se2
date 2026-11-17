# IntegrityToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.IntegrityToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ChangeMode` | Input action for scrolling through |
| `ModeHints` | Map of an integrity mode to it's control hint. |
| `ToolPrimaryHint` | Hint shown for |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\IntegrityToolInputAdapter\WelderToolInputAdapter.def`

```json
{
  "Guid": "78e24f38-096b-4ce6-9da0-b4e2e57d4935",
  "InputContextDefinition": "3f355857-1157-4124-a89f-e7ee79d33bc3",
  "ToolPrimary": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "ToolSecondary": null,
  "ToolTertiary": null,
  "ChangeMode": "94fd4f16-ce85-47e4-a4a5-09fa4bad602f",
  "ModeHints": {
    "Component": "IntegrityToolComponentHint",
    "Raw": "IntegrityToolRawHint"
  },
  "ToolPrimaryHint": "WelderToolPrimary"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('IntegrityToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='IntegrityToolInputHandlerDefinitionObjectBuilder')
```
