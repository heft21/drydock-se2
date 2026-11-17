# ExplosionEffectsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Explosions.ExplosionEffectsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Explosions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CollisionIntensityAudioParameter` | Collision intensity parameter |
| `CollisionIntensityLarge` | Value for when a large explosion should be played |
| `CollisionIntensitySmall` | Value for when a small explosion should be played |
| `ExplosionDistanceAudioParameter` | Collision intensity parameter |
| `FallbackEffect` | In case material pair isn't found, a fallback effect is used in its stead. |
| `MassThreshold` | Which mass to consider for small or large explosions. If collider mass is over value, large explosions are played. Used to determine value for |
| `MaterialEffectList` | Dictionary of all material pairs and their event names. |
| `MaxExplosionEffectRadius` | Maximum radius of explosion effect |

## A real one

`Vanilla\Assets\System\Configurations\Effects\ExplosionEffectsConfiguration.def`

Too large to inline. Fields present:

`CollisionIntensityAudioParameter`, `CollisionIntensityLarge`, `CollisionIntensitySmall`, `ExplosionDistanceAudioParameter`, `FallbackEffect`, `Guid`, `MassThreshold`, `MaterialEffectList`, `MaxExplosionEffectRadius`

---

Read it with the MCP server rather than by hand:

```
describe_type('ExplosionEffectsConfigurationObjectBuilder')
search_content('', type_contains='ExplosionEffectsConfigurationObjectBuilder')
```
