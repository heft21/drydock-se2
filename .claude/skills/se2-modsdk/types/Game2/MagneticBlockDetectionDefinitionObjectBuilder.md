# MagneticBlockDetectionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.MagneticBlockDetectionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxAlignmentAngle` | The maximum angle allowed between the block and target surface for it to be accepted. (An angle of 0 require perfect alignment, an angle of 90 allow any surface detected.) |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\MagneticBlockDetectionDefinition.def`

```json
{
  "Guid": "acd74520-5e6b-4dee-8d2b-811e9d12a348",
  "MaxAlignmentAngle": 25
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MagneticBlockDetectionDefinitionObjectBuilder')
search_content('', type_contains='MagneticBlockDetectionDefinitionObjectBuilder')
```
