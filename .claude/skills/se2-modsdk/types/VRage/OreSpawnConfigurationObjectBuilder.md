# OreSpawnConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.OreSpawnConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **1**

## What it is

Migrations for ore spawn configuration.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxEffectiveSlopeDegrees` | Maximum slope (in degrees) at which slope correction is applied to surface ore depth. Beyond this, correction is capped: ores on steeper terrain may visibly outcrop. |
| `OrePrefab` | Generic ore prefab for planet ore deposits. Required in order for the planet to be able to spawn ores. |
| `SurfacePadding` | Multiplier on the minimum surface clearance for surface ore deposits. 1.0 = ore top tangent to the local surface (no poke-through). Greater than 1 burries deeper, lesser then one allows them closer to surface. |

## A real one

`Engine\Assets\Configurations\OreSpawnConfiguration.def`

```json
{
  "Guid": "2b84e931-0a7a-4077-bd35-cac133e33b6a",
  "OrePrefab": "37f2f1bf-7419-441e-b593-0163014bb5fc"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('OreSpawnConfigurationObjectBuilder')
search_content('', type_contains='OreSpawnConfigurationObjectBuilder')
```
