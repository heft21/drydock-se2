# BaseColorDecalMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Materials.Decals.BaseColorDecalMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials.Decals`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Texture` | Texture composed of Color (RGB) and Opacity (A) |

## A real one

`Vanilla\Assets\System\UI3D\VoxelHand\VoxelHand_Decal_X.def`

```json
{
  "Guid": "953feeb4-ad8b-4615-847a-584490b5222e",
  "Texture": "{G}0dd74c63-606b-4ae5-a0fb-2c883bfcc7e0"
}
```

Others: `ProjectionAxisXDecal`, `ProjectionAxisYDecal`

---

Read it with the MCP server rather than by hand:

```
describe_type('BaseColorDecalMaterialDefinitionObjectBuilder')
search_content('', type_contains='BaseColorDecalMaterialDefinitionObjectBuilder')
```
