# ItemDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Items.ItemDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Items`
- definitions using it: **31**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultMetaData` | The default meta data applied when a new item is created. |
| `Description` | Description of the item. |
| `DisplayName` | Display name of the item. |
| `ExplosiveRisk` | Explosive risk per unit of ammo. Used to estimate explosion size when an inventory holding this ammo is destroyed. A value of 0 means the ammo is inert. |
| `Flags` | Specify item stacking behavior |
| `Icon` | Icon used to represent this item on the player HUD |
| `IsRareLoot` | Defines this item as a rare loot item |
| `MassPerUnit` | Weight of one unit of this item |
| `Type` | Specify the type(s) this item belongs to |

## A real one

`Vanilla\Assets\Items\Ores\IceOre\IceOreItem.def`

```json
{
  "Guid": "6ae64849-8c10-4341-88da-dbe385cbb3bb",
  "DisplayName": "OreIce",
  "Description": "",
  "Icon": "{G}17324d0f-c41c-4082-804b-b3784814e0a7",
  "VolumePerUnit": 0.0001,
  "MassPerUnit": 1,
  "Flags": "PresetNormal",
  "Type": "Ore",
  "DefaultMetaData": null
}
```

Others: `GoldOre_Item`, `IronOre_Item`

---

Read it with the MCP server rather than by hand:

```
describe_type('ItemDefinitionObjectBuilder')
search_content('', type_contains='ItemDefinitionObjectBuilder')
```
