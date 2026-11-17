# BlockKindDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.BlockKindDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **223**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlockGroups` | Groups to which this block kind belongs. The block kind will be inserted there using automatic rules. Check for more information regarding insertion rules. |
| `Description` | Localization key of blocks description inside the block kind |
| `Name` | Localization key of block kind name |
| `OrderingPriority` | Affects on block kinds order in . Check for detailed description of block kinds sorting rules |

## A real one

`Vanilla\Assets\UI\Screens\GScreen\Decor\Interior\Crate\CrateBlockKind.def`

```json
{
  "Guid": "e2588836-5b6f-4513-9559-b36c9e488527",
  "Name": "Crate",
  "Description": "CrateDesc",
  "OrderingPriority": 0,
  "BlockGroups": [
    {
      "Key": "24ba99f5-8eeb-4550-94bb-872cd65b3b75",
      "Value": "96dc82f8-52a7-455c-9460-b493f6d88d53"
    }
  ]
}
```

Others: `BedBlockKindDefinition`, `DrillBlockKindDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockKindDefinitionObjectBuilder')
search_content('', type_contains='BlockKindDefinitionObjectBuilder')
```
