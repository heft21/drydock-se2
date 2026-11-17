# ParticleLightDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.ParticleLightDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **36**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FlareDefinition` | Optional artistic lens flare produced by the light |
| `FlickeringParams` | Set up flickering parameters |
| `GravityDisplacement` | Light displacement along the gravity direction |
| `LifeTime` | Light lifetime |
| `LifeTimeVariance` | Light lifetime variance |
| `StartTime` | Light start time |
| `StartTimeVariance` | Light start time variance |
| `TimeLines` | Time-varying parameters |

## A real one

`Vanilla\Assets\System\Particles\Blocks\Grinder\ParticleLight_Grinder.def`

Too large to inline. Fields present:

`FlareDefinition`, `FlickeringParams`, `GravityDisplacement`, `Guid`, `LifeTime`, `LifeTimeVariance`, `StartTime`, `StartTimeVariance`, `TimeLines`

Others: `ParticleLight_Reactor`, `ParticleLight_ArmorHit`

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleLightDefinitionObjectBuilder')
search_content('', type_contains='ParticleLightDefinitionObjectBuilder')
```
