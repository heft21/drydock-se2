# ConnectorStyleDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Tutorial.Connectors.ConnectorStyleDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Tutorial.Connectors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Color` | Line color |
| `EndCap` | End cap shape |
| `StartCap` | Start cap shape |
| `Thickness` | Line thickness |

## A real one

`Vanilla\Assets\UI\Tutorials\Styles\DefaultConnectorStyle.def`

```json
{
  "Guid": "b1628341-0419-4bef-8bd6-af6a1af3a3c8",
  "Color": {
    "PackedValue": 4278251775
  },
  "Thickness": 3,
  "StartCap": {
    "Kind": "None",
    "Size": 0
  },
  "EndCap": {
    "Kind": "Arrow",
    "Size": 16
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ConnectorStyleDefinitionObjectBuilder')
search_content('', type_contains='ConnectorStyleDefinitionObjectBuilder')
```
