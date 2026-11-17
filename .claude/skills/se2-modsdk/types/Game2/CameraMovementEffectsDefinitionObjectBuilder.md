# CameraMovementEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraMovementEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AtmosphereDensityThreshold` | Atmospheric density at which the effect switch from space effect to atmosphere effect |
| `MovementEffect` | Particle Effect to spawn when the movement speed exceeds the threshold. This effect will be used in space, planet-specific effects are defined on the |
| `MovementSpeedThreshold` | Minimum movement speed threshold at which the particles become visible (relative to the CollisionSpeedThreshold speed from ) |
| `PlanetWithAtmosphereTag` | Tags that planets with atmosphere report under in the observers system |

## A real one

`Vanilla\Assets\System\Camera\CockpitFirstPersonCamera\CockpitPrefabFirstPersonCamera_CameraMovementEffectsDefinition.def`

```json
{
  "Guid": "9342e701-1901-4d4d-842f-627db9e5fc66",
  "MovementSpeedThreshold": 1,
  "AtmosphereDensityThreshold": 0,
  "MovementEffect": "dbcd2c38-cde2-4efc-9a4e-f63412539a3d",
  "PlanetWithAtmosphereTag": ""
}
```

Others: `CockpitPrefabThirdPersonCamera_CameraMovementEffectsDefinition`, `CharacterPrefabFirstPersonCamera_CameraMovementEffectsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraMovementEffectsDefinitionObjectBuilder')
search_content('', type_contains='CameraMovementEffectsDefinitionObjectBuilder')
```
