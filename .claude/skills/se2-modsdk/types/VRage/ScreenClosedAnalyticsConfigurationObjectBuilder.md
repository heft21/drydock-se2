# ScreenClosedAnalyticsConfigurationObjectBuilder

`VRage:Keen.VRage.UI.EngineComponents.ScreenClosedAnalyticsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.UI.EngineComponents`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AllowedScreenTypes` | Screen types defined in this collection do send |

## A real one

`Engine\Assets\Configurations\Setup\ScreenClosedAnalyticsConfiguration.def`

```json
{
  "Guid": "3cc71d90-a426-4c65-9089-156d33951aa8",
  "AllowedScreenTypes": [
    {
      "Key": "44b6b84f-13db-47f8-8640-d8d822793295",
      "Value": "MainMenuScreen"
    },
    {
      "Key": "c7229240-aa1f-470e-bfeb-418fed837679",
      "Value": "Character > Character"
    },
    {
      "Key": "435bdd5f-4a42-42f0-b7dd-5887e1e43d1e",
      "Value": "Build > Blocks"
    },
    {
      "Key": "1df2ddfa-fe51-4394-b0a7-9326199a8918",
      "Value": "NewGameMenuScreen"
    },
    {
      "Key": "f73bb38f-ebb4-47d3-9dad-03e44cc17693",
      "Value": "OptionsScreen"
    },
    {
      "Key": "6bbeb424-aa84-4048-b084-01bd97abd5c7",
      "Value": "Grid > Inventory"
    },
    {
      "Key": "b7622052-6779-4e84-b2b3-106b70428769",
      "Value": "Build > Blueprints"
    },
    {
      "Key": "645944a4-fb31-426a-b351-116208cf0772",
      "Value": "DetailsScreen"
    },
    {
      "Key": "3f9ff716-4007-4334-ac79-6502e32b4759",
      "Value": "Grid > ControlPanel"
    },
    {
      "Key": "22f80ab0-4d8d-4b42-9211-dbd43dea25fe",
      "Value": "ScenarioSelectionScreen"
    },
    {
      "Key": "c25152c3-db68-48fa-affd-ee3df3a720a3",
      "Value": "ManageModsScreen"
    },
    {
      "Key": "1e469ae7-23c5-4666-b128-25753ce4a3c7",
      "Value": "QuickMenuScreen"
    },
    {
      "Key": "bff02215-ea3c-4b13-b3cf-728619929236",
      "Value": "WorkshopScreen"
    },
    {
      "Key": "5c77ecda-a511-46b2-920d-33e28aa3f859",
      "Value": "MapScreen"
    },
    {
      "Key": "e265222b-c40a-4b10-b547-de2466639911",
      "Value": "HelpScreen"
    },
    {
      "Key": "f1f22000-5559-4c5c-9cae-c43b2696f509",
      "Value": "Grid > Production"
    },
    {
      "Key": "e7fb69e3-ee33-4d2a-92fb-02ffc5827cbd",
      "Value": "Grid > Production"
    },
    {
      "Key": "b1984ed0-0a26-4f66-ada4-bf1e961007fd",
      "Value": "LoadMenuScreen"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ScreenClosedAnalyticsConfigurationObjectBuilder')
search_content('', type_contains='ScreenClosedAnalyticsConfigurationObjectBuilder')
```
