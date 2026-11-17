# AsteroidRingMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.Templates.AsteroidRingMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials.Templates`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AbsorptionLength` | The distance after which the volume completely blocks the light. This gets modulated by the opacity texture. |
| `ColorOpacityTexture` | Texture composed of Color (RGB) and Opacity (A), which will premultiply the color. |
| `FadeDistance` | Fade-in distance when the volume starts to appear beyond StartDistance |
| `ScatteringMagnitude` | Scattering amplitude of the ring which gets multiplied by the color. |
| `StartDistance` | Distance before which the volume is not rendered |

## A real one

`Vanilla\Assets\System\AsteroidRings\TestRing\RingVolume.def`

```json
{
  "Guid": "8d41ba58-039f-4254-a028-b6c4ee0ebb87",
  "DefaultState": "835c99a6-cac2-4da3-a6ff-58d57af78be8",
  "PinTextures": false,
  "CustomTexelDensity": null,
  "ColorOpacityTexture": "{G}6c2e7547-29a4-43f8-bb4a-45415ac408de",
  "AbsorptionLength": 1900,
  "ScatteringMagnitude": -3.8,
  "StartDistance": 10000,
  "FadeDistance": 5000
}
```

Others: `RingVolumeMap`, `KemikRing_Volume`

---

Read it with the MCP server rather than by hand:

```
describe_type('AsteroidRingMaterialDefinitionObjectBuilder')
search_content('', type_contains='AsteroidRingMaterialDefinitionObjectBuilder')
```
