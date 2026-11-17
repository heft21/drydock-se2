# UIClickAnalyticsConfigurationObjectBuilder

`VRage:Keen.VRage.Analytics.Events.UIClickAnalyticsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Analytics.Events`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AllowedScreenTypes` | Screen types defined in this collection are sent |
| `IgnoredButtonsTypes` | Button types defined in this collection do not send |

## A real one

`Engine\Assets\Configurations\Setup\UIClickAnalyticsConfiguration.def`

```json
{
  "Guid": "f11450f0-3ef5-4b02-ad58-6e544862f38a",
  "AllowedScreenTypes": [
    {
      "Key": "8370014a-2d85-4c1a-8b74-a4c4c1b85a5e",
      "Value": "Character > Character"
    },
    {
      "Key": "e281fd5f-3376-4058-bd3a-7a3c4c69ca5b",
      "Value": "Build > Blocks"
    },
    {
      "Key": "4fb2b3d6-bcfc-43c5-95a6-393daa1fb75d",
      "Value": "NewGameMenuScreen"
    },
    {
      "Key": "160bf067-ea7c-42ad-9ef1-ee9b133db911",
      "Value": "OptionsScreen"
    },
    {
      "Key": "29696638-7b39-42c8-a1f1-f48ba8ff2c07",
      "Value": "Grid > Inventory"
    },
    {
      "Key": "7ae09867-9214-47ec-88a2-027a03fb6651",
      "Value": "Build > Blueprints"
    },
    {
      "Key": "08e6b448-a2b1-4f4a-8f2e-db5fda54d0ef",
      "Value": "DetailsScreen"
    },
    {
      "Key": "4afbc372-f68e-4c16-962b-ef3856054234",
      "Value": "Grid > ControlPanel"
    },
    {
      "Key": "e12bc7b9-3bcb-4b09-bca3-072a49568eaf",
      "Value": "ScenarioSelectionScreen"
    },
    {
      "Key": "76bf0679-6e69-4e23-a10f-9f21775bfe19",
      "Value": "ManageModsScreen"
    },
    {
      "Key": "1dc4bb7a-3b72-45ef-8877-bd9517ae7dbd",
      "Value": "QuickMenuScreen"
    },
    {
      "Key": "7b3e50c5-0f89-483d-a29c-156dac018e04",
      "Value": "WorkshopScreen"
    },
    {
      "Key": "df967652-c6d9-40b0-a84d-34803a32f167",
      "Value": "MapScreen"
    },
    {
      "Key": "d4db5a93-138b-42d9-bfd4-50769d5e78ef",
      "Value": "HelpScreen"
    },
    {
      "Key": "65d0a5e1-db0d-43cd-a2c9-83ed1cc4451c",
      "Value": "Grid > Production"
    },
    {
      "Key": "16e6889b-ec3a-45a1-a0bb-1213e363958a",
      "Value": "MainMenuScreen"
    },
    {
      "Key": "0de0638b-762b-4b35-ba35-74766ab4a47a",
      "Value": "TerminalScreen"
    }
  ],
  "IgnoredButtonsTypes": [
    {
      "Key": "c8a0a161-fcf2-4987-8418-521fb8228935",
      "Value": "ScrollerView"
    },
    {
      "Key": "a3a3b09a-0cf6-4a70-88f8-e25edf4f4d17",
      "Value": "Back"
    },
    {
      "Key": "93ac426d-b261-47d2-83ea-3576b99ab255",
      "Value": "Yes"
    },
    {
      "Key": "62817c3c-1cc3-4cfa-84b1-2300de4833c7",
      "Value": "No"
    },
    {
      "Key": "f9abc355-1437-4464-b2b3-8bd20a8d3161",
      "Value": "Exit"
    },
    {
      "Key": "50b470f9-6ae5-416d-8f15-e49807406c9f",
      "Value": "Cancel"
    },
    {
      "Key": "857063c8-3f8b-4152-8ed9-7e52f4ab822f",
      "Value": "Close"
    },
    {
      "Key": "9e721146-a8a3-4a71-956c-1154491fed93",
      "Value": ""
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UIClickAnalyticsConfigurationObjectBuilder')
search_content('', type_contains='UIClickAnalyticsConfigurationObjectBuilder')
```
