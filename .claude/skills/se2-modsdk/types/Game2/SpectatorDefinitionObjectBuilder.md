# SpectatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Spectators.SpectatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Spectators`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumedInputKinds` | InputKinds consumed by |
| `DefaultSpectatorLinearSpeed` | Baseline spectator movement speed |
| `DefaultSpeedMultiplier` | Default movement speed boost multiplier |
| `InputContextDefinitionMovement` | Free spectator move input context |
| `InputContextDefinitionUtility` | Utility input context (placeholder / not used yet) |
| `IsMouseInverted` | Invert mouse input? |
| `KeyLookSensitivity` | Sensitivity multiplier for /// |
| `LinearSpeedChange` | Input to adjust movement speed |
| `LookDown` | Look down. Variant of for keys |
| `LookLeft` | Look left. Variant of for keys |
| `LookRight` | Look right. Variant of for keys |
| `LookUp` | Look up. Variant of for keys |
| `MaxSpectatorLinearSpeed` | Maximum spectator movement speed |
| `MinSpectatorLinearSpeed` | Minimum spectator movement speed |
| `MouseLook` | Mouse look input (2D axis) |
| `MouseSensitivity` | Mouse look sensitivity while in spectator mode |
| `MoveBackward` | Move backward input |
| `MoveDown` | Move down input |
| `MoveForward` | Move forward input |
| `MoveLeft` | Move left input |
| `MoveRight` | Move right input |
| `MoveUp` | Move up input |
| `PassedInputKinds` | InputKinds passed by to next controllers in the stack |
| `RollLeft` | Roll left input |
| `RollRight` | Roll right input |
| `SpectatorRollSpeed` | Spectator roll speed |
| `SpeedBoost` | Toggle for spectator movement speed boost |
| `ToggleGridFollowing` | Input for toggling follow grid mode |
| `ToggleHeadLights` | Input for toggling spectator headlights |
| `ToolbarInputKind` | For the toolbar to show, this input kind must be active |

## A real one

`Vanilla\Assets\System\Spectator\Spectator.def`

```json
{
  "Guid": "626b9cc2-3622-47b4-acfc-f7662da87e3d",
  "ConsumedInputKinds": [
    "Movement",
    "Rotation",
    "Interaction",
    "Tools",
    "Utility",
    "Toolbar"
  ],
  "PassedInputKinds": [],
  "MouseSensitivity": 0.002,
  "DefaultSpeedMultiplier": 2.8571,
  "DefaultSpectatorLinearSpeed": 2.1,
  "MinSpectatorLinearSpeed": 0.0001,
  "MaxSpectatorLinearSpeed": 100000,
  "SpectatorRollSpeed": 2,
  "IsMouseInverted": false,
  "InputContextDefinitionMovement": "8cd79fd8-8af1-4cd4-a6bc-a460c8f7e0fc",
  "InputContextDefinitionUtility": "e255eb8e-6419-4f58-9a5e-1a857957f6df",
  "MoveForward": "70e8a38b-ee2b-4fc1-8edf-6da0e27607e0",
  "MoveBackward": "5670039f-ea4c-431e-8311-6131a6d36ad7",
  "MoveLeft": "d040c535-4952-4a8c-a993-fc5e0fc4e990",
  "MoveRight": "d4529b0d-bb1e-4d0b-a61c-72d21a1e216c",
  "MoveUp": "fc7128fe-2609-4e1d-b501-e8c5051777d1",
  "MoveDown": "5e4ea1d9-1ccb-4227-8a76-f54f384c2295",
  "SpeedBoost": "314f02e6-f6d4-4cc5-9497-4e175b3d2f50",
  "RollLeft": "06e925c6-e7e3-4bc5-a03c-ca19fcf898c3",
  "RollRight": "d849517e-1b28-4e40-bc04-f6c72661e67c",
  "LookLeft": "9c78f323-ff0e-48ba-8e8c-b541d9094f42",
  "LookRight": "2326e7e3-eafc-4072-b99b-c1749c278dea",
  "LookUp": "f8517b34-838c-45bb-b3ee-4631b7ddcba4",
  "LookDown": "6b9d6675-0c44-47a6-9c44-2fbe8e52397d",
  "MouseLook": "e886f672-5656-4d23-a4ba-77a14bb702be",
  "KeyLookSensitivity": 20,
  "LinearSpeedChange": "247b11d0-741a-4fd6-ad61-cb8684047def",
  "ToggleGridFollowing": "9ad853aa-2db8-4582-8058-5c73605f555a",
  "ToggleHeadLights": "35eee78d-5fa0-4f15-b3f6-8b25a4db01f9",
  "ToolbarInputKind": "Movement"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SpectatorDefinitionObjectBuilder')
search_content('', type_contains='SpectatorDefinitionObjectBuilder')
```
