# UI3DConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.UI3D.UI3DConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.UI3D`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CapsuleCylinder` | Unused, will be removed TODO: SE2-17158 |
| `CapsuleHemisphere` | Unused, will be removed TODO: SE2-17158 |
| `CapsuleModel` | Unused, will be removed TODO: SE2-17158 |
| `CornerLengthPercent` | Unused, will be removed TODO: SE2-17158 |
| `CubeModel` | Unused, will be removed TODO: SE2-17158 |
| `DashLengthPercent` | Unused, will be removed TODO: SE2-17158 |
| `DrawOutlineDots` | Unused, will be removed TODO: SE2-17158 |
| `DrawVolumeDots` | Unused, will be removed TODO: SE2-17158 |
| `Emissivity` | Emissivity of the placement outline material |
| `Font` | Default font to use for UI text |
| `HighlightLengthPercent` | Unused, will be removed TODO: SE2-17158 |
| `PlacementOutline` | Shader to use when rendering with depth testing |
| `PlacementOutlineCenterSize` | Unused, will be removed TODO: SE2-17158 |
| `PlacementOutlineEdgeMargin` | Unused, will be removed TODO: SE2-17158 |
| `PlacementOutlineNondepth` | Shader to use when rendering without depth testing |
| `PlacementOutlineThickness` | Unused, will be removed TODO: SE2-17158 |
| `RampModel` | Unused, will be removed TODO: SE2-17158 |
| `SphereModel` | Unused, will be removed TODO: SE2-17158 |
| `SymmetryPlaneAntialiasingFactor` | Size, in world-space scaling units, of the fading region of the symmetry planes. A larger value means there will be a longer fade. Note that the value is scaled based on the extents of the symmetry area bounds. |
| `VoxelHandHighlightColor` | Unused, will be removed TODO: SE2-17158 |
| `VoxelHandHighlightSize` | Unused, will be removed TODO: SE2-17158 |

## A real one

`Vanilla\Assets\System\Configurations\UI3DConfiguration.def`

```json
{
  "Guid": "2e4af449-4cba-4c21-b2d9-a57dea68ad59",
  "Font": "0c519c1d-22ea-49ea-b82c-70e3a937f193",
  "PlacementOutline": "cf2f28b4-52af-439d-8f9f-cb3cb4136659",
  "PlacementOutlineNondepth": "eee39281-6d30-4e13-a2a1-9045e5e4e634",
  "Emissivity": 5,
  "PlacementOutlineThickness": 0.01,
  "PlacementOutlineEdgeMargin": 0.025,
  "PlacementOutlineCenterSize": 0.25,
  "DashLengthPercent": 0.3,
  "CornerLengthPercent": 0.15,
  "HighlightLengthPercent": 0.15,
  "DrawOutlineDots": true,
  "DrawVolumeDots": true,
  "SymmetryPlaneAntialiasingFactor": 0.002,
  "VoxelHandHighlightColor": {
    "X": 0.9911022,
    "Y": 0.5209957,
    "Z": 0,
    "W": 1
  },
  "VoxelHandHighlightSize": 0.1,
  "SphereModel": "{G}93f6efb6-a225-4d58-82d5-43cddf871796",
  "CubeModel": "{G}6e1f971d-08a4-41e7-bd7d-a01adf7d3431",
  "CapsuleModel": "{G}587016a9-1a48-4c3f-a08f-bb39b08f1e7c",
  "CapsuleCylinder": "{G}587016a9-1a48-4c3f-a08f-bb39b08f1e7c",
  "CapsuleHemisphere": "{G}f3403a21-3f8c-4e17-8610-4610c45e28c3",
  "RampModel": "{G}30b09b47-5606-46e1-be5d-93f9d27f390a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UI3DConfigurationObjectBuilder')
search_content('', type_contains='UI3DConfigurationObjectBuilder')
```
