# MovementHUDConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Movement.MovementHUDConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Movement`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArtificialGravityType` | Gravity type from artificial sources |
| `InertiaDampenerOffIcon` | Icon that is shown when the Inertia Dampeners are disabled |
| `InertiaDampenerOnIcon` | Icon that is shown when the Inertia Dampeners are enabled |
| `NaturalGravityType` | Gravity type from natural sources |
| `RelativeDampenerIcon` | Icon that is shown when the Relative Dampeners are enabled |

## A real one

`Vanilla\Assets\System\Configurations\MovementHUDConfiguration.def`

```json
{
  "Guid": "59463882-33e6-41be-b841-b88ab2ddbef4",
  "InertiaDampenerOnIcon": "{G}f1f3d4f9-b10f-40d5-9a6d-9b1b5ea42016",
  "InertiaDampenerOffIcon": "{G}f07eda89-27f7-4d23-8073-00b72b3e7397",
  "RelativeDampenerIcon": "{G}3c7d2d0d-37da-439a-91ad-a811cdfc0526",
  "ArtificialGravityType": "e7ae9aa5-d436-4d54-b7ec-59296d3c7edb",
  "NaturalGravityType": "5e06c1f9-3087-4611-b075-3188a6785d95",
  "SpeedUnitLabels": {
    "MetersPerSecond": "SpeedometerMetersPerSecond",
    "KilometersPerHour": "SpeedometerKilometersPerHour",
    "MilesPerHour": "SpeedometerMilesPerHour"
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MovementHUDConfigurationObjectBuilder')
search_content('', type_contains='MovementHUDConfigurationObjectBuilder')
```
