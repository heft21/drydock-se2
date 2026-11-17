# WaterRenderingConfigurationObjectBuilder

`VRage:Keen.VRage.Water.Client.WaterRenderingConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Client`
- definitions using it: **1**

## What it is

Removal of volumetric water debug materials from WaterRenderingConfiguration.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `WaterFoamTextures` | foam textures |
| `WaterParticleMaterial` | Material used for experimental mode of rendering water with individual particles |
| `WaterParticleUnitSphere` | Unit sphere used for experimental mode of rendering water with individual particles |
| `WaterParticlesEffect` | Water particles effect |

## A real one

`Engine\Assets\Configurations\WaterRenderingConfiguration.def`

```json
{
  "Guid": "109864e9-0fba-43c9-bbff-36fabfc75607",
  "VolumetricWaterMaterial": "28837cea-eb51-4312-9ce6-58a51014415b",
  "VolumetricWaterLODsDebugMaterial": "624df3c8-f90a-4cc8-be8a-2ee8f5c081f1",
  "VolumetricWaterDensityDebugMaterial": "ef3ebec5-bea5-474c-9a5a-44e05dce00f2",
  "WaterParticleUnitSphere": "{G}cb345be6-fa58-4001-843b-bc2100fe4e37",
  "WaterParticleMaterial": "e9d09ea8-b7f3-4d51-b604-a90ed9b38f73",
  "WaterParticlesEffect": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterRenderingConfigurationObjectBuilder')
search_content('', type_contains='WaterRenderingConfigurationObjectBuilder')
```
