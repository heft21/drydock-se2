# ProjectileVisualsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.ProjectileSystems.ProjectileVisualsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.ProjectileSystems`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ImpactMaterialEffectList` | Optional per-projectile impact effects by material. Overrides the global for materials present in this dictionary. Materials not listed fall back to the global configuration. |
| `ImpactScale` | Scale of the impact particle effect for this projectile. If zero, uses the global configuration scale. |
| `TracerEffect` | for the tracers. |
| `TracerVelocityMultiplier` | Velocity multiplier for the tracer effect |

## A real one

`Vanilla\Assets\System\Projectiles\ProjectileVisuals.def`

```json
{
  "Guid": "7ae481b5-af05-42c5-9241-6f2c2e5d6c50",
  "TracerEffect": "fae1f955-53bf-4f9c-9ea9-cd45f0b6bc64",
  "TracerVelocityMultiplier": 5
}
```

Others: `ProjectileRifle_VisualsDefinition`, `ProjectilePistol_VisualsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectileVisualsDefinitionObjectBuilder')
search_content('', type_contains='ProjectileVisualsDefinitionObjectBuilder')
```
