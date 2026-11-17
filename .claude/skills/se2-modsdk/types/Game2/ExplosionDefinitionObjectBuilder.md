# ExplosionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Explosions.ExplosionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Explosions`
- definitions using it: **11**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlastWaveCoefficient` | The pressure wave coefficient increases how far will the explosion impulse be applied to affected objects (it multiplies the explosion radius). |
| `CollisionMaterial` | Setting the collision material on the projectile emitter will enable the collision and explosion systems select proper effects to use on impact. |
| `DamageTypeToDamage` | Mapping of damage type to damage value for each object type that should be damaged by this explosion. This represents the explosive energy released in the center of the explosion - it will decay with distance. The keys should correspond to the damage type StringIds from IHitReceiver Definition. Example: "Block" -> 5, "Character" -> 10 |
| `ExplosionDecal` | Decal to be placed when explosion happens |
| `MaximumVoxelHardnessAffected` | Maximum voxel hardness affected by the blast. See |

## A real one

`Vanilla\Assets\System\Explosions\Inventory.def`

```json
{
  "Guid": "e936cb9f-3445-4efd-988f-d292770b2ddd",
  "ExplosionRadius": 3,
  "BlastWaveCoefficient": 2.5,
  "DamageTypeToDamage": {
    "235c92de-c788-46f2-aab0-972b2e305115": 200,
    "a28e367b-9919-4601-99f6-d333fcbdb0ba": 100,
    "1a83ac16-b2e3-4fa5-869f-fa1cd63b290e": 100,
    "9fc2643b-1e26-4aa6-957d-e72b7292d505": 225,
    "798fe06a-94c8-4b50-9732-c7e957941646": 100
  },
  "MaximumVoxelHardnessAffected": 6,
  "CollisionMaterial": "cb3c95ed-3d47-4cf7-bd3a-4c845a8a809a",
  "ExplosionDecal": "9929a8be-ff5f-4342-90b9-aaafa912ae3e"
}
```

Others: `MetorExplosion`, `RocketExplosion`

---

Read it with the MCP server rather than by hand:

```
describe_type('ExplosionDefinitionObjectBuilder')
search_content('', type_contains='ExplosionDefinitionObjectBuilder')
```
