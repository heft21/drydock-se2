# FirstPersonCameraWithInputDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Modes.FirstPersonCameraWithInputDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Modes`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AngularSpeed` | Additional view rotation speed multiplier on top of mouse look input |
| `ClampAngles` | Should camera clamp view angles - for example, first person view in cockpit should not allow full rotation |
| `InputContextDefinition` | Input context settings |
| `MaxX` | Maximum horizontal angle that the camera can rotate. |
| `MaxY` | Maximum vertical angle that the camera can rotate. |
| `MinX` | Minimum horizontal angle that the camera can rotate. |
| `MinY` | Minimum vertical angle that the camera can rotate. |
| `MouseDelta` | Mouse look / view direction input |
| `MouseSensitivity` | Mouse look sentitivity multiplier |
| `ResetFreeLook` | Input to recenter view |
| `ResetFreeLookThreshold` | Threshold time for the double-tap of Alt to reset the view |

## A real one

`Vanilla\Assets\System\Camera\CockpitFirstPersonCamera\FirstPersonCameraWithInput.def`

```json
{
  "Guid": "bf2a7b08-a490-4bb4-89d3-4c1c14829f8d",
  "RotationSpringStiffnessLag": 1,
  "LookOffsetResetSpringStiffnessLag": 0.33,
  "ClampAngles": true,
  "MaxX": 90,
  "MinX": -90,
  "MaxY": 80,
  "MinY": -90,
  "MouseSensitivity": 0.002,
  "AngularSpeed": 1,
  "InputContextDefinition": "b95a7fea-66ae-4c2a-b1ce-897408a15ef7",
  "FreeLookInputContextDefinition": "b7e4c2a9-3f16-4d8b-9c05-7a1e2d6f48b3",
  "MouseDelta": "45dcca79-8b8b-461d-b72f-6967c44b2683",
  "ResetFreeLook": "b03bdab2-0082-4c38-b272-c2156ab765f2",
  "ResetFreeLookThreshold": 5000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FirstPersonCameraWithInputDefinitionObjectBuilder')
search_content('', type_contains='FirstPersonCameraWithInputDefinitionObjectBuilder')
```
