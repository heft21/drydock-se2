# PlanetSpherizationOverrideDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Materials.PlanetSpherizationOverrideDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials`
- definitions using it: **10**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AtmosphereSpherizationOverride` | The spherization data applied to the atmosphere of a planet. If null - the value from is used |
| `SkyboxSpherizationOverride` | The spherization data applied to the skybox brightness of a planet. If null - the value from is used |
| `SpherizationOverride` | The spherization data applied to the planet. If null - the value from is used |

## A real one

`Vanilla\Assets\Environment\Planets\MarsLike\MarsLike_PlanetSpherizationOverrideDefinition.def`

```json
{
  "Guid": "f259ae05-ef19-464f-8aa6-2c15a5e93558",
  "SpherizationOverride": null,
  "AtmosphereSpherizationOverride": null,
  "SkyboxSpherizationOverride": null
}
```

Others: `EarthLike_PlanetSpherizationOverrideDefinition`, `Testerrain_PlanetSpherizationOverrideDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetSpherizationOverrideDefinitionObjectBuilder')
search_content('', type_contains='PlanetSpherizationOverrideDefinitionObjectBuilder')
```
