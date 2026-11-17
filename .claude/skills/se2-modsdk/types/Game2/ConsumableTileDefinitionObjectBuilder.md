# ConsumableTileDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.ConsumableTileDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Consumable` | The tool in this group |
| `Description` | Tool description |

## A real one

`Vanilla\Assets\UI\Screens\GScreen\CharacterGear\MedikitTileDefinition.def`

```json
{
  "Guid": "ff555089-55eb-42cf-a27c-2cabf920678b",
  "Name": "ConsumableMedikit",
  "Order": 0,
  "Subcategories": [
    {
      "Key": "113ddb45-aff9-4df9-bd83-7ec65901b41d",
      "Value": "833e54c6-7fb3-4e6d-8ebf-f4967758a41c"
    }
  ],
  "Consumable": "3042ad6b-e888-4ee0-9e04-bf7cf77afd4a",
  "Description": "ConsumableMedKitDesc"
}
```

Others: `SuitBatteryTileDefinition`, `OxygenRechargeTileDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ConsumableTileDefinitionObjectBuilder')
search_content('', type_contains='ConsumableTileDefinitionObjectBuilder')
```
