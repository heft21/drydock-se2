# CharacterHeadAnimatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.CharacterHeadAnimatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HeadBoneName` | Name of a bone representing characters head. Rotation of this bone will be replaced with computed rotation. |
| `HeadInterpolation` | Interpolation factor for how quickly the head transitions from one rotation to another |
| `HeadRotation` | Additional rotation applied to head after new orientation is computed to correct for non-standard bone orientation for head or any following bones. |
| `HeadYawLimit` | Maximum angle deviation for the head Yaw rotation |
| `NeckBoneName` | Name of a bone representing characters neck. Bone immediately before Head bone. |
| `NeckRotation` | Additional rotation that is applied on top of the Neck bone rotation to correct for non-standard bone orientation of neck ( standard is -Z forward, Y up). Yaw rotation is applied around Y axis and with non-standard bone orientation they need to be corrected. |

## A real one

`Vanilla\Assets\Characters\System\CharacterHeadAnimatorDefinition.def`

```json
{
  "Guid": "b27be809-40d8-4211-8079-b45ae8edb197",
  "HeadYawLimit": 1.25,
  "NeckBoneName": "Neck_M",
  "HeadBoneName": "Head1_M",
  "NeckRotation": {
    "X": 0,
    "Y": 0,
    "Z": 0,
    "W": 1
  },
  "HeadRotation": {
    "X": -0.5416752,
    "Y": -0.45451948,
    "Z": 0.5416752,
    "W": 0.45451948
  },
  "HeadInterpolation": 0.2,
  "NeckEulerHint": {
    "X": 0,
    "Y": 0,
    "Z": 0
  },
  "HeadEulerHint": {
    "X": 0,
    "Y": -90,
    "Z": 100
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterHeadAnimatorDefinitionObjectBuilder')
search_content('', type_contains='CharacterHeadAnimatorDefinitionObjectBuilder')
```
