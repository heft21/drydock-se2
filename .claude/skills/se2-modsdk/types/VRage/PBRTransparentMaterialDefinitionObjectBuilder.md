# PBRTransparentMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.PBRTransparentMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **69**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FresnelTightness` | Fresnel tightness. 1 is "physically correct"; values below 1 will expand the angle the fresnel occurs in, and values above 1 will shrink that angle. Use low values to exaggerate the visibility of glass like materials. |
| `SpecularBaseColor` | Base specular color. Alpha of this color controls the opacity of the fresnel effect; an alpha of 1 will look like glass, whereas an alpha of 0 is better if you want to remove the fresnel for a less glass-like appearance. The brightness of the specular base color will control the actual reflectivity, use a darker value and a brighter alpha map for tinted glass. |

## A real one

`Vanilla\Assets\BlockMaterials\ClearGlass.def`

```json
{
  "Guid": "30072ea8-c740-4a4c-8c5c-1276d102d939",
  "DefaultState": "84886702-d56d-4404-a343-7fc98c238db8",
  "PinTextures": false,
  "ColorMetalTexture": "{G}97195b31-349d-4382-8665-863e85313e74",
  "NormalRoughnessTexture": "{G}989dc761-21cd-420c-b8b5-f43b3c881ea9",
  "ExtensionsTexture": "{G}bf8e00ee-9447-4b3b-a57c-7cc94ce1ac32",
  "EmissivityMultiplier": 0,
  "SpecularBaseColor": {
    "PackedValue": 4294967295
  },
  "FresnelTightness": 0.001
}
```

Others: `WindowGlass`, `FrostedGlass`

---

Read it with the MCP server rather than by hand:

```
describe_type('PBRTransparentMaterialDefinitionObjectBuilder')
search_content('', type_contains='PBRTransparentMaterialDefinitionObjectBuilder')
```
