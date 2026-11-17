# ThreeOptionsDialogDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Dialogs.ThreeOptionsDialog.ThreeOptionsDialogDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Dialogs.ThreeOptionsDialog`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CancelOption` | Cancel Button |
| `DefaultOption` | Default Button |
| `SelectedOption` | Pre-Selected option on |

## A real one

`Vanilla\Assets\MainMenuData\UI\Dialogs\SaveBeforeExit.def`

```json
{
  "Guid": "46835f21-d59b-40d3-8fc7-96cf9f211776",
  "Title": "ExitToWindowsDialogTitle",
  "Content": "SaveBeforeQuitDialog",
  "ConfirmOption": "GenericDialogYes",
  "CancelOption": "GenericDialogCancel",
  "DefaultOption": "GenericDialogNo",
  "SelectedOption": "Confirm"
}
```

Others: `SaveBeforeLoad`, `SaveBeforeQuit`

---

Read it with the MCP server rather than by hand:

```
describe_type('ThreeOptionsDialogDefinitionObjectBuilder')
search_content('', type_contains='ThreeOptionsDialogDefinitionObjectBuilder')
```
