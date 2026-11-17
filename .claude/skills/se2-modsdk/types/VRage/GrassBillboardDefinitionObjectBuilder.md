# GrassBillboardDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.GrassBillboardDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **46**

## What it is

Builder for the grass billboard

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AOMaxHeight` | Height ratio of the grass blade affected by height based AO. |
| `AlphaThreshold` | Alpha threshold for the cutout texture |
| `BaseColorHueVariance` | Per instance hue variance on base color |
| `BaseColorLuminosityVariance` | Per instance luminosity variance on base color |
| `ColorTranslucencyTexture` | Texture composed of Color (RGB) and translucency (A) texture for grass billboards |
| `ExtensionTexture` | Extension texture for alpha and ao |
| `HeightBasedAO` | Strength of height based AO. |
| `HeightBasedAODistance` | Distance at which height based AO fades out. |
| `NormalTexture` | Texture composed of Normal (RGB), A for roughness. |
| `SSSIntensity` | Subsurface scattering intensity. Controls how strong the subsurface scattering effect is on grass. The stronger the effect, the more it's gonna lit-up the shadowed side of the billboard. |
| `SSSTranslucencyThickness` | Subsurface scattering translucency thickness |

## A real one

`Vanilla\Assets\Environment\Foliage\Grass\Grass01.def`

```json
{
  "Guid": "e61ab020-ef10-4635-a1c8-f19cec321a5c",
  "ColorTranslucencyTexture": "{G}a44c1580-424e-45d6-8761-321a351aaa8f",
  "NormalTexture": "{G}64d0a5a8-6836-4ff5-bf9d-738d6b86a6f4",
  "ExtensionTexture": "{G}75cc3551-2464-4ef7-a44e-861f0b4a2cc4",
  "BaseColorHueVariance": 0.02,
  "BaseColorLuminosityVariance": -0.07,
  "SSSIntensity": 0.2,
  "SSSTranslucencyThickness": 0,
  "AlphaThreshold": 0.5
}
```

Others: `Grass02`, `Grass03`

---

Read it with the MCP server rather than by hand:

```
describe_type('GrassBillboardDefinitionObjectBuilder')
search_content('', type_contains='GrassBillboardDefinitionObjectBuilder')
```
