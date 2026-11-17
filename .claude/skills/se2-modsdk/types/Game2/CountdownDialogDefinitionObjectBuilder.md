# CountdownDialogDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Dialogs.CountdownDialog.CountdownDialogDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Dialogs.CountdownDialog`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConfirmByDefault` | If , the automatically chosen resolution will be the , else . |
| `Seconds` | Time to the auto-resolution of the dialog |

## A real one

`Vanilla\Assets\MainMenuData\UI\Dialogs\DisplaySettingsChangedDialog.def`

```json
{
  "Guid": "7e307026-1196-4aed-b101-a6423a05e2be",
  "Title": "DialogsDisplaySettingsChanged",
  "Content": "DialogsDisplaySettingsChangedContent",
  "ConfirmOption": "GenericDialogYes",
  "CancelOption": "GenericDialogNo",
  "SelectedOption": "Confirm",
  "Seconds": 15,
  "ConfirmByDefault": false
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CountdownDialogDefinitionObjectBuilder')
search_content('', type_contains='CountdownDialogDefinitionObjectBuilder')
```
