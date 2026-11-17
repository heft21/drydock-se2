# SolarGeneratorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.SolarGeneratorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DummyType` | Type of the dummies that will be used to detect the sun from. Orientation of the dummies matter; the forward vector of the dummy should be facing away from the surface. |
| `EfficiencyMultiplier` | Multiplier that affects the efficiency of the solar panel. For single-sided solar panels, put at 1. For double-sided solar panels, put to 2, so that when only 1 side of the panel is lit, the full is given. Even with a higher multiplier, the output can't exceed |
| `LargeObjectsOcclusionDetection` | Similar to , but the raycast considers only very large objects (planets). If 0, large objects occlusion detection is disabled. Higher values do not imply higher performance hit for this detection type. |
| `MaxOutput` | Maximum amount of the resource that can be produced |
| `OcclusionDetection` | Length of the raycast from each dummy to the sun to see if the block is in shadow. If all zero, occlusion detection is disabled. |
| `ProductionPriority` | Priority of this block in the resource distribution system. |
| `ResourceType` | Type of resource that is produced |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\SolarGeneratorDefinition.def`

```json
{
  "Guid": "6f033597-2b60-41a9-9fa0-21d4f5a75e67",
  "ResourceType": "bcded093-f5c0-4997-af3a-a6fbd853ad66",
  "ProductionPriority": {
    "Priority": 10
  },
  "MaxOutput": 1000,
  "DummyType": "748f5403-3e17-40e2-9d8d-7dadbd23a0c1",
  "OcclusionDetection": {
    "HighPrecision": 500,
    "MediumPrecision": 1500,
    "LowPrecision": 3000
  },
  "LargeObjectsOcclusionDetection": 1500000,
  "EfficiencyMultiplier": 2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SolarGeneratorDefinitionObjectBuilder')
search_content('', type_contains='SolarGeneratorDefinitionObjectBuilder')
```
