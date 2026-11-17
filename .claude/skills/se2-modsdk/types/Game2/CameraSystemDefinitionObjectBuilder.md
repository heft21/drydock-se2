# CameraSystemDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraSystemDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CompositionToCameraPrefabs` | Central place for specifying which entity compositions can be observed by which camera modes. |
| `CompositionToNamedCameraPrefabs` | Specify the named camera modes supported by a specific entity compositions |
| `InputContextDefinition` | Camera system input context |
| `SwitchCameraShoulder` | Input to switch the camera horizontal position (shoulder) in 3rd person camera |
| `ToggleCamera` | Input action to switch to the next camera mode |

## A real one

`Vanilla\Assets\System\Controller\CameraSystem.def`

Too large to inline. Fields present:

`CompositionToCameraPrefabs`, `CompositionToNamedCameraPrefabs`, `Guid`, `InputContextDefinition`, `SwitchCameraShoulder`, `ToggleCamera`

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraSystemDefinitionObjectBuilder')
search_content('', type_contains='CameraSystemDefinitionObjectBuilder')
```
