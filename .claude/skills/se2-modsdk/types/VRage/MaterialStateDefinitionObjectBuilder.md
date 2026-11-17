# MaterialStateDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.MaterialStateDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials`
- definitions using it: **156**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Blend` | Material blending strategy to render target. |
| `Category` | Category of the |
| `DebugViews` | Available material specific debug views |
| `Description` | Description of the material state, explaining what it is used for in user-friendly way. |
| `DomainShader` | Material domain shader. Used for compilation of the material |
| `EntityDataType` | Compatible Entity type data consumed by the shader. |
| `Flags` | Various flags supplied to render regarding rasterization, Z writes or outputs to passes |
| `GlobalDataType` | Compatible type of global custom data. |
| `HullShader` | Material hull shader. Used for compilation of the material |
| `InstanceDataType` | Compatible Instance type data consumed by the shader. |
| `Macros` | Macros supplied to shader. One shader can have multiple permutations via macros. |
| `MaterialDataType` | Compatible type of material template. |
| `Name` | Name of the material. This name is predetermined to use in UI. For logging use |
| `Options` | Available material specific options |
| `OrderLayer` | Rendering order layer of this material. Most of the materials should not need any ordering, even for transparent pipeline, as we are using Order independent transparency. However, there are some cases where custom ordering brings better result Examples: - mesh decals have to be rendered after normal opaque objects to prevent z-fighting - some expensive materials should be rendered after the cheaper ones |
| `OrderLayerOffset` | Offset within the same layer. Allows fine-tuning of the order in specific cases (terrain shader optimizations, decal layering etc.) |
| `PixelShader` | Material pixel shader. Used for compilation of the material |
| `RaytracingShader` | Material raytracing shader. Used for compilation of the material. Raytracing shader must implement same __MaterialVertex and __MaterialPixel interfaces + optional interpolation functions. Raytracing shader should be as simple as possible. |
| `TopologyType` | Primitive topology type |
| `VertexShader` | Material vertex shader. Used for compilation of the material |
| `VertexStream0Type` | Requested type of vertex stream 0 |
| `VertexStream1Type` | Requested type of vertex stream 1 |
| `VertexStream2Type` | Requested type of vertex stream 2 |

## A real one

`Engine\Assets\Materials\States\LCD.def`

```json
{
  "Guid": "f0506eb6-3ac9-4fc8-845f-62d6014c1790",
  "Category": "Default",
  "Name": "LCD",
  "Description": "LCD material with UV rotation for screen content orientation",
  "VertexShader": {
    "FullPath": "geometry\\materials\\lcdvertex.hlsl"
  },
  "PixelShader": {
    "FullPath": "geometry\\materials\\lcdpixel.hlsl"
  },
  "HullShader": null,
  "DomainShader": null,
  "RaytracingShader": null,
  "Macros": [
    {
      "Key": "627c295e-0015-4b5c-9a0b-3f51be930d79",
      "Value": "FSR_MASKS_GBUFFER"
    }
  ],
  "EntityDataType": "VRage:Keen.VRage.Core.Render.Materials.EntityCustomData",
  "InstanceDataType": "VRage:Keen.VRage.Core.Render.Materials.InstanceCustomData",
  "GlobalDataType": "VRage:Keen.VRage.Core.Render.Materials.GlobalCustomData",
  "MaterialDataType": "VRage:Keen.VRage.Core.Render.Materials.Templates.LCDMaterialDefinition",
  "TopologyType": "Triangles",
  "VertexStream0Type": "VRage:Keen.VRage.Render.Data.VertexFormat.VertexFormatPositionUV0Packed",
  "VertexStream1Type": "VRage:Keen.VRage.Render.Data.VertexFormat.VertexFormatNormalTangentPacked",
  "VertexStream2Type": "VRage:Keen.VRage.Core.Render.Data.VertexFormatNull",
  "OrderLayer": "None",
  "OrderLayerOffset": 0,
  "Blend": "Disable",
  "Flags": "StateBackfaceCulling, StateZWriteEnabled, PassGBuffer, PassDepth, PassIndirect",
  "Options": [],
  "DebugViews": [
    {
      "Key": "a6294300-477b-428a-898e-8fd4ca8dfc7e",
      "Value": "4e7c2f4c-9a33-495d-afdd-7163d9337d36"
    }
  ]
}
```

Others: `PBR`, `PBRAlpha`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialStateDefinitionObjectBuilder')
search_content('', type_contains='MaterialStateDefinitionObjectBuilder')
```
