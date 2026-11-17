# ColorIndicatorMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.ColorIndicatorMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **14**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AnimationParameters` | Parameters that determine how the indicator blinks. |
| `Color` | Color (sRGB) of the indicator. |
| `Emissivity` | Emissivity of the indicator. |

## A real one

`Vanilla\Assets\BlockMaterials\LightBulbColorIndicator.def`

```json
{
  "Guid": "f099e128-254d-48af-86c3-be6006d110ce",
  "DefaultState": "394d2de7-637d-4c16-bde0-51261fc40e00",
  "PinTextures": false,
  "Color": {
    "PackedValue": 4290838289
  },
  "Emissivity": 4,
  "AnimationParameters": null
}
```

Others: `IndicatorMaterial+ACT`, `IndicatorMaterial+RDY`

---

Read it with the MCP server rather than by hand:

```
describe_type('ColorIndicatorMaterialDefinitionObjectBuilder')
search_content('', type_contains='ColorIndicatorMaterialDefinitionObjectBuilder')
```
