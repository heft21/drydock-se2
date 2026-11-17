# PBRParallaxMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.PBRParallaxMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **69**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DepthBias` | Limits parallax offset at steep viewing angles. A value of 1.0 flattens depth along the horizon. |
| `DisplacementTexture` | Texture composed of Height (R) |
| `HeightRatio` | How deep the heightmap is in relation to the width of the texture. Typical values range 0.05 and 0.1. |

## A real one

`Vanilla\Assets\BlockMaterials\ConveyorsAtlas.def`

```json
{
  "Guid": "3020a2ff-e3b5-4990-8f96-6da1338c3de2",
  "DefaultState": "7436e9f2-f45d-4dac-9360-da3a5e87698b",
  "PinTextures": false,
  "ColorMetalTexture": "{G}9391ef96-86d7-4568-a4d8-236a43e93ce8",
  "NormalRoughnessTexture": "{G}691f3fba-ac39-470f-81af-3a0d0ae302e0",
  "ExtensionsTexture": "{G}62df83df-cad4-4b80-88f1-c907d50845c1",
  "EmissivityMultiplier": 1,
  "DisplacementTexture": "{G}bc5c31a4-af19-4a06-b41b-8f6f1ecf9d1a",
  "HeightRatio": 0.1,
  "DepthBias": 1
}
```

Others: `GratingMetallic`, `ArmorConstruction01`

---

Read it with the MCP server rather than by hand:

```
describe_type('PBRParallaxMaterialDefinitionObjectBuilder')
search_content('', type_contains='PBRParallaxMaterialDefinitionObjectBuilder')
```
