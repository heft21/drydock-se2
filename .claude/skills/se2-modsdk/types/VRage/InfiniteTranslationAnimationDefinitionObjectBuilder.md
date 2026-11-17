# InfiniteTranslationAnimationDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.RigidAnimations.InfiniteTranslationAnimationDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.RigidAnimations`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Distance` | Distance to cover by the translation before switching to the opposite direction |
| `Slowdown` | Angle speed decrease in angles/s |
| `Speedup` | Speed increase in m/s |
| `Velocity` | Velocity of the translation |

## A real one

`Vanilla\Assets\Blocks\Refinery\Refinery\750\Subparts\Refinery750_Subparts_InfiniteTranslationAnimationDefinition.def`

```json
{
  "Guid": "187b91eb-8b89-435a-9ac8-bbdf14267fc6",
  "Velocity": {
    "X": 0,
    "Y": 0.25,
    "Z": 0
  },
  "Distance": 0.65,
  "Speedup": 1,
  "Slowdown": 1
}
```

Others: `Assembler500_S1SideDeviceSubpart_InfiniteTranslationAnimationDefinition`, `Assembler500_S2FrontDeviceSubpart_InfiniteTranslationAnimationDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('InfiniteTranslationAnimationDefinitionObjectBuilder')
search_content('', type_contains='InfiniteTranslationAnimationDefinitionObjectBuilder')
```
