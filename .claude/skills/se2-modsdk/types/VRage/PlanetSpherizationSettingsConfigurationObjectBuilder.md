# PlanetSpherizationSettingsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Materials.PlanetSpherizationSettingsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AtmosphereSpherizationData` | The spherization data applied to the atmosphere |
| `SkyboxSpherizationData` | The spherization data applied to the skybox brightness |
| `SpherizationData` | The spherization data applied to all planets |

## A real one

`Engine\Assets\Configurations\PlanetSpherizationSettingsConfiguration.def`

```json
{
  "Guid": "32b23cce-2c78-472b-975d-187996d8e074",
  "SpherizationData": {
    "SpherizeFactor": 0.8,
    "SpherizeStart": 0.8,
    "SpherizeRange": 3
  },
  "AtmosphereSpherizationData": {
    "SpherizeFactor": 0.8,
    "SpherizeStart": 0.1,
    "SpherizeRange": 0.4
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetSpherizationSettingsConfigurationObjectBuilder')
search_content('', type_contains='PlanetSpherizationSettingsConfigurationObjectBuilder')
```
