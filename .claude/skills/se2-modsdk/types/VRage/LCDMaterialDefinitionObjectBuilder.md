# LCDMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.LCDMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FSRMaskAmount` | FSR transparence composition mask for pixels covered by this material. |
| `Orientation` | Screen content orientation (0 = 0deg, 1 = 90deg CW, 2 = 180deg, 3 = 270deg CW). |
| `ScreenAspectRatio` | Aspect ratio (width / height) of the physical screen mesh this material is applied to. Used by the LCD shader to fit the texture inside the screen without stretching. |

## A real one

`Vanilla\Assets\BlockMaterials\LCDScreen.def`

```json
{
  "Guid": "6a5cdee6-32b2-452c-aa11-c2b55319372f",
  "DefaultState": "f0506eb6-3ac9-4fc8-845f-62d6014c1790",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "ColorMetalTexture": "{G}746399c1-b17d-4a30-920a-ad23fa4acc8f",
  "NormalRoughnessTexture": "{G}276047d9-ced8-4782-8ba9-5e21cd545064",
  "ExtensionsTexture": "{G}2f499db0-6050-4df3-9651-c18bfaabea98",
  "EmissivityMultiplier": 80,
  "Orientation": 0,
  "ScreenAspectRatio": 1
}
```

Others: `LCDScreen_On`, `LCDScreen_Off`

---

Read it with the MCP server rather than by hand:

```
describe_type('LCDMaterialDefinitionObjectBuilder')
search_content('', type_contains='LCDMaterialDefinitionObjectBuilder')
```
