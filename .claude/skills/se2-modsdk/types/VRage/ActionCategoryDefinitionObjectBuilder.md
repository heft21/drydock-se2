# ActionCategoryDefinitionObjectBuilder

`VRage:Keen.VRage.Input.Definitions.ActionCategoryDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Input.Definitions`
- definitions using it: **13**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DisplayName` | Name of the category when shown in the game's UI. |

## A real one

`Engine\Assets\Configurations\Input\HiddenActionCategory.def`

```json
{
  "Guid": "5e15cdd3-26f1-49ef-b608-9cd9db938903",
  "DisplayName": "Hidden"
}
```

Others: `GridActionCategory`, `DebugActionCategory`

---

Read it with the MCP server rather than by hand:

```
describe_type('ActionCategoryDefinitionObjectBuilder')
search_content('', type_contains='ActionCategoryDefinitionObjectBuilder')
```
