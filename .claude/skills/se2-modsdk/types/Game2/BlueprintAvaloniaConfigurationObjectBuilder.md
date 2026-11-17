# BlueprintAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Shared.UGC.Blueprint.BlueprintAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Shared.UGC.Blueprint`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DeleteIcon` | Delete icon for blueprint |
| `DetailIcon` | Detail icon for blueprint |
| `DownloadIcon` | Download icon for blueprint |
| `DownvoteIcon` | Downvote icon for blueprint |
| `KeenCreationBlueprintIcon` | Icon for a bundled blueprint |
| `LocalBlueprintIcon` | Icon for local blueprint |
| `OnlineOwnedBlueprintIcon` | Icon for online owned blueprint |
| `PrivateOnlineOwnedBlueprintIcon` | Icon for private online owned blueprint |
| `ScreenshotIcon` | Screenshot for blueprint |
| `SubscribedBlueprintIcon` | Icon for subscribed blueprint |
| `UpvoteIcon` | Upvote icon for blueprint |

## A real one

`Vanilla\Assets\MainMenuData\UGC\Blueprints\BlueprintAvaloniaConfiguration.def`

```json
{
  "Guid": "5e4656ba-c387-44b5-89e6-24aecd658118",
  "DetailIcon": "{G}18e8e0e4-575b-480c-85b0-5b1424b9fecd",
  "DeleteIcon": "{G}709a035d-2036-4fb7-8fda-817fb8363a5a",
  "DownloadIcon": "{G}a3345433-f1d3-4762-8273-597db7aaf042",
  "UpvoteIcon": "{G}ea28f2bc-82c7-411b-b797-ae61428e8868",
  "DownvoteIcon": "{G}59ba378a-deef-466a-8b84-cdd1857e6924",
  "ScreenshotIcon": "{G}72a8598f-b3c5-4787-a328-2e7947d01455",
  "LocalBlueprintIcon": "{G}084318c5-0139-4c84-9247-11e889397656",
  "OnlineOwnedBlueprintIcon": "{G}d48c7ae6-41a1-4ae1-b2d8-3b2d4b158909",
  "SubscribedBlueprintIcon": "{G}9ec4b3db-21b8-464d-bdfd-f3184a23c21d",
  "PrivateOnlineOwnedBlueprintIcon": "{G}6da25c9d-d7e9-4573-a22c-fa070df69002",
  "KeenCreationBlueprintIcon": "{G}e5d91627-3a2c-4de2-b752-48544f3710e0"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlueprintAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='BlueprintAvaloniaConfigurationObjectBuilder')
```
