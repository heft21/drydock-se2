# ReplayToolInputConfigurationObjectBuilder

`Game2:Keen.Game2.Client.Debugging.Screens.ReplayTool.ReplayToolInputConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.Debugging.Screens.ReplayTool`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EndRecording` | Start the recording in the current scene. |
| `InputContextDefinition` | Input context settings. |
| `SpawnCharacter` | Input action for spawning a new character. |
| `StartRecording` | Start the recording in the current scene. |

## A real one

`Vanilla\Assets\System\Configurations\ReplayToolInputConfiguration.def`

```json
{
  "Guid": "57128a52-84ab-457b-ae8f-be8a9104d02f",
  "InputContextDefinition": "32d29ffc-87b3-4cd8-86b4-26c714e35964",
  "SpawnCharacter": "265efe5f-c0af-4703-aa5f-1fefcdf59f6e",
  "StartRecording": "f7eb9c90-71e1-472b-a1ff-2c88bf5a1efa",
  "EndRecording": "177600c8-e320-47ce-94d9-d942278275c8"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ReplayToolInputConfigurationObjectBuilder')
search_content('', type_contains='ReplayToolInputConfigurationObjectBuilder')
```
