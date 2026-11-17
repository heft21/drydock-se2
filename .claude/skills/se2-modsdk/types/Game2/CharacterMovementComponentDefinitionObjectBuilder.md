# CharacterMovementComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterMovementComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlignmentSpeed` | Character up-vector alignment speed, in degrees per second (e.g. when aligning with ground surface) |
| `CrouchSpeedMultiplier` | Speed multiplier applied to character movement when crouched. 0.5 means half the speed. |
| `GroundedGravityType` | AffectedByGravityDefinition to use while grounded/walking |
| `JetpackGravityType` | AffectedByGravityDefinition to use while flying with jetpack |
| `JogSpeedMultiplier` | Speed multiplier applied to character movement when not sprinting. |
| `LayersToIgnoreWhenProbingGround` | Entity Layers to ignore when checking the ground for character alignment. |
| `MagneticBootsAlignmentSpeed` | Same as while the character is wearing magnetic boots |
| `MaxRelativeDistance` | Maximum distance from target within which the character relative speed dampeners will apply |
| `SupportAngle` | Threshold angle between the character's down vector and current gravity direction beyond which the character is no longer considered supported by the ground and will start floating. |

## A real one

`Vanilla\Assets\Characters\System\CharacterMovement.def`

```json
{
  "Guid": "eddb2647-ddb7-447f-92c3-502f37141260",
  "AlignmentSpeed": 90,
  "SupportAngle": 0.541,
  "MagneticBootsAlignmentSpeed": 90,
  "LayersToIgnoreWhenProbingGround": [
    {
      "Key": "91576921-a178-4171-8232-7b3e3fa1604c",
      "Value": "Characters"
    },
    {
      "Key": "da6de4fd-0d33-496b-a09a-2e9c235fe0c2",
      "Value": "FloatingObjects"
    }
  ],
  "MaxRelativeDistance": 100,
  "GroundedGravityType": "6290b4c6-99f6-42dd-9425-bcd72170e6bc",
  "JetpackGravityType": "ae2c2b8f-f331-4cbe-98f9-7905cf001dc5",
  "CrouchSpeedMultiplier": 0.2,
  "JogSpeedMultiplier": 0.6
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterMovementComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterMovementComponentDefinitionObjectBuilder')
```
