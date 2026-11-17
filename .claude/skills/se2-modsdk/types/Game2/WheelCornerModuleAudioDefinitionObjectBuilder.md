# WheelCornerModuleAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.WheelCornerModuleAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BrakingRatioParameter` | Parameter for representing the ratio of brake currently applied, in range [0, 1]. |
| `BrakingTorqueParameter` | Parameter for representing the braking torque currently applied to the wheel, in Newton-seconds. |
| `PropulsionRatioParameter` | Parameter for representing the ratio of propulsion currently applied, in range [0, 1]. |
| `PropulsionTorqueParameter` | Parameter for representing the propulsion torque currently applied to the wheel, in Newton-seconds. |
| `RotationSpeedParameter` | Parameter for representing the current wheel rotation speed represented in RPM. |
| `WheelCornerModuleAudio` | Audio event to play by the wheel corner module block. |
| `WheelRadiusParameter` | Parameter for representing radius of the wheel. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\WheelCornerModuleAudioDefinition.def`

```json
{
  "Guid": "115e137f-f41b-45d6-a8db-d0c39c706e56",
  "WheelCornerModuleAudio": "event:/SFX/Block/Wheels/Engine/WheelEngineTestMedium",
  "WheelRadiusParameter": "WheelRadius",
  "PropulsionTorqueParameter": "PropulsionTorque",
  "BrakingTorqueParameter": "BrakingTorque",
  "RotationSpeedParameter": "RotationSpeed"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WheelCornerModuleAudioDefinitionObjectBuilder')
search_content('', type_contains='WheelCornerModuleAudioDefinitionObjectBuilder')
```
