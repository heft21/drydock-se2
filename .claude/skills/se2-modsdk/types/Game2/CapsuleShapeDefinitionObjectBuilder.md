# CapsuleShapeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes.CapsuleShapeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Height` | Height/length of the capsule in meters |
| `Radius` | Radius of the capsule in meters |

## A real one

`Vanilla\Assets\System\Creative Tools\Voxel Hand\Shapes\VoxelHandCapsuleShape.def`

```json
{
  "Guid": "881ade9e-ddea-472d-ab0d-79ea37c33b82",
  "Name": "VoxelHandShapeCapsule",
  "Icon": "{G}f913e4c7-9111-434b-a27f-d195cc14585b",
  "HoverIcon": "{G}f913e4c7-9111-434b-a27f-d195cc14585b",
  "Height": 5,
  "Radius": 1
}
```

Others: `Drill350_CapsuleShapeDefinitionPrimary`, `Drill350_CapsuleShapeDefinitionSecondary`

---

Read it with the MCP server rather than by hand:

```
describe_type('CapsuleShapeDefinitionObjectBuilder')
search_content('', type_contains='CapsuleShapeDefinitionObjectBuilder')
```
