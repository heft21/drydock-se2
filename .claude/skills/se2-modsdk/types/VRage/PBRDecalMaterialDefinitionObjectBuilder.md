# PBRDecalMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Materials.Decals.PBRDecalMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials.Decals`
- definitions using it: **24**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\UI3D\VoxelHand\Axis\VoxelHandMaterial_Axis.def`

```json
{
  "Guid": "58646778-6cb4-4b4f-80ad-6e46009767e0",
  "ColorMetalTexture": "{G}0dd74c63-606b-4ae5-a0fb-2c883bfcc7e0",
  "NormalRoughnessTexture": "{G}d092d45f-6aed-42cb-9305-941611b7e65c",
  "ExtensionsTexture": "{G}e7057c98-3bcb-455b-981c-69d545a23fdf",
  "EmissivityMultiplier": 200
}
```

Others: `WheelTracks_DecalMaterial`, `WheelTracks_Sand_DecalMaterial`

---

Read it with the MCP server rather than by hand:

```
describe_type('PBRDecalMaterialDefinitionObjectBuilder')
search_content('', type_contains='PBRDecalMaterialDefinitionObjectBuilder')
```
