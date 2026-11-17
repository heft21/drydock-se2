# PBRMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.PBRMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **779**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ColorMetalTexture` | Texture composed of Color (RGB) and Metalness (A), along with a slot for transparency which will premultiply the color. Only use the transparency slot with transparent pass materials; do not use it for alpha cutout. |
| `EmissivityMultiplier` | Emissivity multiplier. Emissive masks range from 0 to 1, so this can be used to boost the emissivity to higher values. |
| `ExtensionsTexture` | Extension texture with AO (R), Emissive (G), Color Mask (B), and Transparency (A) |
| `NormalRoughnessTexture` | Texture composed of Normal (RGB) and Roughness (A) |

## A real one

`Engine\Assets\Materials\Dev\Grid.def`

```json
{
  "Guid": "3f767d72-d408-48c5-beee-6ba238be945e",
  "DefaultState": "28b46a4e-18ee-459f-a3b1-f268e7a20801",
  "PinTextures": false,
  "ColorMetalTexture": "{G}91222364-8a35-4d34-ba4e-8854897ed4a9",
  "NormalRoughnessTexture": "{G}74a6e2a7-08eb-43b3-88fa-4bbb9ee5ef80",
  "ExtensionsTexture": "{G}9a94838f-ef58-4488-8ad5-379b31b4bec5",
  "EmissivityMultiplier": 0
}
```

Others: `Chrome`, `Copper`

---

Read it with the MCP server rather than by hand:

```
describe_type('PBRMaterialDefinitionObjectBuilder')
search_content('', type_contains='PBRMaterialDefinitionObjectBuilder')
```
