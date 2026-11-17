# SimulatedProjectileDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProjectileSystems.SimulatedProjectileDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProjectileSystems`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EntityFilterDistanceMax` | how far from the entity filter is the hit considered as self hit in |
| `ExplosionCullingDistance` | Maximum distance from the explosion center at which the explosion is allowed. If no observer with the tag configured in is within this distance, the explosion and its voxel deformation are skipped (the projectile is still removed). Set to 0 to disable explosion culling. |
| `ExplosionDefinition` | Optional for projectiles that explode when they are destroyed. |
| `IsAffectedByBulletDrop` | Whether the projectile should be affected by bullet drop. |
| `ProjectilePrefab` | Optional Prefab from which the projectile is instantiated. |

## A real one

`Vanilla\Assets\System\Projectiles\MeteorProjectile.def`

```json
{
  "Guid": "fb130746-5b7d-4d00-9521-dc43f836748e",
  "AmmoIcon": "{G}764c2baf-db08-477c-8578-d2ad46712ccf",
  "AmmoHighlightIcon": "{G}74824ead-8169-4113-a5c3-f8aaa3b7e02d",
  "Range": 40000,
  "DamageTypeToDamage": {},
  "MaximumVoxelHardnessAffected": 10,
  "Integrity": 10,
  "DefaultDecalDefinition": null,
  "CompositionToDecalDefinitions": {},
  "DeformationCoefficient": 0.5,
  "AreaEffectsRadius": 0,
  "Visuals": null,
  "Velocity": 200,
  "Mass": 45,
  "ProjectilePrefab": "b4778b4e-44a0-43db-aad0-526c94c05329",
  "IsAffectedByBulletDrop": false,
  "ExplosionDefinition": "1982c6d4-161e-4926-be5a-df05b1c766ae",
  "ExplosionCullingDistance": 500
}
```

Others: `ProjectileRocketLauncher`

---

Read it with the MCP server rather than by hand:

```
describe_type('SimulatedProjectileDefinitionObjectBuilder')
search_content('', type_contains='SimulatedProjectileDefinitionObjectBuilder')
```
