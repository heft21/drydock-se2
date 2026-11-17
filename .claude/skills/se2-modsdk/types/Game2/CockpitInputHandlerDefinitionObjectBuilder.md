# CockpitInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.CockpitInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActionSecondary` | Input for Secondary action that activates secondary action of all eligible blocks (alternative fire, drilling) TODO SE2-30203 remove |
| `AngularInput` | Settings for the angular velocity-based rotation input system. Defaults recovered from the last angular-era .def (Dev1 #8, June 2024). |
| `InputContextDefinitionMovement` | Definition for input context for all movement inputs (WSAD, roll, rotation) |
| `InputContextDefinitionUtility` | Definition for input context for all utility inputs (terminal screen, inventory, dampeners, etc) |
| `Interact` | Interaction (exit cockpit) input |
| `LookDown` | Look down. Variant of for keys. Instant, decays instantly |
| `LookLeft` | Look left. Variant of for keys. Instant, decays instantly |
| `LookRight` | Look right. Variant of for keys. Instant, decays instantly |
| `LookUp` | Look up. Variant of for keys. Instant, decays instantly |
| `MoveBack` | Move back input |
| `MoveDown` | Move down input |
| `MoveForward` | Move forward input |
| `MoveLeft` | Strafe left input |
| `MoveRight` | Strafe right input |
| `MoveUp` | Move up input |
| `ParkingTooltipDelay` | Delay between parking becoming possible and showing the parking tooltip. |
| `ParkingTooltipIcon` | Icon to display on the parking tooltip notification |
| `ParkingTooltipText` | Text of parking tooltip, informing player they can park their ship. |
| `RollLeft` | Roll left input |
| `RollRight` | Roll right input |
| `TargetInput` | Settings for the target/reticle-based rotation input system. Defaults match the current live .def values. |
| `ToggleDampeners` | Toggle dampeners input |
| `ToggleLights` | Toggle reflector lights on/off |
| `ToggleParkingBrakes` | Switch all magnetic and connector blocks that are available for parking. |
| `TogglePower` | Turn grid on/off. |
| `YawPitchAnalog` | Analog inputs for Yaw and Pitch. They build up over time and decay over time. Example of analog input is a movement of mouse. |
| `YawPitchDigital` | Digital inputs for Yaw and Pitch. They are instant and decay instantly Example of digital input are arrow keys. TODO SE2-31593 remove |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CockpitInputAdapter\CockpitInputAdapter.def`

```json
{
  "Guid": "8a6853f0-e096-4909-9ac7-c1fa807153eb",
  "InputContextDefinitionUtility": "bbe6a2d5-0bb8-43c1-9e11-4c7cee91ad44",
  "InputContextDefinitionMovement": "f5611a9f-ac5e-4719-bb34-e2662450c0e8",
  "Interact": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "ToggleDampeners": "a4dc7bbc-43e9-4d3a-9ee2-85afa3816983",
  "MoveForward": "70e8a38b-ee2b-4fc1-8edf-6da0e27607e0",
  "MoveBack": "5670039f-ea4c-431e-8311-6131a6d36ad7",
  "MoveLeft": "d040c535-4952-4a8c-a993-fc5e0fc4e990",
  "MoveRight": "d4529b0d-bb1e-4d0b-a61c-72d21a1e216c",
  "MoveUp": "fc7128fe-2609-4e1d-b501-e8c5051777d1",
  "MoveDown": "5e4ea1d9-1ccb-4227-8a76-f54f384c2295",
  "RollLeft": "06e925c6-e7e3-4bc5-a03c-ca19fcf898c3",
  "RollRight": "d849517e-1b28-4e40-bc04-f6c72661e67c",
  "YawPitchAnalog": "85c0bd3d-215f-456a-8480-b6f5dd99546c",
  "LookLeft": "9c78f323-ff0e-48ba-8e8c-b541d9094f42",
  "LookRight": "2326e7e3-eafc-4072-b99b-c1749c278dea",
  "LookUp": "f8517b34-838c-45bb-b3ee-4631b7ddcba4",
  "LookDown": "6b9d6675-0c44-47a6-9c44-2fbe8e52397d",
  "YawPitchDigital": "48673d6a-7d82-4f4e-9c96-9e64ab1c1d68",
  "ToggleLights": "400f4dee-cb80-46cf-80b3-c7343dc84b9a",
  "ToggleParkingBrakes": "4033d70e-1467-4c4b-85f4-40ab2ead1017",
  "TogglePower": "213e6a8c-d159-4b25-a9fd-ae727ecde77f",
  "Boost": "314f02e6-f6d4-4cc5-9497-4e175b3d2f50",
  "DoubleTapTime": 2500000,
  "Target": "4cd393a8-047a-427e-a9c2-51e2b723bbef",
  "ParkingTooltipDelay": 10000000,
  "ParkingTooltipText": "ParkingTooltip",
  "ParkingTooltipIcon": "{G}edb96123-5827-4aa7-ba4a-b9e60e5c52ac",
  "HintsTitle": "ControlCategoryName",
  "TogglePowerOnHint": "ToggleShipPowerOn",
  "TogglePowerOffHint": "ToggleShipPowerOff",
  "ToggleLightsOnHint": "ToggleShipLightsOn",
  "ToggleLightsOffHint": "ToggleShipLightsOff",
  "ToggleDampenersOnHint": "ToggleDampenersOn",
  "ToggleDampenersOffHint": "ToggleDampenersOff",
  "ExitCockpitHint": "ExitCockpit",
  "TargetGridHint": "TargetGrid",
  "BoostHint": "BoostShip",
  "AngularInput": {
    "AnalogCoefficient": 0.0002,
    "DigitalCoefficient": 0.0063,
    "InputExponentialParameter": 2.5,
    "ReturnMultiplier": 2.5,
    "DecayLinear": 0.02,
    "DecayExponential": 0.985,
    "DeadzoneSize": 0.01,
    "UIScale": 0.4,
    "DecayDelayTime": 1500000,
    "DecayRampUpTime": 1000000,
    "DecayMinimum": 0.5
  },
  "TargetInput": {
    "AnalogCoefficient": 0.0015,
    "DigitalCoefficient": 0.015,
    "RollingDigitalCoefficient": 0.1,
    "RollMassFactor": 1.5,
    "RollLimiter": 0,
    "RollDecayPower": 3,
    "RollRampUpPower": 2,
    "UIScale": 0.4,
    "ReticleSize": 0.01,
    "DeadzoneSize": 1e-05,
    "DecayDelayTime": 12500000,
    "DecayRampUpTime": 32500000,
    "DecayMinimum": 0.15
  }
}
```

Others: `CryopodInputHandler`

---

Read it with the MCP server rather than by hand:

```
describe_type('CockpitInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='CockpitInputHandlerDefinitionObjectBuilder')
```
