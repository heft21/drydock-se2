# AudioVisualEffectDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Definitions.AudioVisualEffectDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Definitions`
- definitions using it: **65**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AudioEffect` | Path to the FMOD audio effect. One-shot sound |
| `MinimumAudioVelocity` | Minimum velocity at which the audio effect will be played. |
| `ParticleEffectDefinition` | Particle effect to play |
| `ProjectileHitOrientation` | Direction in which the visual effects will be oriented relative to the projectile hit. will orient the visual effects in the direction of the hit surface's normal. will orient the visual effects towards the shot incident direction. |

## A real one

`Vanilla\Assets\Characters\System\CharacterHit.def`

```json
{
  "Guid": "3a19c2e6-fb2f-4b87-8abd-cb6056c38525",
  "AudioEffect": "event:/SFX/Character/BulletHit",
  "MinimumAudioVelocity": null,
  "ParticleEffectDefinition": "79accfa5-e83b-4783-8ff6-c0b1edb3acfd",
  "ProjectileHitOrientation": "HitNormal"
}
```

Others: `WarheadArm`, `Placeholder`

---

Read it with the MCP server rather than by hand:

```
describe_type('AudioVisualEffectDefinitionObjectBuilder')
search_content('', type_contains='AudioVisualEffectDefinitionObjectBuilder')
```
