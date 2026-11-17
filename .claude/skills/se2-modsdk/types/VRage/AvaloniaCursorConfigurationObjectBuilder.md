# AvaloniaCursorConfigurationObjectBuilder

`VRage:Keen.VRage.UI.Definitions.AvaloniaCursorConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.UI.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FallbackCursor` | Cursor used as a fallback for any Standard cursors not defined in . If not provided then the corresponding system cursor will be used as fallback instead. |
| `StandardCursorOverrides` | Maps standard cursor types to pre-defined custom cursors used to override them. |

## A real one

`Engine\Assets\Core\UI\AvaloniaCursorConfiguration.def`

```json
{
  "Guid": "db8d2bbc-8c23-49fa-9342-0aec92a72b60",
  "StandardCursorOverrides": {},
  "FallbackCursor": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AvaloniaCursorConfigurationObjectBuilder')
search_content('', type_contains='AvaloniaCursorConfigurationObjectBuilder')
```
