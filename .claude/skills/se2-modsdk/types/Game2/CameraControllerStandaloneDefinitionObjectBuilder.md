# CameraControllerStandaloneDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraControllerStandaloneDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AngularSpeed` | Additional modifier affecting view rotation speed, layered on top of mouse input |
| `AttachToLocalPlayer` | Attach camera to local player at a fixed distance |
| `InputContextDefinition` | Camera input context settings |
| `MouseDelta` | 2D axis input for view rotation |
| `MouseSensitivity` | Mouse sensitivity multiplier for camera rotation around target |
| `OffsetToLocalPlayer` | Offset from camera to the local player if attached |
| `UseTransformOfSpectator` | Initialize camera to match the transform of the first spector in the scene (entity with ) |

## A real one

`Vanilla\Assets\System\Camera\StandaloneDeltaCamera\CharacterStandaloneDeltaCameraControllerDefinition.def`

```json
{
  "Guid": "72b8430a-5064-4980-ab93-1bbbb18b17f0",
  "InputContextDefinition": "e3b9a7d4-1c52-4f8a-bd06-9a2f5c8e71b6",
  "FreeLookInputContextDefinition": "b7e4c2a9-3f16-4d8b-9c05-7a1e2d6f48b3",
  "UseTransformOfSpectator": false,
  "MouseDelta": "45dcca79-8b8b-461d-b72f-6967c44b2683",
  "FreeLookModifier": "b03bdab2-0082-4c38-b272-c2156ab765f2",
  "MouseSensitivity": 0.002,
  "AngularSpeed": 0.025,
  "AttachToLocalPlayer": true,
  "OffsetToLocalPlayer": {
    "X": 0,
    "Y": 0,
    "Z": 10
  }
}
```

Others: `CharacterStandaloneStaticCameraControllerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraControllerStandaloneDefinitionObjectBuilder')
search_content('', type_contains='CameraControllerStandaloneDefinitionObjectBuilder')
```
