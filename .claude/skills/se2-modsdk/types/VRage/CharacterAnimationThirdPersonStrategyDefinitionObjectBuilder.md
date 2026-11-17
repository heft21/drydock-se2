# CharacterAnimationThirdPersonStrategyDefinitionObjectBuilder

`VRage:Keen.VRage.Animation.GameObjects.CharacterAnimationThirdPersonStrategyDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.GameObjects`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\AnimationsThirdPerson.def`

```json
{
  "Guid": "a209dc77-0c1e-4eef-bd68-252e158f5c25",
  "AnimationControllerDefinition": "90c615ee-ede3-4711-aa3a-c9ad6897a5e6",
  "AnimationEvents": true
}
```

Others: `NPCAnimationThirdPersonStrategyDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterAnimationThirdPersonStrategyDefinitionObjectBuilder')
search_content('', type_contains='CharacterAnimationThirdPersonStrategyDefinitionObjectBuilder')
```
