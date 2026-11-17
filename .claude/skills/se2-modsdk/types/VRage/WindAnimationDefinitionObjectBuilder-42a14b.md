# WindAnimationDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.Wind.WindAnimationDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.Wind`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Branch1Motion` | Parameters for the motion of level 1 branches |
| `Branch2Motion` | Parameters for the motion of level 2 branches |
| `RippleMotion` | Parameters for the motion ripples through the leaves |
| `SharedMotion` | Parameters for the motion of branches |

## A real one

`Vanilla\Assets\Procedural\VS2_3\Planets\Verdure\Flora\RoundBush\Wind_RoundBush.def`

```json
{
  "Guid": "999f8b87-5805-4ea9-923c-980c3b6fb252",
  "SharedMotion": {
    "Enabled": true,
    "Bend": 0.3,
    "Oscillation": 0.3,
    "Speed": 1,
    "Turbulence": 1,
    "Flexibility": 0,
    "StartHeight": 0.075
  },
  "Branch1Motion": {
    "Enabled": true,
    "Bend": 0.19,
    "Oscillation": 0.56,
    "Speed": 1,
    "Turbulence": 0.8,
    "Flexibility": 0,
    "Independence": 0.1,
    "StretchLimit": 0.5
  },
  "Branch2Motion": {
    "Enabled": true,
    "Bend": 0.19,
    "Oscillation": 0.3,
    "Speed": 1,
    "Turbulence": 0.8,
    "Flexibility": 0,
    "Independence": 0.2,
    "StretchLimit": 0.5
  },
  "RippleMotion": {
    "Enabled": true,
    "Planar": 0.02,
    "Directional": 0.02,
    "Speed": 1,
    "Flexibility": 0,
    "Independence": 3,
    "Shimmer": 0
  }
}
```

Others: `Wind_Medium_AridBush`, `Wind_Small_Acacia`

---

Read it with the MCP server rather than by hand:

```
describe_type('WindAnimationDefinitionObjectBuilder')
search_content('', type_contains='WindAnimationDefinitionObjectBuilder')
```
