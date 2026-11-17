# PBRFloraLeavesMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.PBRFloraLeavesMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **82**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AOIntensity` | Intensity of vertex AO. 1 means unaltered vertex AO and 0 ignores it. |
| `AOMultiplier` | AO multiplier on composite AO (vertex + texture) |
| `AlphaCutoutThreshold` | Alpha cutout threshold |
| `AlphaMaskTexture` | Extension texture, eg. Ambient Occlusion |
| `BaseColorHueVariance` | Hue variance on base color based on light map uvs |
| `BaseColorLuminosityVariance` | Luminosity variance on base color based on light map uvs |
| `ColorTranslucencyTexture` | Texture composed of Color (RGB) and Translucency (A) |
| `EmissivityMultiplier` | Emissivity multiplier |
| `ExtensionsTexture` | Extension texture, eg. Ambient Occlusion |
| `FlipBackfaceNormals` | Enable backface normal flipping |
| `GlobalHue` | Global hue to apply to the texture |
| `GlobalLuminosity` | Global luminosity to apply to the texture |
| `GlobalSaturation` | Global saturation to apply to the texture |
| `NormalRoughnessTexture` | Texture composed of Normal (RGB) and Roughness (A) |
| `ReflectanceMultiplier` | Emissivity multiplier |
| `SSSHueShift` | Hue shift for SSS translucency |
| `SSSIntensity` | Global intensity of SSS |
| `SSSTranslucencyThickness` | Global intensity of SSS |

## A real one

`Vanilla\Assets\Procedural\VS2_3\Planets\Verdure\Flora\Ivy\IvyAtlas.def`

```json
{
  "Guid": "4d4acd5e-3b53-4eb3-86bc-ba0db131998d",
  "DefaultState": "441607c6-d256-42f3-94b3-6977ef3f99d0",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "ColorTranslucencyTexture": "{G}94930110-f558-4e6b-a1b9-65bad071d907",
  "NormalRoughnessTexture": "{G}eab78cc6-d0b5-4221-a027-7c7eef2cbf26",
  "ExtensionsTexture": "{G}0d1a74f5-b6ec-45bc-a763-a10d9b36aadb",
  "EmissivityMultiplier": 0,
  "ReflectanceMultiplier": 0.75,
  "AOIntensity": 1,
  "AOMultiplier": 0.8,
  "AlphaCutoutThreshold": 0.5,
  "FlipBackfaceNormals": true,
  "SSSIntensity": 0.5,
  "SSSHueShift": 0,
  "SSSTranslucencyThickness": 0.2,
  "BaseColorHueVariance": 0.03,
  "BaseColorLuminosityVariance": 0.14,
  "GlobalHue": 0,
  "GlobalSaturation": 0,
  "GlobalLuminosity": 0,
  "AlphaMaskTexture": "{G}1fdd07c2-bbc6-4fa8-a1e6-e48468a23ad5"
}
```

Others: `Mushroom`, `BirchFruit`

---

Read it with the MCP server rather than by hand:

```
describe_type('PBRFloraLeavesMaterialDefinitionObjectBuilder')
search_content('', type_contains='PBRFloraLeavesMaterialDefinitionObjectBuilder')
```
