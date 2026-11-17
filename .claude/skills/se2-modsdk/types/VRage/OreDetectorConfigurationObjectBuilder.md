# OreDetectorConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Components.OreDetectorConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RegionMargin` | Region trigger margin. Allows to spawn region before entity enters it. |
| `RegionPerAxis` | Number of region on each world axis. This define the area in the world where ore detection is possible. |
| `SectorPerRegion` | Number of sector in each axis per region. A region will spawn sectors only if an ore detector enters its bounds. |
| `SectorSize` | Size of a sector. A sector will query voxel storage using its bounds, large sector may slow down detection. |

## A real one

`Engine\Assets\Configurations\OreDetectorConfiguration.def`

```json
{
  "Guid": "18e54823-24b0-4db7-b7a7-2d0cea8937a8",
  "SectorSize": 1024,
  "SectorPerRegion": 4,
  "RegionPerAxis": 33554431,
  "RegionMargin": 1024
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('OreDetectorConfigurationObjectBuilder')
search_content('', type_contains='OreDetectorConfigurationObjectBuilder')
```
