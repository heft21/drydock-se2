# CategoryDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.CategoryDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **18**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Name` | Localization key of category name |
| `Order` | Order 0 is special, and will be treated as , so such categories will be added to the end. Then categories are sorted by localization keys and Guids |
| `Tooltip` | Localization key of category tooltip |

## A real one

`Vanilla\Assets\UI\Screens\GScreen\ArmorCategory.def`

```json
{
  "Guid": "5f499f39-b8e5-48c8-a927-65ea758660c8",
  "Name": "ArmorCategoryName",
  "Tooltip": "ArmorCategoryTooltip",
  "Order": 0
}
```

Others: `DecorCategory`, `ControlCategory`

---

Read it with the MCP server rather than by hand:

```
describe_type('CategoryDefinitionObjectBuilder')
search_content('', type_contains='CategoryDefinitionObjectBuilder')
```
