# QuickMenuDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Library.Controls.QuickMenu.QuickMenuDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Library.Controls.QuickMenu`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CancelRadialMenu` | Input action to close/cancel the radial menu |

## A real one

`Vanilla\Assets\UI\QuickMenuDefinition.def`

```json
{
  "Guid": "183da096-9d49-4d8c-9954-7c00153ed90e",
  "CancelRadialMenu": "4c45b354-3848-44f2-8c61-f254a3b1cd6b"
}
```

Others: `TerrainSculptor_QuickMenuDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('QuickMenuDefinitionObjectBuilder')
search_content('', type_contains='QuickMenuDefinitionObjectBuilder')
```
