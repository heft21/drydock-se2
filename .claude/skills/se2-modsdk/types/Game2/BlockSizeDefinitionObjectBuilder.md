# BlockSizeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.BlockSizeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Icon` | Block size icon that is used on the size indicator when this block size is available for the selected block kind |
| `Name` | Localization key of block size name |
| `RelativeBlockSize` | A unique value used to compare the size with other block sizes. |
| `UnavailableIcon` | Block size icon that is used on the size indicator to display that this block size is not available for the selected block kind |

## A real one

`Vanilla\Assets\UI\Screens\GScreen\BlockSizes\BlockSize1.def`

```json
{
  "Guid": "7ffccf4b-3536-4bf7-b224-0b1a809e81b3",
  "Name": "BlockSize1Name",
  "RelativeBlockSize": 1,
  "Icon": "{G}fe07c6b6-73e9-4c8b-b3ec-cd73aa1d6be5",
  "UnavailableIcon": "{G}f2668719-fde2-4425-b11c-34695e891a1a"
}
```

Others: `BlockSize2`, `BlockSize3`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockSizeDefinitionObjectBuilder')
search_content('', type_contains='BlockSizeDefinitionObjectBuilder')
```
