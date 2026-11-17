# EmptyMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.EmptyMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **25**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Engine\Assets\Materials\Armor\ArmorGlobal.def`

```json
{
  "Guid": "d3f3f63f-cfd3-45f5-ac52-529392655da5",
  "DefaultState": "56ef582c-a251-4a55-8091-5ead3067253f",
  "PinTextures": false
}
```

Others: `EdgeColor2D`, `FillColor2D`

---

Read it with the MCP server rather than by hand:

```
describe_type('EmptyMaterialDefinitionObjectBuilder')
search_content('', type_contains='EmptyMaterialDefinitionObjectBuilder')
```
