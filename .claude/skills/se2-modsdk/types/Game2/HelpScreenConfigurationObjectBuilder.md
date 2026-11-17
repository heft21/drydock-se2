# HelpScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Help.HelpScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Help`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Tabs` | Topics to be displayed on HelpScreen |

## A real one

`Vanilla\Assets\System\Configurations\HelpScreenConfiguration.def`

```json
{
  "Guid": "cad2f0e4-1ea6-496c-9852-1af88930dcd5",
  "Tabs": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('HelpScreenConfigurationObjectBuilder')
search_content('', type_contains='HelpScreenConfigurationObjectBuilder')
```
