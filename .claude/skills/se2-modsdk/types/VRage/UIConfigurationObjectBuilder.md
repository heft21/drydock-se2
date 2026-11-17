# UIConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Data.UIConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultFontFamily` | Default family to use when a font is not found. |
| `InternalFont` | Font used internally for tests and debugging. |

## A real one

`Engine\Assets\Configurations\Setup\UIConfiguration.def`

```json
{
  "Guid": "8ac430f4-2611-4506-a6ff-9ee194e13256",
  "DefaultFontFamily": "558bf912-cbe6-49ce-9e8d-f211e5c70506",
  "InternalFont": "34c4c656-ccc7-4ad2-9fc9-324087b8423d"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UIConfigurationObjectBuilder')
search_content('', type_contains='UIConfigurationObjectBuilder')
```
