# SubcategoryDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.SubcategoryDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **51**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Categories` | Categories to which this subcategory belongs |
| `Name` | Localization key of subcategory name |
| `Order` | Order 0 is special, and will be treated as , so such subcategories will be added to the end. Then subcategories are sorted by localization keys and Guids |
| `Tooltip` | Localization key of subcategory tooltip |

## A real one

`Vanilla\Assets\UI\Screens\GScreen\Armor\HeavyArmorSubcategory.def`

```json
{
  "Guid": "dfeaceb9-9946-44c8-8212-50692a7d80cb",
  "Name": "HeavyArmorSubcategoryName",
  "Tooltip": "HeavyArmorSubcategoryTooltip",
  "Order": 0,
  "Categories": [
    {
      "Key": "24b6a1a1-a4ef-4043-8768-75575808ff5b",
      "Value": "5f499f39-b8e5-48c8-a927-65ea758660c8"
    }
  ]
}
```

Others: `LightArmorSubcategory`, `CockpitsSubcategory`

---

Read it with the MCP server rather than by hand:

```
describe_type('SubcategoryDefinitionObjectBuilder')
search_content('', type_contains='SubcategoryDefinitionObjectBuilder')
```
