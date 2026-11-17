# CockpitHUDConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Cockpit.CockpitHUDConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Cockpit`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AntennaHighlightIcon` | Highlighted icon for the Antenna toggle |
| `AntennaIcon` | Icon representing the antenna status of the grid |
| `BatteryChargeIcon` | Icon for the Battery charge resource bar |
| `DampenerHighlightIcon` | Highlighted icon for the Dampener toggle |
| `DampenerIcon` | Icon for the Dampener toggle |
| `GridPowerHighlightIcon` | Highlighted icon representing the grid power status of the grid |
| `GridPowerIcon` | Icon representing the grid power status of the grid |
| `HydrogenIcon` | Icon for the hydrogen resource bar |
| `InventoryErrorIcon` | Error icon displayed for the Inventory percentage |
| `InventoryFullness` | Represents the fullness of the inventory. |
| `InventoryIcon` | Icon underneath the inventory percentage icon |
| `ParkingBrakeHighlightIcon` | Highlighted icon representing the parking brake status of the cockpit |
| `ParkingBrakeIcon` | Icon representing the parking brake status of the cockpit |
| `PowerUsageIcon` | Icon for the power usage resource bar |

## A real one

`Vanilla\Assets\UI\HUD\CockpitHUDConfiguration.def`

```json
{
  "Guid": "997ea15a-b6b8-4b1c-9705-70a77ce29ebf",
  "AntennaIcon": "{G}0c0cef0f-aade-4e29-b8b9-01aca8750b52",
  "AntennaHighlightIcon": "{G}eec11e71-49b9-4572-bef2-2fa0d66271ee",
  "ParkingBrakeIcon": "{G}edb96123-5827-4aa7-ba4a-b9e60e5c52ac",
  "ParkingBrakeHighlightIcon": "{G}8d37b5b8-a651-4f75-9f2f-0e33244c5773",
  "DampenerIcon": "{G}952b4b49-dadb-4c91-a2f7-b33709c7da98",
  "DampenerHighlightIcon": "{G}fa3c256d-332d-4805-9a3e-161c28e5ceb1",
  "GridPowerIcon": "{G}8294b498-795e-429b-a0b7-1d409a8edec0",
  "GridPowerHighlightIcon": "{G}562b53ee-bc1a-4d82-8a4d-a8b7a28ffeb9",
  "InventoryIcon": "{G}4c242a22-9886-417b-a4d9-c386ac4c2349",
  "InventoryErrorIcon": "{G}9e93802d-967a-4ab8-affb-a32d1cfae1d7",
  "BatteryChargeIcon": "{G}7c0a191b-9ce9-4ebb-8326-04d72f7d58b7",
  "PowerUsageIcon": "{G}ef095032-1a8f-45c6-ab90-26844b171df2",
  "HydrogenIcon": "{G}9e440cec-6de0-4a89-a703-6853f2b40958",
  "InventoryFullness": 100,
  "StallLiftRatio": 1,
  "StallRecoveryLiftRatio": 1.1,
  "StallVerticalSpeedThreshold": 0.3,
  "StallWarningDelay": 0.5,
  "StallWarningAudio": "event:/UI/CockpitStallWarning"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CockpitHUDConfigurationObjectBuilder')
search_content('', type_contains='CockpitHUDConfigurationObjectBuilder')
```
