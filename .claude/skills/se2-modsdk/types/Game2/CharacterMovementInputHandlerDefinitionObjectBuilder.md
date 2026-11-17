# CharacterMovementInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterMovementInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoostMode` | Input for starting/stopping the boost mode |
| `InputContextDefinitionMovement` | Context for inputs affecting character position (WSAD, jump, sprint...) |
| `InputContextDefinitionRotation` | Context for inputs affecting character rotation (mouse look, left/right roll) |
| `InputContextDefinitionUtility` | Context for other utility inputs (jetpack, magnetic boots, dampeners...) |
| `Jetpack` | Input for toggling jetpack |
| `Jump` | Input for jumping |
| `KeyLookSensitivity` | Sensitivity multiplier for /// |
| `KeyboardRollControlInputValueCoefficient` | Roll speed sensitivity |
| `LookDown` | Look down. Variant of for keys |
| `LookLeft` | Look left. Variant of for keys |
| `LookRight` | Look right. Variant of for keys |
| `LookUp` | Look up. Variant of for keys |
| `MouseControlInputValueCoefficient` | Mouse look sensitivity |
| `MouseLook` | Input for character view direction |
| `MoveBackward` | Input for moving backward |
| `MoveDown` | Input for moving down (along character's negative Y axis) |
| `MoveForward` | Input for moving forward |
| `MoveLeft` | Input for strafing left |
| `MoveRight` | Input for strafing right |
| `MoveUp` | Input for moving up (along character's positive Y axis) |
| `RollLeft` | Input for rolling character to its left |
| `RollRight` | Input for rolling character to its right |
| `SpeedBoost` | Input for toggling sprint |
| `ToggleCrouch` | Input for toggling crouching state |
| `ToggleDampeners` | Input for toggling global dampeners Will automatically slow down character movement toward zero speed when enabled |
| `ToggleRelativeDampeners` | Input for toggling relative dampeners Will dampen character's motion to match the target entity's speed |
| `ToggleWalk` | Input for toggling walking at reduced speed |
| `WalkMovementMultiplier` | Movement input multiplier when walking mode is enabled using input. 0.8 means character walks at 80% of jog speed. |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\CharacterMovementInputAdapter.def`

```json
{
  "Guid": "4b745c75-775c-4831-9cb5-90d4dbb2f681",
  "MouseControlInputValueCoefficient": 0.002,
  "WalkMovementMultiplier": 0.5,
  "KeyboardRollControlInputValueCoefficient": 0.025,
  "InputContextDefinitionMovement": "dc97504a-86e9-4ad3-9460-b218e6d81fa4",
  "InputContextDefinitionRotation": "bc592b1a-d28c-4951-905c-d4594746f86b",
  "InputContextDefinitionUtility": "37efb236-1e1f-4286-beda-16a1781ac460",
  "MoveForward": "70e8a38b-ee2b-4fc1-8edf-6da0e27607e0",
  "MoveBackward": "5670039f-ea4c-431e-8311-6131a6d36ad7",
  "MoveLeft": "d040c535-4952-4a8c-a993-fc5e0fc4e990",
  "MoveRight": "d4529b0d-bb1e-4d0b-a61c-72d21a1e216c",
  "MoveUp": "fc7128fe-2609-4e1d-b501-e8c5051777d1",
  "MoveDown": "5e4ea1d9-1ccb-4227-8a76-f54f384c2295",
  "SpeedBoost": "314f02e6-f6d4-4cc5-9497-4e175b3d2f50",
  "BoostMode": "f4893db3-3a7c-415a-8b69-6aee4283515a",
  "Jump": "383e31b2-7c33-45bb-8e6d-60505e3b1602",
  "ToggleCrouch": "d5ad431e-2d93-4570-937e-6388e2b42387",
  "ToggleWalk": "fae64a79-865f-4571-8b64-92c95af840d3",
  "RollLeft": "06e925c6-e7e3-4bc5-a03c-ca19fcf898c3",
  "RollRight": "d849517e-1b28-4e40-bc04-f6c72661e67c",
  "Jetpack": "b2af6de8-b7da-4367-a1ef-c1226acf04ee",
  "ToggleDampeners": "a4dc7bbc-43e9-4d3a-9ee2-85afa3816983",
  "ToggleRelativeDampeners": "4d7c3de2-d380-4b0e-9cf6-60943b4f78bc",
  "LookLeft": "9c78f323-ff0e-48ba-8e8c-b541d9094f42",
  "LookRight": "2326e7e3-eafc-4072-b99b-c1749c278dea",
  "LookUp": "f8517b34-838c-45bb-b3ee-4631b7ddcba4",
  "LookDown": "6b9d6675-0c44-47a6-9c44-2fbe8e52397d",
  "MouseLook": "e886f672-5656-4d23-a4ba-77a14bb702be",
  "KeyLookSensitivity": 20
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterMovementInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='CharacterMovementInputHandlerDefinitionObjectBuilder')
```
