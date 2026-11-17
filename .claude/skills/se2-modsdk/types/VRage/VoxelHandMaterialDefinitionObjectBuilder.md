# VoxelHandMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.VoxelHandMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AmbientStrength` | Ambient strength of the voxel hand lighting, in the areas where the artificial light is not applied |
| `BackfaceBrightness` | Brightness multiplier used to darken the inside of the voxel hand effect volume. |
| `EmissivityStrength` | Strength of the emissivity effect in the extension texture |
| `ExtTexture` | Optional extension texture to use, only emissive (green) and alpha (alpha) is used |
| `HighlightEmissivity` | Emissivity of the highlighted area, near where the effect intersects the terrain. |
| `HighlightOpacityFromTexture` | Whether the highlighted area, near where the effect intersects the terrain, should factor in the alpha channel from the extension texture. Set to false in order to make the highlight a flat color, and set to true to make the highlight render with the alpha channel's transparency. |
| `HighlightSize` | Size, in meters, of the highlighted area, near where the effect intersects the terrain. |
| `LightDir` | Direction, in object space, of the artificial light that illuminates the voxel hand |
| `LightingColorMultiplier` | Multiplier on the artificial lighting effect. |
| `LightingEffectExponent` | Exponent to use on the artificial lighting effect. Makes the lit highlight brighter and tighter. |
| `Texture` | Color texture to use, only RGB is used |
| `TextureSize` | Scale factor for the texture. When using UV coordinates, they are multiplied by this value. When using triplanar mapping, the texture is scaled by this value. |

## A real one

`Vanilla\Assets\System\UI3D\VoxelHandMaterial.def`

```json
{
  "Guid": "f241904b-adae-449e-af3e-8d40da213d36",
  "DefaultState": "4cb49d33-8981-4b27-815d-7cb78cee796b",
  "PinTextures": false,
  "Texture": "{G}481f82ae-3fd1-493a-9637-00d5397325b5",
  "ExtTexture": null,
  "EmissivityStrength": 0,
  "HighlightSize": 0.1,
  "HighlightEmissivity": 50,
  "HighlightOpacityFromTexture": false,
  "LightingEffectExponent": 2,
  "LightingColorMultiplier": 10,
  "LightDir": {
    "X": -0.5,
    "Y": 0.5,
    "Z": 1
  },
  "AmbientStrength": 0.8,
  "TextureSize": 0.5,
  "BackfaceBrightness": 0
}
```

Others: `VoxelHandMaterialUVCaps`, `VoxelHandMaterialUVSides`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelHandMaterialDefinitionObjectBuilder')
search_content('', type_contains='VoxelHandMaterialDefinitionObjectBuilder')
```
