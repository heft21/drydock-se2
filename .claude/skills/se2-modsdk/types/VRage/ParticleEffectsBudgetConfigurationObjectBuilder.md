# ParticleEffectsBudgetConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Components.ParticleEffectsBudgetConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxCollisionParticleEffects` | Budget limit for collisions |
| `MaxCollisionSparksParticleEffects` | Budget limit for collisions sparks |
| `MaxFootstepsParticleEffects` | Budget limit for footsteps |
| `MaxThrusterDustParticleEffects` | Budget limit for thruster dust |

## A real one

`Engine\Assets\Configurations\ParticleEffectsBudgetConfiguration.def`

```json
{
  "Guid": "6cfe668e-3f0c-4726-b733-43652d19b116",
  "MaxFootstepsParticleEffects": 200,
  "MaxCollisionParticleEffects": 200,
  "MaxCollisionSparksParticleEffects": 10,
  "MaxThrusterDustParticleEffects": 200,
  "MaxBlockParticleEffects": 200
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleEffectsBudgetConfigurationObjectBuilder')
search_content('', type_contains='ParticleEffectsBudgetConfigurationObjectBuilder')
```
