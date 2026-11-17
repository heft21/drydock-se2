# MechanicalBlockMatchingCounterpartDetectionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.MechanicalBlockMatchingCounterpartDetectionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DetectContinuously` | If true, will look for counterparts continuously, as long as the block is functional, enabled, and not connected, sending signals when the detected counterpart changes. If false, will only look for counterparts, when requested via , and not send any signals. |
| `DetectionArgs` | Settings for detection of counterparts, used with . |
| `DetectionLimits` | The limits that need to be satisfied for a counterpart to be detected. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\MechanicalBlockMatchingCounterpartDetectionDefinition.def`

```json
{
  "Guid": "1b730642-0b65-4d8b-935b-8b09dbe9d19d",
  "DetectionLimits": {
    "MaxDistance": 3,
    "MaxForwardAngle": 45,
    "MaxUpAngle": null,
    "DetectOppositeFacing": true,
    "MustFaceEachOther": true,
    "MaxFacingEachOtherPenetration": 0.25
  },
  "DetectContinuously": true,
  "DetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": false,
    "DetectTopMostEntities": true,
    "Frequency": 3,
    "Occlusion": false,
    "AllowDuplication": false,
    "DummyOcclusionEpsilon": 0
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MechanicalBlockMatchingCounterpartDetectionDefinitionObjectBuilder')
search_content('', type_contains='MechanicalBlockMatchingCounterpartDetectionDefinitionObjectBuilder')
```
