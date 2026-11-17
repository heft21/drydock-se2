# CollisionEffectsConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Definitions.CollisionEffectsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AngleThreshold` | Threshold value of the dot product between the normal and the direction of impact |
| `CollisionCategories` | Dictionary of collision categories which takes, with the maximum impulse required to consider them. Category will be chosen if collision impulse <= value |
| `CollisionIntensityAudioParameter` | Collision intensity parameter |
| `CollisionIntensitySoundThreshold` | Minimum collision impulse that produces effects. |
| `CollisionSoundCooldown` | The minimum time before another sound from the same is played due to close collisions in time. |
| `ForcedPlayEffectGroups` | Array of material groups that should force effect regardless of . |
| `MaterialDirectionalEffectList` | Dictionary of all material pairs and their event names. |
| `MaterialEffectList` | Dictionary of all material pairs and their event names. |
| `SoundConstantImpulseDifference` | Before another sound from the same is played due to constant collisions, verify that incoming impulse is above or below previous impulse +/- this value. If not, the impulse is considered constant and collision sounds are not constantly played |
| `SoundEffectClusterRadius` | Nearby contacts cluster sounds. This parameter represents the maximum distance between nearby contacts that will form a single cluster. |
| `TangentialCollisionParameters` | Dictionary of all material pairs and their event names. |

## A real one

`Engine\Assets\Configurations\CollisionEffectsConfiguration.def`

```json
{
  "Guid": "ce9dffa6-0700-4f51-a860-26e542367bf4",
  "CollisionIntensityAudioParameter": "CollisionIntensity",
  "CollisionIntensitySoundThreshold": 30,
  "CollisionCategories": [],
  "SoundEffectClusterRadius": 2,
  "MaterialEffectList": [],
  "TangentialCollisionParameters": {
    "ThresholdAngle": 0,
    "ThresholdSpeed": 0,
    "MaxScalingSpeed": 0,
    "MaxScalingImpulse": 0,
    "MaxScale": 0,
    "MergeDist": 0
  },
  "MaterialDirectionalEffectList": [],
  "ForcedPlayEffectGroups": [],
  "CollisionSoundCooldown": 0,
  "SoundConstantImpulseDifference": 0,
  "AngleThreshold": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CollisionEffectsConfigurationObjectBuilder')
search_content('', type_contains='CollisionEffectsConfigurationObjectBuilder')
```
