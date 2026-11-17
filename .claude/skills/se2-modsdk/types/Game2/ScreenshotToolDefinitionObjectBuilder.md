# ScreenshotToolDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.ScreenshotToolDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BannerTitle` | Title of the banner shown at the top of the screen. |
| `Cancel` | Abort selection |
| `CancelInputHintText` | Cancel hint text |
| `ConsumedInputKinds` | Inputs consumed by component |
| `InputContext` | Input context for the tool |
| `PassedInputKinds` | Inputs ignored/passed-through by component |
| `TakeScreenshot` | Capture the grid in front of the player |
| `TakeScreenshotInputHintText` | Take Screenshot hint text |
| `TooltipTitle` | Title to display on the dynamic tooltip when tool is active |

## A real one

`Vanilla\Assets\System\Tools\ScreenshotToolDefinition.def`

```json
{
  "Guid": "51b68dac-2907-448f-be5c-326b11632caa",
  "InputContext": "f9ddebfd-3dc4-4e86-8e05-64d7360d6093",
  "TakeScreenshot": "999a7130-521d-4def-8c11-e30205786151",
  "Cancel": "746e1125-883f-494a-a20a-53de11e731ab",
  "ConsumedInputKinds": [
    "",
    "Tools"
  ],
  "PassedInputKinds": [
    "Movement",
    "Rotation",
    "Interaction",
    "Toolbar",
    "Utility"
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ScreenshotToolDefinitionObjectBuilder')
search_content('', type_contains='ScreenshotToolDefinitionObjectBuilder')
```
