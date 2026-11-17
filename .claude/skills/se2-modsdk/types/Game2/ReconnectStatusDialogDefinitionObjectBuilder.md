# ReconnectStatusDialogDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Dialogs.Reconnect.ReconnectStatusDialogDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Dialogs.Reconnect`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\MainMenuData\UI\Dialogs\ReconnectStatusDialogDefinition.def`

```json
{
  "Guid": "f3a450a2-f61a-4b33-a950-7ceef5b50080",
  "Title": "ReconnectStatusDialogTitle",
  "Content": "DialogBlank",
  "AttemptingContent": "ReconnectStatusDialogAttemptingContent",
  "RetryingContent": "ReconnectStatusDialogRetryingContent",
  "ExhaustedContent": "ReconnectStatusDialogExhaustedContent",
  "RetryOption": "ReconnectStatusDialogRetryOption",
  "DeclineOption": "ReconnectStatusDialogDeclineOption"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ReconnectStatusDialogDefinitionObjectBuilder')
search_content('', type_contains='ReconnectStatusDialogDefinitionObjectBuilder')
```
