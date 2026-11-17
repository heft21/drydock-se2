# AutoTargetingDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Weapons.AutoTargetingDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Weapons`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlignmentPrecisionThreshold` | Alignment angle precision threshold for the block to start shooting a target |
| `AzimuthRotationOffset` | Applied to the final azimuth angle as an offset to have correct targeting orientation |
| `AzimuthSpeed` | How fast the block rotates around itself |
| `DirectControlAzimuthSpeed` | How fast the block rotates around itself |
| `DirectControlElevationSpeed` | How fast the block rotates up and down |
| `DirectControlSensitivityReduction` | Divides yaw and pitch received from input by this value. This allows for smoother movement during direct control. |
| `ElevationSpeed` | How fast the block rotates up and down |
| `HighestPriorityTargetType` | If the current target is priority but not of this type and a new potential target of this type is detected, it overrides the current target |
| `IdleAngleChangeTime` | Time to randomly change the angle of the block when it does not have a target |
| `IdleSpeedReduction` | How much to reduce and when the block is idling |
| `IdleTargetCheckDelay` | Delay between target checks using when idle |
| `MaxElevation` | How far up elevation can be set |
| `MaxEngagementRange` | How far away the block can engage targets |
| `MinElevation` | How far down elevation can be set |
| `ShootDelayOnTargetAlign` | Delay before first shot when the block is aligned with the target |
| `TargetCheckDelay` | Delay between target checks using and |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\RocketTurret_AutoTargetingDefinition.def`

```json
{
  "Guid": "c66034b0-8646-436d-aaa6-66e957551e3d",
  "AzimuthSpeed": 120,
  "ElevationSpeed": 120,
  "MinElevation": -40,
  "MaxElevation": 90,
  "MaxEngagementRange": 800,
  "ShootDelayOnTargetAlign": 4999999,
  "AlignmentPrecisionThreshold": 1,
  "IdleAngleChangeTime": 100000000,
  "IdleSpeedReduction": 4,
  "AzimuthRotationOffset": 180,
  "TargetCheckDelay": 1000000,
  "IdleTargetCheckDelay": 20000000,
  "HighestPriorityTargetType": "81303ba7-fefc-4bf4-be5c-fe1222a4a9c2",
  "DirectControlAzimuthSpeed": 120,
  "DirectControlElevationSpeed": 120,
  "DirectControlSensitivityReduction": 25,
  "TargetableCategories": [
    {
      "Key": "52890660-e7fe-40b9-b742-393fa7869258",
      "Value": "c0dd8c33-60bf-451c-9917-9ada62cac06b"
    },
    {
      "Key": "ff2e6fa0-29d6-4e5e-9224-4f50b855601e",
      "Value": "6ac1deec-f4ba-44e3-ad6b-fb0edfcb5666"
    },
    {
      "Key": "55182903-fdd1-49b8-8672-f24ceb0260ab",
      "Value": "d32591d2-b476-48cb-95a2-2d2ce088f1bc"
    },
    {
      "Key": "e3d73be5-03c2-44f9-88ab-e71e9fa6e653",
      "Value": "0ba7f1f9-8565-41b8-b8c4-205c3174c3ad"
    },
    {
      "Key": "351d33d3-1beb-4b63-bf87-45fc2e087683",
      "Value": "b544c2c1-2a3b-41fb-85eb-ac95b38df8a2"
    },
    {
      "Key": "2cb01251-4d56-438c-9323-00cbfe87d77a",
      "Value": "e125712d-f0a9-4de9-839f-41c0075a1c2c"
    }
  ]
}
```

Others: `GatlingTurret_AutoTargetingDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('AutoTargetingDefinitionObjectBuilder')
search_content('', type_contains='AutoTargetingDefinitionObjectBuilder')
```
