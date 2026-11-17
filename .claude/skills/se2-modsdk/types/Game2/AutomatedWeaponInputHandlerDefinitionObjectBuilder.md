# AutomatedWeaponInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.AutomatedWeaponInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HintsTitle` | Localization key for the control hints title. |
| `InputContextDefinitionMovement` | Definition for input context for camera inputs |
| `InputContextDefinitionMovementCharacter` | Definition for input context for camera inputs when directly controlling from a character |
| `Release` | Input for the release control action |
| `ReleaseHint` | Hint shown for action |
| `Reload` | Input for the reload action |
| `ReloadHint` | Hint shown for action |
| `Shoot` | Input for the shoot action |
| `ShootHint` | Hint shown for action |
| `YawPitchAnalog` | Analog inputs for Yaw and Pitch. They build up over time and decay over time. Example of analog input is a movement of mouse. |
| `YawPitchAnalogHint` | Hint shown for action |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\TurretInputAdapter\TurretPrefabInputAdapter_AutomatedWeaponInputHandlerDefinition.def`

```json
{
  "Guid": "9c721489-e6ab-401c-86c0-9d555e5818f3",
  "InputContextDefinitionMovement": "94978a87-94fc-429c-bf85-17ef43c2d881",
  "InputContextDefinitionMovementCharacter": "b82e277d-a767-493b-8200-a283b34be214",
  "YawPitchAnalog": "85c0bd3d-215f-456a-8480-b6f5dd99546c",
  "Shoot": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "Reload": "ef513d1b-5abf-44b3-9f41-10c354610a33",
  "Release": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "HintsTitle": "WeaponBlockToolDefaultName",
  "YawPitchAnalogHint": "CameraControls",
  "ShootHint": "GunShoot",
  "ReloadHint": "ReloadGunTool",
  "ReleaseHint": "TerminalTurretReleaseControl"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AutomatedWeaponInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='AutomatedWeaponInputHandlerDefinitionObjectBuilder')
```
