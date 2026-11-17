# PBRFloraWindMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.PBRFloraWindMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **32**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AOIntensity` | Intensity of vertex AO. 1 means unaltered vertex AO and 0 ignores it. |
| `AOMultiplier` | AO multiplier on composite AO (vertex + texture) |
| `ColorMetalTexture` | Texture composed of Color (RGB) and Metalness (A) |
| `EmissivityMultiplier` | Emissivity multiplier |
| `ExtensionsTexture` | Extension texture, eg. Ambient Occlusion |
| `NormalRoughnessTexture` | Texture composed of Normal (RGB) and Roughness (A) |

## A real one

`Vanilla\Assets\Environment\Planets\Verdure\Flora\VS2_3\Flora\Olive\Texture\OliveBark.def`

```json
{
  "Guid": "2deb0063-78ba-4753-b6f4-6ba2e82ee87a",
  "DefaultState": "7ba38030-fb64-4a61-b3e0-5abd976e764c",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "ColorMetalTexture": "{G}0d2cedb3-91c1-4f9c-b5db-6a13c4e28bec",
  "NormalRoughnessTexture": "{G}e7cc4771-b480-4c6c-a35b-444f41f57755",
  "ExtensionsTexture": "{G}54914d51-9bd4-4aac-87eb-52e26b55d036",
  "EmissivityMultiplier": 0,
  "AOIntensity": 0.6,
  "AOMultiplier": 1
}
```

Others: `BirchBark`, `Cap01`

---

Read it with the MCP server rather than by hand:

```
describe_type('PBRFloraWindMaterialDefinitionObjectBuilder')
search_content('', type_contains='PBRFloraWindMaterialDefinitionObjectBuilder')
```
