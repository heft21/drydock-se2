# ActionCategoryConfigurationObjectBuilder

`VRage:Keen.VRage.Input.Definitions.ActionCategoryConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Input.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HiddenActionCategory` | Category used by actions that should not appear in the UI. |
| `OrderedControlCategories` | Control Categories in the order they should be displayed in the UI. |

## A real one

`Engine\Assets\Core\ActionCategoryConfiguration.def`

```json
{
  "Guid": "e91fd7f6-ee70-430e-bccc-f063eb6cd606",
  "HiddenActionCategory": "5e15cdd3-26f1-49ef-b608-9cd9db938903",
  "OrderedControlCategories": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ActionCategoryConfigurationObjectBuilder')
search_content('', type_contains='ActionCategoryConfigurationObjectBuilder')
```
