# WheelSafeSpeedConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Damage.WheelSafeSpeedConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Damage`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GracePeriod` | Time after loosing contact with the ground for which cars will be subject to the increased safe speed. |
| `LayersCarIsInvulnerableTo` | Layer filter that matches the entities the car will be invulnerable to while in the extra safe speed. Entities in these layers are still damaged normally (and in fact may receive more damage). |
| `LayersInvulnerableToCar` | Layer filter that matches the entities that will be invulnerable to the car while it is within the extra safe speed. Entities in these layers will not receive any damage from the car, if the same layer is not listed in it is possible the car will receive more damage from these entities.. |
| `SafeSpeed` | Safe speed override for rovers with wheels that are contacting the ground. |

## A real one

`Vanilla\Assets\System\Grid\WheelSafeSpeedConfiguration.def`

```json
{
  "Guid": "07271e29-1b46-4c60-b192-b4dea11b1aaf",
  "SafeSpeed": 50,
  "LayersCarIsInvulnerableTo": "6bf68baf-0537-4dab-bed3-79e6599d2d42",
  "LayersInvulnerableToCar": "32ab04c4-22e8-42f3-b298-adf3dfc55bb7"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WheelSafeSpeedConfigurationObjectBuilder')
search_content('', type_contains='WheelSafeSpeedConfigurationObjectBuilder')
```
