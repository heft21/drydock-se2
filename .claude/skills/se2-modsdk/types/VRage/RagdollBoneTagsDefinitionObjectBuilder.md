# RagdollBoneTagsDefinitionObjectBuilder

`VRage:Keen.VRage.Physics.Definitions.RagdollBoneTagsDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Bones` | Maps each ragdoll bone to a specific tag. |

## A real one

`Vanilla\Assets\Characters\System\RagdollBoneTagsDefinition.def`

```json
{
  "Guid": "98ef7258-5e90-460c-b7e0-e791cb099f08",
  "Bones": [
    {
      "$Key": "Ragdoll_Shoulder_R001",
      "$Value": "RightArm"
    },
    {
      "$Key": "Ragdoll_Wrist_L001",
      "$Value": "LeftArm"
    },
    {
      "$Key": "Ragdoll_Elbow_L001",
      "$Value": "LeftArm"
    },
    {
      "$Key": "Ragdoll_Shoulder_L001",
      "$Value": "LeftArm"
    },
    {
      "$Key": "Ragdoll_Elbow_R001",
      "$Value": "RightArm"
    },
    {
      "$Key": "Ragdoll_Wrist_R001",
      "$Value": "RightArm"
    },
    {
      "$Key": "Ragdoll_Hip_L001",
      "$Value": "Leg"
    },
    {
      "$Key": "Ragdoll_Knee_L001",
      "$Value": "Leg"
    },
    {
      "$Key": "Ragdoll_Foot_L001",
      "$Value": "Leg"
    },
    {
      "$Key": "Ragdoll_Hip_R001",
      "$Value": "Leg"
    },
    {
      "$Key": "Ragdoll_Knee_R001",
      "$Value": "Leg"
    },
    {
      "$Key": "Ragdoll_Foot_R001",
      "$Value": "Leg"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RagdollBoneTagsDefinitionObjectBuilder')
search_content('', type_contains='RagdollBoneTagsDefinitionObjectBuilder')
```
