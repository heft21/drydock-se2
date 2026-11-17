# InputCompositionDialogDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Dialogs.InputCompositionDialog.InputCompositionDialogDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Dialogs.InputCompositionDialog`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ContentComposing` | Text shown while the user is actively pressing keys. |
| `ContentIdle` | Text shown while waiting for the user to press a key. |
| `Description` | Text shown for the description |

## A real one

`Vanilla\Assets\MainMenuData\UI\Dialogs\InputCompositionDialogDefinition.def`

```json
{
  "Guid": "9a8ec455-0ae7-49e4-9531-969d44a264eb",
  "Title": "InputCompositionTitle",
  "Content": "InputCompositionContent",
  "ContentComposing": "InputCompositionComposing",
  "ContentIdle": "InputCompositionIdle",
  "Description": "InputCompositionDescription"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InputCompositionDialogDefinitionObjectBuilder')
search_content('', type_contains='InputCompositionDialogDefinitionObjectBuilder')
```
