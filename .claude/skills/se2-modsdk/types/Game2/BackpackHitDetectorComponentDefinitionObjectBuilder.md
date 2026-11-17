# BackpackHitDetectorComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.Effects.BackpackHitDetectorComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character.Effects`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\PrefabCharacterClient_BackpackHitDetectorComponentDefinition.def`

```json
{
  "Guid": "0efb19ca-77af-48fc-84f4-97e0a6a9f2a0",
  "BoneName": "BackPack_M",
  "RiggedAnimatorTag": "DefaultRiggedAnimator",
  "VolumeDummyType": "43b64b49-45cd-460c-9a56-99a4b9f89af2",
  "RayBacktrack": 0.2,
  "MaxPenetration": 0.2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BackpackHitDetectorComponentDefinitionObjectBuilder')
search_content('', type_contains='BackpackHitDetectorComponentDefinitionObjectBuilder')
```
