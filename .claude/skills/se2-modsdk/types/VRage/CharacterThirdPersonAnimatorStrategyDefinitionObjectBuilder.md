# CharacterThirdPersonAnimatorStrategyDefinitionObjectBuilder

`VRage:Keen.VRage.Animation.Client.GameObjects.CharacterThirdPersonAnimatorStrategyDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.Client.GameObjects`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\AnimatorThirdPerson.def`

```json
{
  "Guid": "447c68ee-ca65-4f45-872c-a1f1cf709b37",
  "AnimationPriority": 1,
  "AnimationController": "90c615ee-ede3-4711-aa3a-c9ad6897a5e6"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterThirdPersonAnimatorStrategyDefinitionObjectBuilder')
search_content('', type_contains='CharacterThirdPersonAnimatorStrategyDefinitionObjectBuilder')
```
