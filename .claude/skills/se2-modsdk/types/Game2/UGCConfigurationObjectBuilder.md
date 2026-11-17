# UGCConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Worlds.UGCConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Worlds`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlueprintCategories` | Contains the categories for the blueprint tags |
| `BlueprintDetailsTitle` | Title shown in the blueprint details screen |
| `BlueprintSearchText` | Search string for the Blueprint search text box |
| `BlueprintTypeTag` | Tag added to all blueprints |
| `BundledUGCAuthorName` | The author name to be shown for bundled UGC items |
| `BundledUGCTooltip` | Tooltip for bundled UGC item |
| `DefaultVisibilityOnPublish` | Tooltip for unsubscribing to a UGC item |
| `DeleteTooltip` | Tooltip for deleting to a UGC item |
| `LocalUGCTooltip` | Tooltip for local UGC item |
| `MinSearchLength` | Minimum length of the search string for the UGC search |
| `ModCategories` | Contains the categories for the mod tags |
| `ModSearchText` | Search string for the Blueprint search text box |
| `ModTypeTag` | Tag added to all worlds |
| `ModsDetailsTitle` | Title shown in the world details screen |
| `PrivatePublishedUGCTooltip` | Tooltip for privately published UGC item |
| `PublicPublishedUGCTooltip` | Tooltip for publicly published UGC item |
| `SortByCreationDateKey` | Key of sort by creation date text |
| `SortByDate` | Local sorting method name for Sorting by Date |
| `SortByLastUpdatedKey` | Key of sort by last update text |
| `SortByName` | Local sorting method name for Sorting by Name |
| `SortByPopularityKey` | Key of sort by popularity text |
| `SortBySubscribersKey` | Key of sort by subscribers text |
| `SubscribeTooltip` | Tooltip for subscribing to a UGC item |
| `SubscribedUGCTooltip` | Tooltip for subscribed UGC item |
| `UnsubscribeTooltip` | Tooltip for unsubscribing to a UGC item |
| `WorldCategories` | Contains the categories for the world tags |
| `WorldContainerTypeTag` | Tag added to all worlds |
| `WorldDetailsTitle` | Title shown in the world details screen |
| `WorldSearchText` | Search string for the Blueprint search text box |

## A real one

`Vanilla\Assets\MainMenuData\UGC\UGCConfiguration.def`

```json
{
  "Guid": "c4bdc6b6-b2d8-4ea2-bfc0-6244c698131b",
  "BundledUGCAuthorName": "KeenSoftwareHouse",
  "SubscribeTooltip": "DetailsScreenSubscribe",
  "DeleteTooltip": "DetailsScreenDelete",
  "UnsubscribeTooltip": "DetailsScreenUnsubscribe",
  "SortByPopularityKey": "SortByPopularity",
  "SortBySubscribersKey": "SortBySubscribers",
  "SortByCreationDateKey": "SortByCreationDate",
  "SortByLastUpdatedKey": "SortByLastUpdated",
  "DefaultVisibilityOnPublish": "Public",
  "BlueprintDetailsTitle": "BlueprintDetailsScreenTitle",
  "WorldDetailsTitle": "WorldDetailsScreenTitle",
  "ModsDetailsTitle": "ModDetailsScreenTitle",
  "BlueprintCategories": [
    {
      "Key": "3c4dbbed-a936-4423-8c5b-da29498ff52c",
      "Value": {
        "Name": "BPTagCategory",
        "Tags": [
          "BPTagCreative",
          "BPTagExploration",
          "BPTagMining",
          "BPTagModule",
          "BPTagSpace",
          "BPTagSpacecraft",
          "BPTagStation"
        ]
      }
    }
  ],
  "WorldCategories": [
    {
      "Key": "5e0cf004-857d-4227-be5b-4278e1968a19",
      "Value": {
        "Name": "WorldTagsCategory",
        "Tags": [
          "WorldTagCreative",
          "WorldTagExploration",
          "WorldTagShowcase",
          "WorldTagSpaceFocused",
          "WorldTagTestingWorld"
        ]
      }
    }
  ],
  "ModCategories": [
    {
      "Key": "484d171d-4075-41b1-9035-3f4ebdb03d17",
      "Value": {
        "Name": "ModTagCategory",
        "Tags": [
          "ModTagArmor",
          "ModTagAudio",
          "ModTagAsteroid",
          "ModTagBlock",
          "ModTagCharacter",
          "ModTagMaterial",
          "ModTagParticles",
          "ModTagSkybox",
          "ModTagOther"
        ]
      }
    }
  ],
  "BlueprintTypeTag": "UGCBlueprintTypeTag",
  "WorldContainerTypeTag": "UGCWorldTypeTag",
  "ModTypeTag": "UGCModTypeTag",
  "MinSearchLength": 2,
  "BlueprintSearchText": "SearchBlueprints",
  "WorldSearchText": "SearchWorlds",
  "ModSearchText": "SearchMods",
  "SortByName": "SortName",
  "SortByDate": "SortDate",
  "LocalUGCTooltip": "Local",
  "PublicPublishedUGCTooltip": "PublicPublished",
  "PrivatePublishedUGCTooltip": "PrivatePublished",
  "SubscribedUGCTooltip": "Subscribed",
  "BundledUGCTooltip": "KeenCreation"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UGCConfigurationObjectBuilder')
search_content('', type_contains='UGCConfigurationObjectBuilder')
```
