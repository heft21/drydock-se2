# PlanetMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Layers` | Specifies the material layers for a surface biome, each associated with a specific depth. Provides the option to define multiple material layers instead of just one material rule per biome. This allows for more detailed and realistic planetary surfaces through depth-based material transitions. |
| `Material` | TODO: Remove after stable deploy |
| `MaxDepth` | TODO: Remove after stable deploy |
| `Value` | TODO: Remove after stable deploy |

## A real one

`Vanilla\Assets\Environment\Planets\EarthLike\Grass.def`

```json
{
  "Guid": "dcc18242-74b0-4157-bdb1-4cb09c8ca2d4",
  "Layers": [
    {
      "Key": "dd4da5be-1983-4546-83c6-940863cd6189",
      "Value": {
        "Material": "91691e18-1d3a-45ae-a0f4-9e9594f8c8b6",
        "Depth": 1
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetMaterialDefinitionObjectBuilder')
search_content('', type_contains='PlanetMaterialDefinitionObjectBuilder')
```
