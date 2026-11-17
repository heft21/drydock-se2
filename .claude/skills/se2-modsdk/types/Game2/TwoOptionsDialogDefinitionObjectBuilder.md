# TwoOptionsDialogDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Dialogs.TwoOptionsDialog.TwoOptionsDialogDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Dialogs.TwoOptionsDialog`
- definitions using it: **40**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CancelOption` | Cancel Button |
| `IsMultiline` | When true, renders the input as a large multiline text area instead of a single-line field. |
| `SelectedOption` | Pre-Selected option on |

## A real one

`Vanilla\Assets\System\Mission\MissionFailedDialog.def`

```json
{
  "Guid": "78c79317-b8cc-4b57-af4c-a0daeda82179",
  "Title": "MissionFailedTitle",
  "Content": "MissionFailedContent",
  "ConfirmOption": "MissionFailedReloadSave",
  "CancelOption": "MissionFailedExitToMenu",
  "SelectedOption": "Confirm"
}
```

Others: `LowMemoryWarning`, `UrlWarningDialog`

---

Read it with the MCP server rather than by hand:

```
describe_type('TwoOptionsDialogDefinitionObjectBuilder')
search_content('', type_contains='TwoOptionsDialogDefinitionObjectBuilder')
```
