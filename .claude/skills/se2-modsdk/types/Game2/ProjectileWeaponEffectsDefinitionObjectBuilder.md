# ProjectileWeaponEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Weapons.ProjectileWeaponEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Weapons`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlwaysSpawnEffectAtDummy` | If true, the effect will be spawned at dummy position |
| `BarrelOffset` | Offset of the muzzle flash position |
| `BarrelOrientationOffset` | Offset of the muzzle flash orientation |
| `MaxMuzzleEffectsAtTheSameTime` | How many muzzle effects exist at the same time. Additional effects will be reused |
| `OnFireParticle` | Particle that spawns when the weapon fires a projectile |

## A real one

`Vanilla\Assets\CharacterTools\DebugGun\DebugGun_Client_GunToolEffectsDefinition.def`

```json
{
  "Guid": "c540819f-f5f9-40ad-bf2b-15c7b6434344",
  "BarrelOrientationOffsetEuler": {
    "X": 0,
    "Y": 0,
    "Z": 0
  },
  "OnFireParticle": {
    "ParticleEffect": "7e5569ac-4fe6-479f-959e-af2897802fb9",
    "Dummy": "6fc9829d-3ee4-4735-b229-e00157f67a42",
    "Scale": 1
  },
  "BarrelOffset": {
    "X": 0,
    "Y": 0,
    "Z": 0
  },
  "BarrelOrientationOffset": {
    "X": 0,
    "Y": 0,
    "Z": 0,
    "W": 1
  },
  "MaxMuzzleEffectsAtTheSameTime": 5,
  "AlwaysSpawnEffectAtDummy": true
}
```

Others: `ProjectileWeaponEffectsDefinition`, `InteriorTurret_Subpart_ProjectileWeaponEffectsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectileWeaponEffectsDefinitionObjectBuilder')
search_content('', type_contains='ProjectileWeaponEffectsDefinitionObjectBuilder')
```
