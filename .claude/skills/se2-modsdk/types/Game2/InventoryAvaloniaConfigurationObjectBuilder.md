# InventoryAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.Character.InventoryAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterAsset` | Asset for the character |
| `ConnectedHoveredIcon` | Icon used to represent the "Connected" state when hovered. |
| `ConnectedIcon` | Icon used to represent the "Connected" state |
| `HideEmptyHoveredIcon` | Icon used to represent the "hide empty slots" state when hovered. |
| `HideEmptyIcon` | Icon used to represent the "hide empty slots" state in the default state. |
| `NotConnectedHoveredIcon` | Icon used to represent the "Not Connected" state when hovered. |
| `NotConnectedIcon` | Icon used to represent the "Not Connected" state |
| `ShowEmptyHoveredIcon` | Icon used to represent the "show empty slots" state when hovered. |
| `ShowEmptyIcon` | Icon used to represent the "show empty slots" state in the default UI state. |

## A real one

`Vanilla\Assets\MainMenuData\UI\Terminal\InventoryAvaloniaConfiguration.def`

```json
{
  "Guid": "b2e9d2b8-1c8d-4e0a-95b7-ef01de1dc88a",
  "CharacterAsset": "{G}7f0b4144-1b4a-4eef-bd07-4edf6404caba",
  "ShowEmptyIcon": "{G}887a6607-1438-4096-8029-f432921af07a",
  "ShowEmptyHoveredIcon": "{G}5b855e5d-0819-4fc7-828c-dff1a9af06c6",
  "HideEmptyIcon": "{G}6ac75b07-27f2-444d-a3d6-348ce5f5f8f0",
  "HideEmptyHoveredIcon": "{G}4f708f3c-e3bd-4025-8232-b2e48cf2b646",
  "ConnectedIcon": "{G}3d975ff4-9287-40a4-8a0d-15992c722df6",
  "ConnectedHoveredIcon": "{G}cc7c7689-d640-4e28-9b22-a59ef38cf2c5",
  "NotConnectedIcon": "{G}3a18d173-88b8-49e1-a2fd-5afb74206481",
  "NotConnectedHoveredIcon": "{G}1cbb6cfd-a5b4-484c-9019-805126fbadd1",
  "QuestIcon": "{G}677561b7-23f3-44e7-b8c6-77d2d3b00e90"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='InventoryAvaloniaConfigurationObjectBuilder')
```
