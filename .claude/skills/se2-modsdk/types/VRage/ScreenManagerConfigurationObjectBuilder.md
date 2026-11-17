# ScreenManagerConfigurationObjectBuilder

`VRage:Keen.VRage.UI.Screens.ScreenManagerConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.UI.Screens`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PinningTimeout` | Sets the timeout for texture pinning operations. If a pinning operation takes longer than this time span, it will assert and open screen anyway. |

## A real one

`Engine\Assets\Data\ScreenManagerConfiguration.def`

```json
{
  "Guid": "f4b13415-1f17-4c21-9588-7203699fd3e5",
  "PinningTimeout": 80000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ScreenManagerConfigurationObjectBuilder')
search_content('', type_contains='ScreenManagerConfigurationObjectBuilder')
```
