# InventoryStreamedUIConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Terminal.Inventories.InventoryStreamedUIConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Terminal.Inventories`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CombinedNameFormat` | Format the names of entity and its parent. Use {Child} and {Parent} as placeholders for respective names. |
| `DefaultDropDistance` | Default distance from player item is dropped. |
| `DefaultEntityName` | Default name used if entity has no name |
| `DefaultInventoryName` | Default name that will be assigned to the inventory if it does not have custom one |

## A real one

`Vanilla\Assets\System\Configurations\InventoryStreamedUIConfiguration.def`

```json
{
  "Guid": "a66f7c1e-8561-4a7c-b467-682993fd2d35",
  "DefaultInventoryName": "DefaultInventoryName",
  "CombinedNameFormat": "FullInventoryNameFormat",
  "AccessedCombinedNameFormat": "AccessedFullInventoryNameFormat",
  "DefaultEntityName": "DefaultEntityName",
  "DefaultDropDistance": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryStreamedUIConfigurationObjectBuilder')
search_content('', type_contains='InventoryStreamedUIConfigurationObjectBuilder')
```
