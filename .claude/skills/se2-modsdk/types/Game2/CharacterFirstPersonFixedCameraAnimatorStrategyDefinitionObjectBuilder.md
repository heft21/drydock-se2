# CharacterFirstPersonFixedCameraAnimatorStrategyDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterFirstPersonFixedCameraAnimatorStrategyDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CameraFixedBoneNames` | Names of the bones that will be programatically positioned to stay fixed in camera space. |
| `FirstPersonAdapter` | Definition for first person camera adapter to obtain information about the bone the camera is attached to. |
| `FirstPersonModelOffset` | Offset for the character first person model relative to camera. If zero, the camera bone of the first person rig will match camera bone position of the third person rig. |

## A real one

`Vanilla\Assets\Characters\System\AnimatorFirstPerson.def`

```json
{
  "Guid": "2761e1e6-b1bc-467f-ba4b-4efb4838aa29",
  "AnimationPriority": 1,
  "FirstPersonAdapter": "61ab743f-29cc-4790-a7b4-2cb34c979db2",
  "CameraFixedBoneNames": [
    {
      "Key": "896d9add-9379-495e-b090-aa628c4e1e2c",
      "Value": "Shoulder_L"
    },
    {
      "Key": "78a4e2dc-bcb0-4e7a-8014-64b0042cc002",
      "Value": "Shoulder_R"
    }
  ],
  "FirstPersonModelOffset": {
    "X": 0,
    "Y": 0,
    "Z": -0.1
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterFirstPersonFixedCameraAnimatorStrategyDefinitionObjectBuilder')
search_content('', type_contains='CharacterFirstPersonFixedCameraAnimatorStrategyDefinitionObjectBuilder')
```
