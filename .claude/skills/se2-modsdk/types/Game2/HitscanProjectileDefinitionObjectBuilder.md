# HitscanProjectileDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProjectileSystems.HitscanProjectileDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProjectileSystems`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Impulse` | For hitscan projectiles we cannot calculate impulse as they have 0 mass and infinite velocity. If they should apply impulse to the hit object, it can be provided through this value. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\Projecticles\ProjectileRifle.def`

```json
{
  "Guid": "12953d5b-2c87-4f9b-8375-edbe4b25fbdb",
  "AmmoIcon": "{G}41bd3d9e-f614-4bc5-9a42-f239c45032a3",
  "AmmoHighlightIcon": "{G}2ae6b95c-8ddc-4738-a4dd-2921d3ce3daa",
  "Range": 60,
  "DamageTypeToDamage": {
    "235c92de-c788-46f2-aab0-972b2e305115": 5,
    "a28e367b-9919-4601-99f6-d333fcbdb0ba": 0.75,
    "086749bf-91d2-4089-b62e-71764eb54fc2": 6.25,
    "9fc2643b-1e26-4aa6-957d-e72b7292d505": 20,
    "798fe06a-94c8-4b50-9732-c7e957941646": 15,
    "b10eb750-79e5-4393-84d7-55a535184fa2": 50
  },
  "MaximumVoxelHardnessAffected": 4,
  "Integrity": 0,
  "DefaultDecal": "5c753183-9148-44e0-a1cc-9ac04af229b8",
  "DeformationCoefficient": 0.1,
  "AreaEffectsRadius": 0,
  "Visuals": "e631aa00-d5cb-4fec-9231-bbb7aa3d011e",
  "GunshotStimulusIntensityMultiplier": 1,
  "GunshotStimulusRadiusMultiplier": 1,
  "ImpactStimulusIntensityMultiplier": 1,
  "ImpactStimulusRadiusMultiplier": 1,
  "Impulse": 10
}
```

Others: `ProjectilePistol`, `ProjectileGatling`

---

Read it with the MCP server rather than by hand:

```
describe_type('HitscanProjectileDefinitionObjectBuilder')
search_content('', type_contains='HitscanProjectileDefinitionObjectBuilder')
```
