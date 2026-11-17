# DynamicBoneParentedPositionBaseDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.DynamicBoneParentedPositionBaseDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\EmoteProps\EmotePropBoneParent.def`

```json
{
  "Guid": "0afdaaec-2352-4ea4-b516-f0c9e0913e46",
  "RiggedAnimatorTag": "FirstPersonAwareRiggingAnimator"
}
```

Others: `RocketLaunchMagazineSubpart_DynamicBoneParentedPositionBaseDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DynamicBoneParentedPositionBaseDefinitionObjectBuilder')
search_content('', type_contains='DynamicBoneParentedPositionBaseDefinitionObjectBuilder')
```
