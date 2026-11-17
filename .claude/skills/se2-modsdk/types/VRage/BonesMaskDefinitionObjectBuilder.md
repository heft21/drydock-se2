# BonesMaskDefinitionObjectBuilder

`VRage:Keen.VRage.Animation.Data.BonesMaskDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.Data`
- definitions using it: **33**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Bones` | Weights for bones in the mask. Only bones present in this dictionary will be affected by the mask with the given weight. |

## A real one

`Vanilla\Assets\Characters\Shared\AnimationControllers\1PMask.def`

```json
{
  "Guid": "a6aac254-48de-42e8-ac4b-eecfbb128e24",
  "Bones": [
    {
      "$Key": {
        "Name": "CameraBoneParent"
      },
      "$Value": 1
    },
    {
      "$Key": {
        "Name": "Root_M"
      },
      "$Value": 1
    },
    {
      "$Key": {
        "Name": "Scapula_R"
      },
      "$Value": 0
    },
    {
      "$Key": {
        "Name": "Scapula_L"
      },
      "$Value": 0
    }
  ]
}
```

Others: `3PMask`, `DrillMask`

---

Read it with the MCP server rather than by hand:

```
describe_type('BonesMaskDefinitionObjectBuilder')
search_content('', type_contains='BonesMaskDefinitionObjectBuilder')
```
