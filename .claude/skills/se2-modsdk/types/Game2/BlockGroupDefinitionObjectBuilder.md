# BlockGroupDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.BlockGroupDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **262**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlockKinds` | Use this collection to manually set order for block kinds in the group. Other block kinds belonging to it will be added automatically during post-processing step: they will be sorted by ordering priorities, localization keys and Guids, and then inserted according to ordering priorities. The block kind with specified ordering priority will be inserted after the last block kind that has higher ordering priority. Ordering priority 0 is special, and will be treated as >. Other block kinds will be simply appended to the end of the group. |

## A real one

`Vanilla\Assets\UI\Screens\GScreen\Decor\LCDs\Groups\LCDAll.def`

```json
{
  "Guid": "4086f17d-3d28-4c30-9e9a-25e190fba520",
  "Name": "LCD",
  "Order": 0,
  "Subcategories": [
    {
      "Key": "3ee62864-092f-457e-a3ba-9e76af4e36fe",
      "Value": "dd74ab72-433e-4952-8188-d3d83c3d5ade"
    }
  ],
  "BlockKinds": []
}
```

Others: `SeatBlockGroup`, `CrateBlockGroup`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockGroupDefinitionObjectBuilder')
search_content('', type_contains='BlockGroupDefinitionObjectBuilder')
```
