# VoxelPlanetWatchdogConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Components.VoxelPlanetWatchdogConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PlanetRadiusFactor` | Factor to divide by to form the planet center check collider |

## A real one

`Engine\Assets\Configurations\VoxelPlanetWatchdogConfiguration.def`

```json
{
  "Guid": "90df5203-d5c1-4b8b-b0b4-a65f7fc78e07",
  "PlanetRadiusFactor": 8,
  "SparseUpdate": null,
  "TrackingSparseUpdate": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelPlanetWatchdogConfigurationObjectBuilder')
search_content('', type_contains='VoxelPlanetWatchdogConfigurationObjectBuilder')
```
