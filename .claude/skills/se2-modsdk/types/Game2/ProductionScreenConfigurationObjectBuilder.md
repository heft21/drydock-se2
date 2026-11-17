# ProductionScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.Production.ProductionScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen.Production`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DestroyedNotification` | Notification shown when a production block with any queued recipes is destroyed |
| `FailurePriorities` | Items at the start of the collection are highest priority, and will be shown first. |
| `FailureTips` | Tooltips shown when there are issues preventing recipes from running |
| `MaxTips` | Maximum number of tips that can be shown at once |
| `ResourcesRequiredTextKey` | Text displayed in the header of the required Bill of Materials (BOM) control. |
| `TotalResourcesRequiredTextKey` | Text displayed in the header of the total required Bill of Materials (BOM) control. |

## A real one

`Vanilla\Assets\System\Configurations\ProductionScreenConfiguration.def`

```json
{
  "Guid": "0bc8a82a-3746-4722-b8aa-b8566600a319",
  "DestroyedNotification": "d354627d-f001-4448-8e0d-070906fe7c12",
  "FailureTips": {
    "Disabled": {
      "Title": "ProductionFailureReasonDisabledTitle",
      "Description": "ProductionFailureReasonDisabledDescription"
    },
    "Unfunctional": {
      "Title": "ProductionFailureReasonUnfunctionalTitle",
      "Description": "ProductionFailureReasonUnfunctionalDescription"
    },
    "InventoryFull": {
      "Title": "ProductionFailureReasonInventoryFullTitle",
      "Description": "ProductionFailureReasonInventoryFullDescription"
    },
    "MissingItems": {
      "Title": "ProductionFailureReasonMissingItemsTitle",
      "Description": "ProductionFailureReasonMissingItemsDescription"
    },
    "MissingResource": {
      "Title": "ProductionFailureReasonMissingResourceTitle",
      "Description": "ProductionFailureReasonMissingResourceDescription"
    }
  },
  "MaxTips": 1,
  "FailurePriorities": [
    {
      "Key": "09d04cc0-5b40-4c9c-a6db-edea9e5a1bed",
      "Value": "None"
    },
    {
      "Key": "3bd326c4-befc-4d54-9208-9c8fc1e6a106",
      "Value": "Disabled"
    },
    {
      "Key": "5a432376-394c-4dd2-a9e5-ebc8e5eaa341",
      "Value": "Unfunctional"
    },
    {
      "Key": "ea4dc7c0-5dca-429c-8fed-9a06bbe7d034",
      "Value": "InventoryFull"
    },
    {
      "Key": "991e2695-daff-4aed-b9b3-5be518bd7821",
      "Value": "MissingItems"
    },
    {
      "Key": "c215e1dc-11f8-41a1-9da7-df455633b7f2",
      "Value": "MissingResource"
    }
  ],
  "ResourcesRequiredTextKey": "ProductionScreenResourcesRequired",
  "TotalResourcesRequiredTextKey": "ProductionScreenTotalResourcesRequired"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ProductionScreenConfigurationObjectBuilder')
search_content('', type_contains='ProductionScreenConfigurationObjectBuilder')
```
