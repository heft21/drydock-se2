# TerrainPatternBrushDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.Surface.TerrainPatternBrushDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet.Surface`
- definitions using it: **74**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TextureVariations` | Texture used in the brush with frequency determined by the ratio. For example, a ratio of 3:1 for TextureA to TextureB means TextureA is used three times more often than TextureB. |

## A real one

`Vanilla\Assets\Environment\Planets\EarthLike\LakeBrush.def`

```json
{
  "Guid": "358fb457-39b3-4cc7-a5e3-93a3d40da5a0",
  "HorizontalScale": 64,
  "HeightScale": 2,
  "MidLevel": 0,
  "TextureVariations": [
    {
      "Key": "9af2de60-0252-4cdf-8b9c-b3cf3eb5be1f",
      "Value": {
        "Texture": "fd36148b-ecca-42ec-9ec5-43ee2fdded33",
        "Ratio": 1
      }
    }
  ]
}
```

Others: `DesertBrush`, `GreenGrassBrush`

---

Read it with the MCP server rather than by hand:

```
describe_type('TerrainPatternBrushDefinitionObjectBuilder')
search_content('', type_contains='TerrainPatternBrushDefinitionObjectBuilder')
```
