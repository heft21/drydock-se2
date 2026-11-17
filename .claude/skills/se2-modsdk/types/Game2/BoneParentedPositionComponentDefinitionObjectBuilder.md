# BoneParentedPositionComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.BoneParentedPositionComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoneName` | Name of the bone to bind to |
| `Offset` | Optional offset that will be applied from the bone position. |

## A real one

`Vanilla\Assets\Characters\System\ToolPositionComponent.def`

```json
{
  "Guid": "f97dacda-1c27-45c3-a3d8-13a41c0abf5d",
  "RiggedAnimatorTag": "FirstPersonAwareRiggingAnimator",
  "BoneName": "SE_RigR_Weapon_pin",
  "Offset": {
    "X": 0,
    "Y": 0,
    "Z": 0
  }
}
```

Others: `ToolFake_BoneParenting`, `CharacterBoneParentedPositionComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BoneParentedPositionComponentDefinitionObjectBuilder')
search_content('', type_contains='BoneParentedPositionComponentDefinitionObjectBuilder')
```
