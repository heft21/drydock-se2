# PBRFloraWindImpostorMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.PBRFloraWindImpostorMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **76**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AOMultiplier` | AO multiplier on composite AO (vertex + texture) |
| `AlphaCutoutThreshold` | Alpha cutout threshold |
| `BaseColorHueVariance` | Hue variance on base color based on light map uvs |
| `BaseColorLuminosityVariance` | Luminosity variance on base color based on light map uvs |
| `ColorTexture` | Texture composed of Color (RGB) and Translucency (A) |
| `EmissivityMultiplier` | Emissivity multiplier |
| `ExtensionsTexture` | Extension texture, eg. Ambient Occlusion |
| `GlobalHue` | Global hue to apply to the texture |
| `GlobalLuminosity` | Global luminosity to apply to the texture |
| `GlobalSaturation` | Global saturation to apply to the texture |
| `ImpostorAtlasSize` | Number of rows and columns in the atlas of the imposter |
| `NormalRoughnessTexture` | Texture composed of Normal (RGB) and Roughness (A) |
| `Reflectance` | Emissivity multiplier |
| `SSSHueShift` | Hue shift for SSS translucency |
| `SSSIntensity` | Global intensity of SSS |
| `ShadowBias` | Shadow bias |
| `Type` | Shadow bias |

## A real one

`Vanilla\Assets\Environment\Planets\Verdure\Flora\VS2_0\Flora\Baobab\Texture\Large_Baobab_ImpostorNear.def`

```json
{
  "Guid": "5b2368c1-d846-47ce-83d1-905bea9aba56",
  "DefaultState": "548c1c47-3a90-46bd-8eff-de0e27a6fc19",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "ColorTexture": "{G}aef9555f-30a8-46ae-bb74-fd7893c8511b",
  "NormalRoughnessTexture": "{G}0ad05ff4-663f-4df0-8b54-446046213fec",
  "ExtensionsTexture": "{G}b07b1b0f-9cba-45d9-8ffc-9b975158c5c7",
  "EmissivityMultiplier": 0,
  "Reflectance": 0.5,
  "SSSIntensity": 0.1,
  "SSSHueShift": 0,
  "BaseColorHueVariance": 0,
  "BaseColorLuminosityVariance": 0,
  "ImpostorAtlasSize": 16,
  "AlphaCutoutThreshold": 0.5,
  "ShadowBias": -0.03,
  "Type": "FullSphere",
  "GlobalHue": 0,
  "GlobalSaturation": 0,
  "GlobalLuminosity": 0,
  "AOMultiplier": 1
}
```

Others: `Large_Poplar01_ImpostorNear`, `Large_OliveTree_ImpostorNear`

---

Read it with the MCP server rather than by hand:

```
describe_type('PBRFloraWindImpostorMaterialDefinitionObjectBuilder')
search_content('', type_contains='PBRFloraWindImpostorMaterialDefinitionObjectBuilder')
```
