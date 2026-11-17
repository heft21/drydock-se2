# MapSectorMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.MapSectorMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GradientColor` | The color and opacity of the sector's gradient |
| `GradientThickness` | The thickness of the sector's gradient |
| `LineColor` | The color and opacity of the sector's line border |
| `LineThickness` | The thickness of the sector's lines |
| `MainColor` | The main color and opacity of the sector |

## A real one

`Vanilla\Assets\System\ColonizationMap\Models\MapSectorMaterial.def`

```json
{
  "Guid": "985dc538-4556-4ef1-a385-45b0b1e3813a",
  "DefaultState": "252ee355-6b45-4308-9025-3e83e5d90f31",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "OpacityTexture": "{G}a4c69799-fdb1-45cd-ac16-f7a033daf5e3",
  "NormalRoughnessTexture": "{G}7db0fabf-974d-4a01-b321-b3412bfc30d5",
  "RefractiveIndex": 1.02,
  "EmissivityStrength": 0.15,
  "CollisionHighlightDistance": 0.09961,
  "HighlightStrength": 10,
  "HighlightFalloffPower": 8.28666,
  "AnimationSpeed": {
    "X": 0.025,
    "Y": 0.00025
  },
  "UVScale": {
    "X": 4,
    "Y": 4
  },
  "MainColor": {
    "PackedValue": 436174719
  },
  "GradientColor": {
    "PackedValue": 2963376718
  },
  "LineColor": {
    "PackedValue": 2509207832
  },
  "GradientThickness": 0.45,
  "LineThickness": 0.0005
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MapSectorMaterialDefinitionObjectBuilder')
search_content('', type_contains='MapSectorMaterialDefinitionObjectBuilder')
```
