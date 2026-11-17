# ParticleEmitterDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Data.ParticleEmitterDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **981**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AnimationParameters` | Animation parameters |
| `EmissionParameters` | Emission parameters |
| `EmitterFlags` | Emitter flags |
| `RenderingParameters` | Rendering parameters |
| `SimulationParameters` | Simulation parameters |
| `TimeLines` | Time-varying parameters |

## A real one

`Vanilla\Assets\System\Particles\Generic\Debug\ParticleEmitter_Debug_X.def`

Too large to inline. Fields present:

`AnimationParameters`, `EmissionParameters`, `EmitterFlags`, `Guid`, `RenderingParameters`, `SimulationParameters`, `TimeLines`

Others: `ParticleEmitter_Debug_Y`, `ParticleEmitter_Debug_Z`

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleEmitterDefinitionObjectBuilder')
search_content('', type_contains='ParticleEmitterDefinitionObjectBuilder')
```
