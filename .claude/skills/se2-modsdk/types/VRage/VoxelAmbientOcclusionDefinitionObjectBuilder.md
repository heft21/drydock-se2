# VoxelAmbientOcclusionDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Definitions.VoxelAmbientOcclusionDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Definitions`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Arguments` | Argument for the ambient occlusion algorithm. |

## A real one

`Vanilla\Assets\Environment\System\BoulderVoxelAmbientOcclusion.def`

```json
{
  "Guid": "64007eef-6433-45fc-9a23-84412da390dd",
  "Arguments": {
    "Min": 0.1,
    "Max": 0.9,
    "LODOffset": 1,
    "InterpolationCurve": 2,
    "InterpolationCurveLodAmplifier": 1.2,
    "RangeAmplifier": 4,
    "RangeAmplifierLodReducer": 0.5
  }
}
```

Others: `AsteroidVoxelAmbientOcclusion`, `PlanetVoxelAmbientOcclusion`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelAmbientOcclusionDefinitionObjectBuilder')
search_content('', type_contains='VoxelAmbientOcclusionDefinitionObjectBuilder')
```
