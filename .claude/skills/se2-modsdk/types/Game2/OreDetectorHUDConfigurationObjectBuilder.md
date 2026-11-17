# OreDetectorHUDConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Voxels.OreDetectorHUDConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Voxels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OreDepositGPSType` | GPS type created by ore detectors. |
| `VoxelMaterialMarkers` | Describes how each detected material should be displayed. |

## A real one

`Vanilla\Assets\UI\HUD\OreDetectorHUDConfiguration.def`

Too large to inline. Fields present:

`Guid`, `OreDepositGPSType`, `VoxelMaterialMarkers`

---

Read it with the MCP server rather than by hand:

```
describe_type('OreDetectorHUDConfigurationObjectBuilder')
search_content('', type_contains='OreDetectorHUDConfigurationObjectBuilder')
```
