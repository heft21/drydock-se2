# BoneAnchorTwoBoneIKModifierDefinitionObjectBuilder

`VRage:Keen.VRage.Animation.Animator.BoneAnchorTwoBoneIKModifierDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.Animator`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AnchoredBone` | Name of bone that will be transformed to stay fixed relative to the target bone. |
| `TargetBone` | Name of the bone to anchor to. |

## A real one

`Vanilla\Assets\Characters\System\IK\LeftHandToWeaponPinIKAnchor.def`

```json
{
  "Guid": "21fcc518-0e9f-453e-a065-f07d2581d652",
  "AnchoredBone": "Wrist_L",
  "TargetBone": "SE_RigR_Weapon_pin"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BoneAnchorTwoBoneIKModifierDefinitionObjectBuilder')
search_content('', type_contains='BoneAnchorTwoBoneIKModifierDefinitionObjectBuilder')
```
