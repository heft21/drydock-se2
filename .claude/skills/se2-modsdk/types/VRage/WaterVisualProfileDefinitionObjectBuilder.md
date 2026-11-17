# WaterVisualProfileDefinitionObjectBuilder

`VRage:Keen.VRage.Water.Components.WaterVisualProfileDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Components`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Water\WaterVisualProfiles\TestProfile1.def`

```json
{
  "Guid": "763bfcc9-7328-445b-94ee-933e19de7e53",
  "Settings": {
    "AbsorptionColor": {
      "PackedValue": 4278190335
    },
    "AbsorptionOpacity": 0.1,
    "UnderwaterOpacity": 0.2,
    "ScatteringColor": {
      "PackedValue": 4278190335
    },
    "ScatteringOpacity": 0.002,
    "FresnelSubsurfaceColor": {
      "PackedValue": 4278190335
    },
    "SubsurfaceFresnelStrength": 1,
    "FresnelReflectionColor": {
      "PackedValue": 4278190335
    },
    "FresnelF90Factor": 0.5,
    "DiffuseSubsurfaceStrength": 1,
    "FresnelMultiplier": 1,
    "Roughness": 0,
    "Metalicness": 0,
    "DepthAbsorptionScale": 10,
    "DepthAbsorptionStrength": 15,
    "WaveStrength": 1,
    "VelocityWaveStrength": 1,
    "DeepWaterAmbientTransmittance": 0.1,
    "RefractionStrength": 0,
    "FoamColor": {
      "PackedValue": 4293256677
    },
    "FoamSubsurfaceStrength": 0,
    "WaveHeightScattering": 0.5,
    "ScatteringNoiseCascadesCount": 0,
    "ScatteringNoiseScale": 0.001,
    "ScatteringVariationMultiplierMin": 0,
    "ScatteringVariationMultiplierMax": 0,
    "ScatteringNoiseScaleFalloff": 1,
    "ScatteringNoiseStrengthFalloff": 1,
    "VariationDepth": 0.15,
    "VariationSharpness": 0.5
  }
}
```

Others: `OceanVisualProfile`

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterVisualProfileDefinitionObjectBuilder')
search_content('', type_contains='WaterVisualProfileDefinitionObjectBuilder')
```
