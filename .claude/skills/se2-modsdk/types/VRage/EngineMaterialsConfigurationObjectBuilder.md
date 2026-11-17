# EngineMaterialsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Materials.EngineMaterialsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FloraRaytracingMaterial` | Material to be used for raytracing flora meshes |
| `ImpostorMaterial` | Material to be used with the impostor meshes |
| `Lit` | Materials set for lit |
| `RTXPointLightImposterMaterial` | Default material for raytraced point light imposters |
| `RTXSpotLightImposterMaterial` | Default material for raytraced spot light imposters |
| `Unlit` | Materials set for unlit |
| `_defaultVertexFormatPosition` | Default material for the meshes with stream |
| `_defaultVertexFormatPositionUV0Packed` | Default material for the meshes with stream |
| `_defaultVertexFormatPositionUV0PackedVertexFormatNormalTangentPacked` | Default material for the standard asset meshes |

## A real one

`Engine\Assets\Configurations\Setup\EngineMaterialsConfiguration.def`

```json
{
  "Guid": "9b2de48b-9bb7-4ed9-9b33-4b9c4d82aaa7",
  "ImpostorMaterial": "447c769f-6e2e-4d01-8263-64c38017a83e",
  "FloraRaytracingMaterial": "eddc5436-98bf-4e22-9a7f-cb2b71cd3276",
  "Unlit": {
    "FillColor": "99659628-657d-4ca1-9e03-8703214d2562",
    "FillColorOpaque": "9651f1f3-ae93-44ec-83d7-f69c364cbd7f",
    "FillColorNoDepth": "b2eab858-1f1c-4b46-b34e-1d5aada5c039",
    "FillColorNoDepthOpaque": "aa533c22-fa39-4769-8ad2-bfe473ef081f",
    "EdgeColor": "96be67f5-25c1-4330-84a1-290d340e27d8",
    "EdgeColorOpaque": "cef5a004-fa25-4060-94ff-5689aff016c1",
    "EdgeColorNoDepth": "f272250a-1f18-484a-8408-e1fb7c133287",
    "EdgeColorNoDepthOpaque": "63cc436d-5273-45d6-ac89-005a6a895c76",
    "FillColor2D": "737e90a8-c7dd-47dd-9e16-1b3e74f9915e",
    "EdgeColor2D": "6a4d062a-134a-4a64-b3a6-3a338a131e78"
  },
  "Lit": {
    "FillColor": "046e87cf-f408-48f6-92bb-2cdd9e8d0b11",
    "FillColorOpaque": "0ea0497b-36da-4669-8234-aef4f8bbdfa5",
    "FillColorNoDepth": "36af2f01-c602-4aa2-8010-6f33429f67c5",
    "FillColorNoDepthOpaque": "977a5447-121c-48ba-a4a1-157ab3d457eb",
    "EdgeColor": "57491c74-86ea-454e-ab97-72ef0a449838",
    "EdgeColorOpaque": "4d6e156f-8ae8-4c81-8787-6e527f7e9d0b",
    "EdgeColorNoDepth": "85251181-f81a-469b-af48-2c8ceab1fffd",
    "EdgeColorNoDepthOpaque": "a07a1c48-cbb0-4407-94a7-a1f42e031ad7",
    "FillColor2D": "737e90a8-c7dd-47dd-9e16-1b3e74f9915e",
    "EdgeColor2D": "6a4d062a-134a-4a64-b3a6-3a338a131e78"
  },
  "RTXPointLightImposterMaterial": "da6c5136-8827-4b88-a538-aecab8a42b40",
  "RTXSpotLightImposterMaterial": "12ad8a0f-5a07-43aa-81fa-396c072fb1e5",
  "_defaultVertexFormatPosition": "c667a176-023f-4776-b069-5a6befc6bb82",
  "_defaultVertexFormatPositionUV0Packed": "3255c2e3-e55f-4f10-b56e-51e36fe708b0",
  "_defaultVertexFormatPositionUV0PackedVertexFormatNormalTangentPacked": "d6a50783-e11f-4c4e-8e73-06b7f74fd4bc"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EngineMaterialsConfigurationObjectBuilder')
search_content('', type_contains='EngineMaterialsConfigurationObjectBuilder')
```
