# SphereShapeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes.SphereShapeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes`
- definitions using it: **7**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Radius` | Sphere radius. |

## A real one

`Vanilla\Assets\CharacterTools\HandDrills\Shared\PrimaryHandDrillVoxelShape.def`

```json
{
  "Guid": "589d82e6-e229-4a55-92c2-41cd3b7f4d46",
  "Name": "VoxelHandShapSphere",
  "Icon": "{G}80fd4698-498f-48d3-a820-dc81a16f7034",
  "HoverIcon": "{G}80fd4698-498f-48d3-a820-dc81a16f7034",
  "Radius": 1
}
```

Others: `VoxelHandSphereShape`, `SecondaryHandDrillVoxelShape`

---

Read it with the MCP server rather than by hand:

```
describe_type('SphereShapeDefinitionObjectBuilder')
search_content('', type_contains='SphereShapeDefinitionObjectBuilder')
```
