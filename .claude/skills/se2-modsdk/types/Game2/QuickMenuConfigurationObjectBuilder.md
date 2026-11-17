# QuickMenuConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.QuickMenuConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HoldTime` | Amount of time an input needs to be held for the quick menu to open |

## A real one

`Vanilla\Assets\System\Configurations\QuickMenuConfiguration.def`

```json
{
  "Guid": "c0277c77-549c-41ba-aaac-bda136650176",
  "HoldTime": 2500000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('QuickMenuConfigurationObjectBuilder')
search_content('', type_contains='QuickMenuConfigurationObjectBuilder')
```
