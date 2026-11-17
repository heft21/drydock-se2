# SessionInGameUIDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.InGame.SessionInGameUIDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.InGame`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TerminalScreenViewModelDefinition` | Terminal screen ViewModel settings |

## A real one

`Vanilla\Assets\UI\InGameUI.def`

```json
{
  "Guid": "dd1d1cf4-ec81-44d6-99d2-42a827b9f8f1",
  "TerminalScreenViewModelDefinition": "2d431a51-6077-49f2-bf64-bcedd362b9cb"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SessionInGameUIDefinitionObjectBuilder')
search_content('', type_contains='SessionInGameUIDefinitionObjectBuilder')
```
