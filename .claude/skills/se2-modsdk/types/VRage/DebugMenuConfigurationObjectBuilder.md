# DebugMenuConfigurationObjectBuilder

`VRage:Keen.VRage.Client.DebugMenu.DebugMenuConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Client.DebugMenu`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CloseAction` | Debug menu close action |
| `CycleTabs` | Switch tabs in debug menu |
| `ToggleFocus` | Toggle menu focus |

## A real one

`Engine\Assets\Configurations\Input\DebugMenuConfiguration.def`

```json
{
  "Guid": "ed32cc53-f72c-45df-87c2-fd0445302eb5",
  "CloseAction": "868dcd74-6f5c-44ce-a4c9-e63c4ff18d5d",
  "CycleTabs": "aaee8734-c163-4d71-8302-1462a369cb64",
  "ToggleFocus": "bd0f95cf-44b8-4f19-926d-b795b4efc90a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DebugMenuConfigurationObjectBuilder')
search_content('', type_contains='DebugMenuConfigurationObjectBuilder')
```
