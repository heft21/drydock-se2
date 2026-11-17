# FlatColorMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.FlatColorMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **7**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Color` | Color (sRGB) of the object. |

## A real one

`Engine\Assets\Materials\Imposters\ImpostorFlatColor.def`

```json
{
  "Guid": "7a17c07a-c0b6-4236-ac63-bf869cdea7da",
  "DefaultState": "64ff3268-d5e7-48a1-98a8-9da2b926b314",
  "PinTextures": false,
  "Color": {
    "PackedValue": 4278190335
  }
}
```

Others: `ERROR-VertexFormatPosition`, `ArmorSidePreviewState Material`

---

Read it with the MCP server rather than by hand:

```
describe_type('FlatColorMaterialDefinitionObjectBuilder')
search_content('', type_contains='FlatColorMaterialDefinitionObjectBuilder')
```
