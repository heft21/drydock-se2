# PBREmissiveMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.PBREmissiveMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ColorizationWhenOff` | How much the light's texture colors should be tweaked, when the light is off, to match the emissive color. Useful if the bulb itself is tinted. |
| `EmissiveColor` | Color (sRGB) of the light when on |
| `EmissiveColorStrength` | Emissivity color strength. Controls how quickly the base color changes to the emissivity color as the emissivity rises. Useful if the bulb itself is not tinted but the light source is, such as with an LED. |

## A real one

`Vanilla\Assets\BlockMaterials\PBRLightBulbColorIndicator.def`

```json
{
  "Guid": "f83342c2-f76c-418a-9fe9-97e2119fb004",
  "DefaultState": "3f35202a-dc1a-4747-915a-0ac7af2e2286",
  "PinTextures": false,
  "ColorMetalTexture": "{G}76cf6d96-06d9-47ca-969d-04b74fe3e47f",
  "NormalRoughnessTexture": "{G}897d2860-3dec-4627-95c8-1c12c99a81cc",
  "ExtensionsTexture": "{G}57263e99-0d91-4465-a326-b9653d454cfd",
  "EmissivityMultiplier": 80,
  "EmissiveColor": {
    "PackedValue": 1677721599
  },
  "EmissiveColorStrength": 1,
  "ColorizationWhenOff": 0
}
```

Others: `PaintGun_Paint`, `PBRLightBulbColorIndicator_NoShadow`

---

Read it with the MCP server rather than by hand:

```
describe_type('PBREmissiveMaterialDefinitionObjectBuilder')
search_content('', type_contains='PBREmissiveMaterialDefinitionObjectBuilder')
```
