# UndoInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.UndoInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InputContextDefinitionUndo` | Definition for input context for all Undo/Redo input actions |
| `Redo` | Binding to activate Redo |
| `Undo` | Binding to activate Undo |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\UndoRedoInputHandlers\UndoInputHandlerDefinition.def`

```json
{
  "Guid": "3312fc9d-ed0e-4894-b323-b3df8e490ea5",
  "InputContextDefinitionUndo": "20636022-d49a-4ed2-adf5-db06fed95f01",
  "Undo": "13c633e2-952c-4cbf-8ed9-eb78a1920c1b",
  "Redo": "73c0d807-13f9-403a-b5f2-3a1ca74a6c94"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UndoInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='UndoInputHandlerDefinitionObjectBuilder')
```
