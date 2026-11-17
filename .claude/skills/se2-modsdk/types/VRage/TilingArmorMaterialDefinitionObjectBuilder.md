# TilingArmorMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.TilingArmorMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **18**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaterialInstances` | Material instances to project on mesh sides. Currently supports up to 2 materials. |
| `TileSize` | The size (width, height) in meters for each tile. The dimensions specified should match the textures (aspect ratio) used to avoid stretching. |
| `Tiles` | Tiling Matrix as a sequence of rows, first Tile (Tile11) at top left. Ex: 2x2 => Tile11, Tile21, Tile12, Tile22. Currently supports up to 16 tiles. |
| `TilesCount` | The number of rows and columns in the Tiles Matrix. Currently supports up to 16 tiles. |

## A real one

`Vanilla\Assets\BlockMaterials\ArmorConstruction01Tiled.def`

```json
{
  "Guid": "f06208fe-e1e8-446a-a639-016ce0549c81",
  "DefaultState": "db82e006-c9d1-436f-aa4b-48d7a0d59769",
  "PinTextures": false,
  "MaterialInstances": [
    {
      "Key": "94c8ee45-c596-4f5e-8278-7ea0c42400d0",
      "Value": "f5b0c9b9-fdf0-454a-9ce5-b647b3f98902"
    }
  ],
  "Tiles": [
    {
      "Key": "585de411-bfa5-42a1-b90d-e2e06b6ffb41",
      "Value": {
        "MaterialIndex": 0,
        "Transform": "NoTransform"
      }
    },
    {
      "Key": "d95cb491-2aa3-494f-ac8e-5bb1e64e6b2d",
      "Value": {
        "MaterialIndex": 0,
        "Transform": "Mirrored"
      }
    },
    {
      "Key": "8f1d0a2c-4608-407c-a8e2-e683aa7ea454",
      "Value": {
        "MaterialIndex": 0,
        "Transform": "Rotated"
      }
    },
    {
      "Key": "22dc818b-3388-4b64-ba0a-aa0678674d7f",
      "Value": {
        "MaterialIndex": 0,
        "Transform": "RotatedMirrored"
      }
    }
  ],
  "TilesCount": {
    "X": 2,
    "Y": 2
  },
  "TileSize": {
    "X": 7,
    "Y": 7
  }
}
```

Others: `ArmorConstruction02Tiled`, `ArmorConstruction03Tiled`

---

Read it with the MCP server rather than by hand:

```
describe_type('TilingArmorMaterialDefinitionObjectBuilder')
search_content('', type_contains='TilingArmorMaterialDefinitionObjectBuilder')
```
