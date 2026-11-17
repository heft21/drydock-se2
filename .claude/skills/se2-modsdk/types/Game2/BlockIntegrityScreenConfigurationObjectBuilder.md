# BlockIntegrityScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Blocks.BlockIntegrityScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Blocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CraftingIcon` | Icon displayed for the crafting in progress |
| `FullAmountIcon` | Icon displayed for when the full required amount for the specific crafting component is added. |
| `InventoryIcon` | Icon displayed for the inventory |
| `PartialAmountIcon` | Icon displayed for when the full required amount for the specific crafting component is not yet added. |

## A real one

`Vanilla\Assets\UI\HUD\BlockIntegrityScreenConfiguration.def`

```json
{
  "Guid": "b52b3e37-e087-4eb2-b1c1-940ddd4d2523",
  "InventoryIcon": "{G}4c242a22-9886-417b-a4d9-c386ac4c2349",
  "CraftingIcon": "{G}20b83fc7-e053-41d8-aac4-b59df4e86563",
  "PartialAmountIcon": "{G}d62a1557-d103-4fda-b640-c2fd1dbe4946",
  "FullAmountIcon": "{G}a9180919-6ff0-4e12-a38d-df01b5cf58a8"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockIntegrityScreenConfigurationObjectBuilder')
search_content('', type_contains='BlockIntegrityScreenConfigurationObjectBuilder')
```
