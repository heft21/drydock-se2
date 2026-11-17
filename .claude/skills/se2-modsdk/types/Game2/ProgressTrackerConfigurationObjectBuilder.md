# ProgressTrackerConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Missions.Progress.ProgressTrackers.ProgressTrackerConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Missions.Progress.ProgressTrackers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GridBuildCompletedCompletedBlockCount` | Text formating key for for displaying amount of completed blocks |
| `GridBuildCompletedPercentageBlockCount` | Text formating key for for displaying percentage of blocks built |
| `GridBuildCompletedTotalBlockCount` | Text formating key for for displaying total amount of blocks to build |
| `GridBuiltInAreaBlockAmount` | Text formating key for for displaying block counts on candidate grid There can be many different blocks, number is appended to each group: "ItemAmount" -> {ItemAmount0}, {ItemAmount1}, ... |
| `GridBuiltInAreaGridAmount` | Text formating key for for displaying amount of grids in area |
| `GridBuiltInAreaPcuAmount` | Text formating key for for displaying amount of PCU on candidate grid |
| `GridBuiltInAreaUnfinishedBlockAmount` | Text formating key for for displaying amount of blocks that are not finished |
| `IsPCUInRangeCurrent` | Text formating key for for displaying current PCU count |
| `IsPCUInRangeMax` | Text formating key for for displaying maximum PCU required |
| `IsPCUInRangeMin` | Text formating key for for displaying minimum PCU required |
| `ItemInInventoryAmountCurrent` | Text formating key for for displaying current amount of items |
| `ItemInInventoryAmountPercentage` | Text formating key for for displaying percentage of items ready |
| `ItemInInventoryAmountTotal` | Text formating key for for displaying total amount of items needed |
| `ItemInInventoryItemName` | Text formating key for for displaying item name |

## A real one

`Vanilla\Assets\System\Configurations\ProgressTrackerConfiguration.def`

```json
{
  "Guid": "081ea5ea-2a0c-4d7d-b40d-e10ec113972e",
  "ItemInInventoryItemName": "ItemName",
  "ItemInInventoryAmountCurrent": "ItemAmountCurrent",
  "ItemInInventoryAmountTotal": "ItemAmountTarget",
  "ItemInInventoryAmountPercentage": "ItemAmountPercentage",
  "GridBuildCompletedCompletedBlockCount": "COMPLETED",
  "GridBuildCompletedTotalBlockCount": "TOTAL",
  "GridBuildCompletedPercentageBlockCount": "PERCENTAGE"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ProgressTrackerConfigurationObjectBuilder')
search_content('', type_contains='ProgressTrackerConfigurationObjectBuilder')
```
