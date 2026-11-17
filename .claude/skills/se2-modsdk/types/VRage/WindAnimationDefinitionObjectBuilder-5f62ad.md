# WindAnimationDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.WindAnimationDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **38**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Procedural\VS2_0\Planets\Verdure\Flora\Baobab\Wind_Large_Baobab.def`

```json
{
  "Guid": "2e60fa43-39fa-47ad-b243-7559df720c53",
  "SharedMotion": {
    "Enabled": true,
    "Bend": 7.202,
    "Oscillation": 6.574,
    "Speed": 0.1,
    "Turbulence": 1,
    "Flexibility": 0,
    "StartHeight": 0.25
  },
  "Branch1Motion": {
    "Enabled": true,
    "Bend": 3.434,
    "Oscillation": 15,
    "Speed": 0.1,
    "Turbulence": 0.8,
    "Flexibility": 0,
    "Independence": 1,
    "StretchLimit": 8
  },
  "Branch2Motion": {
    "Enabled": true,
    "Bend": 8.159,
    "Oscillation": 13,
    "Speed": 0.2,
    "Turbulence": 0.8,
    "Flexibility": 0,
    "Independence": 2.87,
    "StretchLimit": 10
  },
  "RippleMotion": {
    "Enabled": true,
    "Planar": 0.647,
    "Directional": 0.647,
    "Speed": 3,
    "Flexibility": 0,
    "Independence": 3,
    "Shimmer": 0
  }
}
```

Others: `WindSmallReinDeer`, `Wind_SmallSaltBush`

---

Read it with the MCP server rather than by hand:

```
describe_type('WindAnimationDefinitionObjectBuilder')
search_content('', type_contains='WindAnimationDefinitionObjectBuilder')
```
