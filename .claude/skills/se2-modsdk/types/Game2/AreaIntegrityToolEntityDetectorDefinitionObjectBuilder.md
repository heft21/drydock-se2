# AreaIntegrityToolEntityDetectorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.AreaIntegrityToolEntityDetectorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DetectionFrequency` | How often (in frames) should the detection of blocks happen |
| `DetectionOvertime` | How long should detection persist even if no interaction are detected |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\IntegrityToolAreaIntegrityToolEntityDetectorDefinition.def`

```json
{
  "Guid": "17e5ccbf-a203-4705-8e38-9c1fca05855e",
  "DetectionOvertime": 0,
  "DetectionFrequency": 20
}
```

Others: `AreaWelderMk1AreaIntegrityToolEntityDetectorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('AreaIntegrityToolEntityDetectorDefinitionObjectBuilder')
search_content('', type_contains='AreaIntegrityToolEntityDetectorDefinitionObjectBuilder')
```
