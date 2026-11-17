# LcdMultiPanelDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Lcd.LcdMultiPanelDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Lcd`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultFont` | Default font for all surfaces on this block type. |
| `MaxRenderDistance` | Maximum distance from the camera at which this block type's LCD surfaces are eligible for an offscreen render target. Beyond this range the block participates in admission only as an out of range candidate and shows the default screen material. |
| `PowerOffMaterial` | Material used when block is powered off. |
| `Surfaces` | Per-surface configuration for this block type. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\LcdMultiPanelDefinition.def`

```json
{
  "Guid": "57977bda-206b-4eb7-942b-6f4006ce8d81",
  "DefaultFont": "{G}984b5200-190a-456a-bcf0-5c1c7afe0028",
  "PowerOffMaterial": "73b146d6-2a17-405c-ac00-dd7ddb4454d6",
  "MaxRenderDistance": 120,
  "Surfaces": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LcdMultiPanelDefinitionObjectBuilder')
search_content('', type_contains='LcdMultiPanelDefinitionObjectBuilder')
```
