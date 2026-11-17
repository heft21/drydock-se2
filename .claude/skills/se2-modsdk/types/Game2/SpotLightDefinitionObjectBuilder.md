# SpotLightDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Shared.Visuals.Lights.Spot.SpotLightDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Shared.Visuals.Lights.Spot`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AmbientLightIntensityMultiplier` | Intensity multiplier of the ambient point light, if the ambient point light is included |
| `IncludeAmbientPointLight` | Enable a point light to add some ambient lighting whenever the spotlight is active. This light does not cast shadows |
| `OuterAngle` | Angle of the spotlight's outer cone in radians |
| `OuterConeStartRadius` | Starting radius of the outer cone of the spotlight in meters |

## A real one

`Vanilla\Assets\System\Spectator\SpectatorSpotlightComponent.def`

```json
{
  "Guid": "b3066485-6696-49cf-b80b-0b05aeb55423",
  "MaxLightBrightness": 130,
  "FalloffRangeMultiplier": 50,
  "OuterAngle": 1.786,
  "OuterConeStartRadius": 0,
  "IncludeAmbientPointLight": true,
  "AmbientLightIntensityMultiplier": 0.3
}
```

Others: `CharacterSpotlightComponent`, `SpotLightDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('SpotLightDefinitionObjectBuilder')
search_content('', type_contains='SpotLightDefinitionObjectBuilder')
```
