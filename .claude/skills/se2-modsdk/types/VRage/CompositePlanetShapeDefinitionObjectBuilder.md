# CompositePlanetShapeDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Components.CompositePlanetShapeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **33**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OverrideMaterial` | Specifies an optional material for the additive shape, allowing custom visual or physical properties to be applied. If not set, the material will be derived from the planet's heightmap. |
| `ShapeCenter` | Specifies the point within the storage to be the central point for this voxel shape. |
| `UsageType` | Specifies how the composite shape interacts with the planet's existing voxel storage. The usage type determines whether the shape adds to or removes from the planet's structure, allowing for flexible modifications to the planet's composite geometry. |
| `VoxelStorageHandle` | A reference to the resource file used to load the voxel map that defines the geometry of the composite shape. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\CompositePlanetShape.def`

```json
{
  "Guid": "dafc7676-b086-4dfa-8f4d-3ed9921ea97c",
  "VoxelStorageHandle": "{G}56ef20ee-732f-4cc2-b9a5-4fb1419e9e3f",
  "UsageType": "Additive",
  "ShapeCenter": {
    "X": 0,
    "Y": 0,
    "Z": 0
  },
  "OverrideMaterial": null
}
```

Others: `CliffRock_512_01_Composite`, `RoundCave_Y_Subtractive`

---

Read it with the MCP server rather than by hand:

```
describe_type('CompositePlanetShapeDefinitionObjectBuilder')
search_content('', type_contains='CompositePlanetShapeDefinitionObjectBuilder')
```
