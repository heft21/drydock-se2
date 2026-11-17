# GScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.GScreen.GScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen.GScreen`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackpackProductionTitle` | Localization key for backpack in production blocks section |
| `CategoryAllName` | Localization key for name of category all |
| `CategoryAllTooltip` | Localization key for tooltip of category all |
| `NextProgressionMilestoneInformationContent` | Localization key for content of next progression milestone tooltip |
| `NextProgressionMilestoneInformationIcon` | Icon used in tile representing information about next progression milestone |
| `NextProgressionMilestoneInformationTitle` | Localization key for title of next progression milestone tooltip |
| `SearchResultsCategoryName` | Localization key for name of search results category |
| `SearchResultsCategoryTooltip` | Localization key for tooltip of search results category |
| `SubcategoryAllName` | Localization key for name of subcategory all |
| `SubcategoryAllTooltip` | Localization key for tooltip of subcategory all |
| `UnknownIcon` | Icon used in a tile when the contents of it are unknown |

## A real one

`Vanilla\Assets\System\Configurations\GScreenConfiguration.def`

```json
{
  "Guid": "25592c6c-5c8b-4542-8a51-59599fd6ecd0",
  "NextProgressionMilestoneInformationTitle": "GScreenNextProgressionMilestoneInformationTitle",
  "NextProgressionMilestoneInformationContent": "GScreenNextProgressionMilestoneInformationContent",
  "NextProgressionMilestoneInformationIcon": "{G}bee2cacf-7661-4e74-a7c4-9bbdd5f95caa",
  "UnknownIcon": "{G}bee2cacf-7661-4e74-a7c4-9bbdd5f95caa",
  "BackpackProductionTitle": "GScreenProductionBlocksBackpackTitle",
  "CategoryAllName": "CategoryAllBlocksName",
  "CategoryAllTooltip": "CategoryAllBlocksTooltip",
  "SearchResultsCategoryName": "SearchResultsCategoryName",
  "SearchResultsCategoryTooltip": "SearchResultsCategoryTooltip",
  "SubcategoryAllName": "SubcategoryAllName",
  "SubcategoryAllTooltip": "SubcategoryAllTooltip"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GScreenConfigurationObjectBuilder')
search_content('', type_contains='GScreenConfigurationObjectBuilder')
```
