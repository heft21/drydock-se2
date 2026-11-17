# BlueprintCreationToolDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.BlueprintCreationToolDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems`
- definitions using it: **1**

## What it is

Definition for

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Cancel` | Abort selection |
| `CancelInputHintText` | Cancel input hint text |
| `CaptureBlueprint` | Capture the grid in front of the player |
| `ConfirmInputHintText` | Confirm/capture input hint text |
| `ConsumedInputKinds` | Inputs consumed by component |
| `CreationBannerTitle` | Banner title when creating a new blueprint |
| `HighlightCornerLengthPercent` | Length of the corners in the highlight outline, as a percentage of the length of the shortest side |
| `HighlightDashLengthPercent` | Length of the dashes in the highlight outline, as a percentage of the length of the shortest side |
| `HighlightTargetGridColor` | Outline color of the targeted grid |
| `HighlightThickness` | Thickness around the bounding box highlight |
| `HighlightThicknessFarScale` | Scale of the outlines when it is at the far distance or beyond |
| `HighlightThicknessScaleFarDistance` | Distance at which outline thickness will reach the far scale |
| `HighlightThicknessScaleNearDistance` | Distance at which outline thickness will start scaling |
| `InputContext` | Input context for the tool |
| `PassedInputKinds` | Inputs ignored/passed-through by component |
| `RaycastDetectorTag` | Tag used to find a raycast detector on the possessed entity when targeting a blueprint |
| `ReplaceBannerTitle` | Banner title when replacing an existing blueprint |
| `TooltipDescription` | Description for the dynamic tooltip, supports {grid} parameter |
| `TooltipTitle` | Title to display on the dynamic tooltip when tool is active |
| `UpdateScreenshotOnReplace` | Take a new screenshot and replace previous one when modifying an existing blueprint |

## A real one

`Vanilla\Assets\System\Tools\BlueprintCreationToolDefinition.def`

```json
{
  "Guid": "f981b6c5-10c2-4a0e-b4dc-5695009a5f9d",
  "InputContext": "ba9a8c9a-01e9-4900-be1e-92a7e270296e",
  "CaptureBlueprint": "eb4f13d9-5f0a-439b-9627-6d843ffd6a71",
  "Cancel": "ca496a3b-aa24-4054-9641-e0f2f16cdab1",
  "RaycastDetectorTag": "FarDetectorComponent",
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
  ],
  "HighlightTargetGridColor": {
    "PackedValue": 4278232575
  },
  "HighlightCornerLengthPercent": 0.25,
  "HighlightDashLengthPercent": 0.25,
  "HighlightThicknessScaleNearDistance": 10,
  "HighlightThicknessScaleFarDistance": 65,
  "HighlightThicknessFarScale": 0.9,
  "HighlightThickness": 1.1,
  "UpdateScreenshotOnReplace": false
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlueprintCreationToolDefinitionObjectBuilder')
search_content('', type_contains='BlueprintCreationToolDefinitionObjectBuilder')
```
