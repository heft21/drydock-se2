# CameraWeatherEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Weather.CameraWeatherEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Weather`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AltitudeFadeEnd` | Distance in meters relative to the cloud top where the altitude fade of effects ends (intensity reaches 0). Negative values end the fade below the cloud top. Must be greater than for fading to occur. |
| `AltitudeFadeStart` | Distance in meters relative to the cloud top where the altitude fade of effects begins. Negative values start the fade below the cloud top. At this altitude, intensity is still 1. |
| `AudioEffect` | Optional looping audio event to play at the camera location. |
| `OcclusionRaycastDistance` | Maximum raycast distance used to check for spawn obstructions. |
| `ParticleDefinition` | Particle effect used for this weather (rain, dust, snow, etc.). Expected to be a camera-local effect (looping / volumetric). |
| `ParticleSpawnCount` | Maximum number of particle effect instances. |
| `ParticleSpawnRadius` | Radius around the camera where particles may be spawned. |
| `ShelteredAudioVolumeMultiplier` | Audio volume multiplier when fully sheltered (0 = silent, 1 = full volume). Volume will smoothly interpolate between this value and 1 based on sheltered factor. |
| `ShelteredFogMultiplier` | Fog foreground occlusion intensity multiplier when fully sheltered (0 = no foreground occlusion, 1 = full foreground occlusion). |
| `ShelteredTransitionTime` | Time in seconds for the sheltered transition to complete (from fully exposed to fully sheltered or vice versa). |
| `ShelteredWindMultiplier` | Wind intensity multiplier when fully sheltered (0 = no wind, 1 = full wind). Wind will smoothly interpolate between this value and 1 based on sheltered factor. |
| `VelocitySpawnBias` | Multiplier controlling how far ahead the spawn volume is shifted along the camera velocity. Higher values push particles further in the direction of travel. |
| `WeatherIntensityParameter` | Parameter to use for modulating audio intensity |
| `WeatherIntensityParameterMax` | Max value for |
| `WindSettingsOverride` | Optional override of wind for vegetation / grass. Only strength and grass bending amplitude are affected, direction remains planet default. |
| `WindShake` | Optional continuous camera shake driven by the wind at the camera. When null the wind shake job no-ops and only the gust modulated render wind change applies. |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\DefaultCameraWeatherEffectsDefinition.def`

```json
{
  "Guid": "91b3fce5-35ce-4dc5-8ce5-72ebb669b993",
  "ParticleDefinition": null,
  "ParticleSpawnRadius": 150,
  "ParticleSpawnCount": 60,
  "VelocitySpawnBias": 1,
  "OcclusionRaycastDistance": 30,
  "AudioEffect": "",
  "WeatherIntensityParameter": "",
  "WeatherIntensityParameterMax": 1,
  "ShelteredTransitionTime": 1,
  "ShelteredAudioVolumeMultiplier": 0.2,
  "ShelteredWindMultiplier": 0.2,
  "ShelteredFogMultiplier": 0.75,
  "AltitudeFadeStart": -200,
  "AltitudeFadeEnd": 100,
  "WindSettingsOverride": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraWeatherEffectsDefinitionObjectBuilder')
search_content('', type_contains='CameraWeatherEffectsDefinitionObjectBuilder')
```
