# ToolToolbarHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Toolbar.ToolToolbarHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Toolbar`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MustReplaceTools` | When true, the overrides in must be present, otherwise the tool request will be denied. When false, the overrides will still be used if present, but not required. |
| `ToolOverrides` | Replaces tool equip requests with other variants, like converting the character paint tool to spectator paint tool |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\CharacterPrefabInputAdapter_ToolToolbarHandlerDefinition.def`

```json
{
  "Guid": "9c5f8152-7353-4fb7-9ab0-9797e5c3acd9",
  "ToolOverrides": {},
  "MustReplaceTools": false
}
```

Others: `SpectatorPrefabInputAdapter_ToolToolbarHandlerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolToolbarHandlerDefinitionObjectBuilder')
search_content('', type_contains='ToolToolbarHandlerDefinitionObjectBuilder')
```
