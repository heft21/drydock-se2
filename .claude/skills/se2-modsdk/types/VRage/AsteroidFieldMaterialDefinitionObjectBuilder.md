# AsteroidFieldMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.AsteroidFieldMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AbsorptionLength` | The distance after which the volume completely blocks the light. This gets modulated by the opacity texture. |
| `CameraFadeDistance` | Fade-in distance when the volume starts to appear beyond StartDistance |
| `Color` | The color of the field. |
| `EdgeSoftness` | Fade-in factor from the edge of the volume. 0 means hard edge and 1 means soft edge all the way to the center |
| `NoiseAmplitude` | Amplitude of the noise applied to the scattered intensity |
| `NoiseOffset` | Offset of the noise applied to the scattered intensity |
| `NoiseScale` | Scale of the noise applied to the scattered intensity |
| `ScatteringMagnitude` | Scattering amplitude of the ring which gets multiplied by the color. |
| `StartDistance` | Distance before which the volume is not rendered |

## A real one

`Vanilla\Assets\System\AsteroidRings\TestField\TestField.def`

```json
{
  "Guid": "585bb891-864b-400c-ba9b-af2304cf42e9",
  "DefaultState": "770d4b00-fd8d-41d0-9253-5d790e6c4338",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "Color": {
    "Values": {
      "X": 0.06521739,
      "Y": 0.1474359,
      "Z": 0.6117647,
      "W": 1
    }
  },
  "AbsorptionLength": 25000,
  "ScatteringMagnitude": -4,
  "StartDistance": 15000,
  "CameraFadeDistance": 10000,
  "EdgeSoftness": 1,
  "NoiseScale": 0.8,
  "NoiseOffset": 0.46533796,
  "NoiseAmplitude": 2
}
```

Others: `AsteroidFieldMap`

---

Read it with the MCP server rather than by hand:

```
describe_type('AsteroidFieldMaterialDefinitionObjectBuilder')
search_content('', type_contains='AsteroidFieldMaterialDefinitionObjectBuilder')
```
