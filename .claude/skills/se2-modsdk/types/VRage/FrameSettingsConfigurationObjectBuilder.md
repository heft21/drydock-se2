# FrameSettingsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Data.FrameSettingsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Data`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArmorSettings` | Settings for armor rendering |
| `Cloud` | Settings of clouds |
| `DRS` | Settings of dynamic resolution scaling |
| `Debug` | DebugSettings allows to enable special views and other features useful for debugging |
| `Decal` | Settings for decals |
| `Environment` | Settings of the environment including background skybox, sun and ambient lighting |
| `FrameManager` | Setting of the frame manager. Frame manager serves to balance out image quality and framerate |
| `GPUParticlesSettings` | Settings for GPU particles |
| `Grass` | Settings of the wind system |
| `HBAO` | Settings of the Ambient Occlusion solution |
| `HZBO` | Settings of the hierarchical occlusion culling |
| `HologramSettings` | Settings of the hologram pass |
| `ImpostorSettings` | Settings for Impostor rendering |
| `LOD` | Settings of the LODDing - definition of the multipliers for lodding distances, lodding method etc. |
| `Light` | Setting of the light - from direction and intensity of the sun to the various local light overrides |
| `MeshEffectSettings` | Settings for mesh effects, which includes highlights |
| `Overrides` | Convenience settings used to override various aspects of the engine like lights, shadow and postprocessing |
| `PostProcess` | Settings of the post processing stack - bloom, eye adaptation etc. |
| `Raytracing` | Settings of the raytracing, specifically for the raytraced global illumination |
| `Shadow` | Specifies the parameters of the shadows for both directional light and local lights |
| `SnowSettings` | Settings for snow |
| `Water` | Settings for water |
| `WindSettings` | Settings of the wind system used in various places |

## A real one

`Engine\Assets\Core\DefaultFrameSettingsConfiguration.def`

---

Read it with the MCP server rather than by hand:

```
describe_type('FrameSettingsConfigurationObjectBuilder')
search_content('', type_contains='FrameSettingsConfigurationObjectBuilder')
```
