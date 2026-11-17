# SpherePreviewDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Preview.SpherePreviewDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Preview`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FillColor` | Sphere fill color |
| `OutlineColor` | Sphere outline color |

## A real one

`Vanilla\Assets\Procedural\VS1_5\System\Data\Planets\SpherePreviewDefinition.def`

```json
{
  "Guid": "289071f7-c0fc-4f9c-9950-41a1329126f0",
  "FillColor": {
    "PackedValue": 1073774592
  },
  "OutlineColor": {
    "PackedValue": 4278222848
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SpherePreviewDefinitionObjectBuilder')
search_content('', type_contains='SpherePreviewDefinitionObjectBuilder')
```
