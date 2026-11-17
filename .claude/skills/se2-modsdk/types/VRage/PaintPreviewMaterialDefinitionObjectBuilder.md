# PaintPreviewMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.PaintPreviewMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Emissivity` | Emissivity of the highlighted section of the dashes. Used to increase visibility in dark areas |
| `GradientAddValue` | Value to add to the color for the far side of the gradient. Used to increase visibility when a very dark color is selected. |
| `LineAnimationSpeed` | Speed that the dashes will rotate around the center. Negative values change the direction |
| `LineDashCount` | Amount of line dashes total |
| `LineDashWidth` | Amount of the dash that is solid, the rest is a gap |
| `LineThickness` | Line thickness in meters |
| `SphereEdgeCutoff` | Cosine value at which point dashed circles near the edge of the sphere will be cut off. Used to stop the paint tool sphere from overlapping the first person model of the character. |

## A real one

`Vanilla\Assets\System\UI3D\PaintPreviewMaterial.def`

```json
{
  "Guid": "8d5e67a5-625e-4144-a8dc-b762e7b62cbb",
  "DefaultState": "0c235648-8668-4061-81ac-6826ff71826a",
  "PinTextures": false,
  "LineThickness": 0.1,
  "LineDashCount": 40,
  "LineDashWidth": 0.7,
  "LineAnimationSpeed": 4,
  "SphereEdgeCutoff": 0.05,
  "Emissivity": 0.5,
  "GradientAddValue": 0.04
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PaintPreviewMaterialDefinitionObjectBuilder')
search_content('', type_contains='PaintPreviewMaterialDefinitionObjectBuilder')
```
