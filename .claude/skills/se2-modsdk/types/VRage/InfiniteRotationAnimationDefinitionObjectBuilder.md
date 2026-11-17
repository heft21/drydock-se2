# InfiniteRotationAnimationDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.RigidAnimations.InfiniteRotationAnimationDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.RigidAnimations`
- definitions using it: **49**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AngularSlowdown` | The rate of decrease in angular speed |
| `AngularSpeed` | The angular speed of the rotation, measured in degrees per second |
| `AngularSpeedup` | The rate of increase in angular speed |
| `RotationAxis` | The axis around which the rotation occurs |
| `VariableAngularInterpolatedSpeed` | An option for animation to adhere to . When provided interpolation value is 0 - is used. If the interpolation value is 1 - is used. values in between will cause interpolation. If the value is null then is used always |

## A real one

`Vanilla\Assets\CharacterTools\HandDrills\Shared\HandDrill_HeadRotation.def`

```json
{
  "Guid": "166da595-297d-4958-b82f-ba7e80d87f97",
  "RotationAxis": {
    "X": 1,
    "Y": 0,
    "Z": 0
  },
  "AngularSpeed": 360,
  "AngularSpeedup": 720,
  "AngularSlowdown": 360
}
```

Others: `Drill350_HeadRotation`, `HandGrinder_HeadAnimation`

---

Read it with the MCP server rather than by hand:

```
describe_type('InfiniteRotationAnimationDefinitionObjectBuilder')
search_content('', type_contains='InfiniteRotationAnimationDefinitionObjectBuilder')
```
