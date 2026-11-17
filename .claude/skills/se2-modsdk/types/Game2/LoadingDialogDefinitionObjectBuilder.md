# LoadingDialogDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Dialogs.LoadingDialog.LoadingDialogDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Dialogs.LoadingDialog`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AbortOption` | Abort Button |
| `AllowAbort` | Define if This loading can be cancelled |
| `KeepsOtherScreensVisible` | Keep screens bellow the dialog visible |

## A real one

`Vanilla\Assets\MainMenuData\UI\Dialogs\SavingDialog.def`

```json
{
  "Guid": "d6708db6-b22b-4ae5-b32c-4c59a3aa2afe",
  "Title": "SavingDialogTitle",
  "Content": "SavingDialogContent",
  "KeepsOtherScreensVisible": true,
  "AllowAbort": false,
  "AbortOption": "DialogBlank"
}
```

Others: `UGCDeletingDialog`, `PreparingForPlaceBlueprint`

---

Read it with the MCP server rather than by hand:

```
describe_type('LoadingDialogDefinitionObjectBuilder')
search_content('', type_contains='LoadingDialogDefinitionObjectBuilder')
```
