# OneOptionDialogDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Dialogs.OneOptionDialog.OneOptionDialogDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Dialogs.OneOptionDialog`
- definitions using it: **41**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConfirmOption` | Confirm Button |

## A real one

`Vanilla\Assets\MainMenuData\UI\Dialogs\RatingDialog.def`

```json
{
  "Guid": "77b4aa17-0a57-4d29-9a4a-bc68c2befc3f",
  "Title": "RatingDialogHeader",
  "Content": "RatingDialogContent",
  "ConfirmOption": "GenericClose"
}
```

Others: `LoadingFailed`, `MissingSaveDialog`

---

Read it with the MCP server rather than by hand:

```
describe_type('OneOptionDialogDefinitionObjectBuilder')
search_content('', type_contains='OneOptionDialogDefinitionObjectBuilder')
```
