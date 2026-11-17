# TranslationAnimationDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.RigidAnimations.TranslationAnimationDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.RigidAnimations`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Speed` | The speed of translation, measured in meters per second |
| `Translation` | Specifies the direction and maximum movement distance in that direction, measured in meters |

## A real one

`Vanilla\Assets\Blocks\Warheads\50\SubParts\S1_TranslationAnimationDefinition.def`

```json
{
  "Guid": "23afbea3-dfab-462f-b6a5-420349d3ec37",
  "Speed": 0.01,
  "Translation": {
    "X": 0,
    "Y": 0.02,
    "Z": 0
  }
}
```

Others: `S2_TranslationAnimationDefinition`, `S1_TranslationAnimationDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('TranslationAnimationDefinitionObjectBuilder')
search_content('', type_contains='TranslationAnimationDefinitionObjectBuilder')
```
