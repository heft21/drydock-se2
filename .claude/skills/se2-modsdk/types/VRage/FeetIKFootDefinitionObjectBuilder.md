# FeetIKFootDefinitionObjectBuilder

`VRage:Keen.VRage.Animation.Client.IK.FeetIKFootDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.Client.IK`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoneName` | Name of the bone that corresponds to the foot that will be positioned and rotated to match the ground surface. |
| `BoneToSoleOffset` | Offset of the sole from the bone position, in foot space (forward points towards tip of the foot). |
| `FootBoneOrientation` | Orientation of the foot bone in the vector space of the foot. If identity, the "forward" vector of the foot bone in the pose should point towards the tip of the foot, and "up" vector upwards from the sole of the foot. |
| `SoleLength` | Length of the sole area of the foot. |
| `SoleWidth` | Width of the sole area of the foot. |

## A real one

`Vanilla\Assets\Characters\System\IK\IKLeftFoot.def`

```json
{
  "Guid": "fe930ba5-bf7b-4061-90d3-8679fadcf694",
  "BoneName": "Ankle_L",
  "FootBoneOrientation": {
    "Forward": "Left",
    "Up": "Backward"
  },
  "SoleWidth": 0.1,
  "SoleLength": 0.25,
  "BoneToSoleOffset": {
    "X": 0,
    "Y": -0.09,
    "Z": -0.07
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FeetIKFootDefinitionObjectBuilder')
search_content('', type_contains='FeetIKFootDefinitionObjectBuilder')
```
