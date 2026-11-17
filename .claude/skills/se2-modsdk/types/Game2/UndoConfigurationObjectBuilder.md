# UndoConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.UndoRedo.UndoConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.UndoRedo`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HistorySize` | Indicates how many undoable actions are remembered |
| `MessageDuration` | How long the notifications should be visible |
| `MessageOperationInProgress` | Message for when another operation is in progress and blocks any further operations |
| `MessageOperationNoOperationAvailable` | Message for when there is no operation in history |
| `MessageOperationTimedOut` | Message for when operation takes too long and is cancelled |
| `MessageRedoOperationFailed` | Message for Redo operation failure that can be recovered |
| `MessageRedoOperationFailedCritically` | Message for Redo critical operation failure that cannot be recovered |
| `MessageRedoSuccess` | Message for redo operation succeeded |
| `MessageUndoOperationFailed` | Message for Undo operation failure that can be recovered |
| `MessageUndoOperationFailedCritically` | Message for Undo critical operation failure that cannot be recovered. |
| `MessageUndoRedoSystemTitle` | Message title for undo/redo operations |
| `MessageUndoSuccess` | Message for undo operation succeeded |
| `OperationTimeout` | Maximum time the operation is allowed to run before it times out |

## A real one

`Vanilla\Assets\System\Configurations\UndoConfiguration.def`

```json
{
  "Guid": "1d42ab2a-c83f-45e3-8e3d-9720d2cc2187",
  "HistorySize": 20,
  "MessageUndoRedoSystemTitle": "UndoMessageTitle",
  "MessageUndoSuccess": "UndoMessageUndoSuccess",
  "MessageRedoSuccess": "UndoMessageRedoSuccess",
  "MessageUndoOperationFailed": "UndoMessageUndoOperationFailedSoft",
  "MessageRedoOperationFailed": "UndoMessageRedoOperationFailedSoft",
  "MessageUndoOperationFailedCritically": "UndoMessageUndoOperationFailedCritically",
  "MessageRedoOperationFailedCritically": "UndoMessageRedoOperationFailedCritically",
  "MessageOperationTimedOut": "UndoMessageOperationTimedOut",
  "MessageOperationNoOperationAvailable": "UndoMessageNoOperationInHistory",
  "MessageOperationInProgress": "UndoMessageOperationInProgress",
  "MessageDuration": 30000000,
  "OperationTimeout": 300000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UndoConfigurationObjectBuilder')
search_content('', type_contains='UndoConfigurationObjectBuilder')
```
