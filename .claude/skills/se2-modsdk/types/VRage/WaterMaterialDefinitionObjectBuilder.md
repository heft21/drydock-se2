# WaterMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.WaterMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DensityColor` | Controls the absorption color of the volume. The chosen color will look like the final color of a volume absorbing a white light. |
| `DensityMultiplier` | Multiplier of the volume density. Used to model the effects of constant absorption and scattering coefficients. |

## A real one

`Engine\Assets\Materials\Global\PlanetWaterMaterial.def`

```json
{
  "Guid": "189bbce9-5723-4979-bdb8-1421074851a9",
  "DefaultState": "f54081f0-f671-44c1-b235-1850d1794fb9",
  "PinTextures": false,
  "DensityMultiplier": 0.06,
  "DensityColor": {
    "PackedValue": 4287056144
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterMaterialDefinitionObjectBuilder')
search_content('', type_contains='WaterMaterialDefinitionObjectBuilder')
```
