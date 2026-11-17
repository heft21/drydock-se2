# HotKeySessionComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.Input.HotKeySessionComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.Input`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActivateBlueprintCreationTool` | Activates the blueprint creation tool |
| `CopyGrid` | Input to activate block placer copy (even if build mode is not active) |
| `CopyGridRaycastDetectorTag` | Tag used to find a raycast detector on the possessed entity when copy pasting |
| `CutGrid` | Input to activate block placer cut (even if build mode is not active) |
| `GPSMarkersChangeLevelOfDetails` | Input to change level of details for GPS markers |
| `InputContextDefinition` | Input context settings |
| `MenuScreen` | Input to open game menu |
| `MessageColor` | Color of the reloading/reload complete messages |
| `MissionEditor` | Input to open MissionEditor |
| `PartialCopyGrid` | Input to activate partial grid copy (even if build mode is not active) |
| `PasteGrid` | Input to activate block placer paste (even if build mode is not active) |
| `ReloadGame` | Input to quick-load last save game |
| `SaveGame` | Input to quick-save current scene |
| `ToggleUIVisibility` | Input to toggle UI rendering |

## A real one

`Vanilla\Assets\UI\MenuScreen.def`

```json
{
  "Guid": "392e0631-7559-4b07-9403-4151b7a9684b",
  "InputContextDefinition": "5f75de3d-75b5-4127-b1f6-90536836fcca",
  "SaveGame": "7ac1e2a8-f506-4ed8-93ad-23d82f45fb1a",
  "ReloadGame": "7febc62c-aecf-449e-93e1-f2dddf541018",
  "MenuScreen": "3f82acb2-793c-4ad0-8e6b-b179c9fa8953",
  "ToggleUIVisibility": "33850909-2e8f-4210-8008-f11f371f1d82",
  "CopyGrid": "611c5883-be69-4bf2-8833-6abb79991124",
  "CutGrid": "0492b0d4-e90b-4550-95a7-399117454701",
  "PasteGrid": "2ca6011c-2d70-4ac1-9b24-c56e28c8eae8",
  "PartialCopyGrid": "93dd2107-8e97-49c9-a463-bd75de97c015",
  "ActivateBlueprintCreationTool": "55a16a1a-da37-499e-bafd-95cf4058da98",
  "GPSMarkersChangeLevelOfDetails": "86a23a0c-6bb5-4743-b3ca-9b7f695a8a8a",
  "MissionEditor": "d80b4c88-7732-47f9-955f-775c2cd45bc5",
  "TogglePause": "3e15315f-0275-4547-8e4b-2f6b9bf1b1c4",
  "TeleportToNPC": "799250c1-70be-45c1-8f86-21b0c95f54fe",
  "SelectNPC": "aed9bda5-9b15-4c2e-a23a-69a6bd32d81b",
  "CopyGridRaycastDetectorTag": "FarDetectorComponent",
  "MessageColor": {
    "PackedValue": 4294967295
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('HotKeySessionComponentDefinitionObjectBuilder')
search_content('', type_contains='HotKeySessionComponentDefinitionObjectBuilder')
```
