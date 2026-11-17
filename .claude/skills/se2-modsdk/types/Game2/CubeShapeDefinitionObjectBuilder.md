# CubeShapeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes.CubeShapeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Depth` | Cube depth in meters |
| `Height` | Cube height in meters |
| `Width` | Cube width in meters |

## A real one

`Vanilla\Assets\System\Creative Tools\Voxel Hand\Shapes\VoxelHandCubeShape.def`

```json
{
  "Guid": "19c56602-75b4-4603-b233-c30d2d385398",
  "Name": "VoxelHandShapeCube",
  "Icon": "{G}43aee8d4-a0e0-4d74-9aba-178fbb0fdc19",
  "HoverIcon": "{G}43aee8d4-a0e0-4d74-9aba-178fbb0fdc19",
  "Height": 1,
  "Width": 1,
  "Depth": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeShapeDefinitionObjectBuilder')
search_content('', type_contains='CubeShapeDefinitionObjectBuilder')
```
