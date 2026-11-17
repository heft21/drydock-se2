# RampShapeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes.RampShapeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Depth` | Ramp depth |
| `Height` | Ramp height |
| `Width` | Ramp width |

## A real one

`Vanilla\Assets\System\Creative Tools\Voxel Hand\Shapes\VoxelHandRampShape.def`

```json
{
  "Guid": "a15d0f63-bade-4b46-8b0d-e6a2e97d01fd",
  "Name": "VoxelHandShapeRamp",
  "Icon": "{G}e8c00315-ad71-4fd0-a9db-d61db012d748",
  "HoverIcon": "{G}e8c00315-ad71-4fd0-a9db-d61db012d748",
  "Height": 1,
  "Width": 1,
  "Depth": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RampShapeDefinitionObjectBuilder')
search_content('', type_contains='RampShapeDefinitionObjectBuilder')
```
