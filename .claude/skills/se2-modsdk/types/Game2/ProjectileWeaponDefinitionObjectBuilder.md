# ProjectileWeaponDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Weapons.ProjectileWeaponDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Weapons`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FilterGrid` | if true, will be the grid rather than the block. This is only useful for weapons with multi level subparts |
| `TurretGeometry` | Only Applicable to turrets. Describes geometry of the turret rotation |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\RocketTurret_ProjectileWeaponDefinition.def`

```json
{
  "Guid": "82c7094d-886a-4fd0-a7db-2b519d6deb63",
  "RoundsPerMinute": 800,
  "VisualsPerRound": null,
  "MaxAngleDeviation": 0,
  "MaxAngleDeviationTime": 10000000,
  "DeviationResetTime": 2499999,
  "BarrelDummyType": "6fc9829d-3ee4-4735-b229-e00157f67a42",
  "Recoil": 0,
  "ReloadTime": 10000000,
  "AmmoTypes": [
    {
      "Key": "13f649fa-9a55-4d3c-9252-cb5d726c4902",
      "Value": "248b2687-a9c6-4806-8c55-d0fe4ba65784"
    }
  ],
  "MaxCapacity": 1,
  "AllowPartialReload": true,
  "FilterGrid": true,
  "TurretGeometry": null
}
```

Others: `GatlingTurret_ProjectileWeaponDefinition`, `RocketLauncher_ProjectileWeaponDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectileWeaponDefinitionObjectBuilder')
search_content('', type_contains='ProjectileWeaponDefinitionObjectBuilder')
```
