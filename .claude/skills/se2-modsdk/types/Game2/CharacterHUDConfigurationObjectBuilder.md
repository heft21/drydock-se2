# CharacterHUDConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Character.CharacterHUDConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Character`
- definitions using it: **1**

## What it is

Migration part

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AntennaHighlightIcon` | Highlighted icon for the Antenna toggle |
| `AntennaIcon` | Icon for the Antenna toggle |
| `CharacterSpotLightAutoEnableStat` | that defines if the Character light automatic mode is on or off |
| `CharacterSpotlightStat` | that defines if the Character light is on or off |
| `DampenerHighlightIcon` | Highlighted icon for the Dampener toggle |
| `DampenerIcon` | Icon for the Dampener toggle |
| `EnergyDifferenceForHUDUpdate` | Energy difference for HUD update |
| `EnergyIcon` | Icon for the energy resource |
| `EnergyStat` | Character suit energy resource |
| `HealthIcon` | Icon for the health resource |
| `HealthStat` | Character health resource |
| `HydrogenStat` | Character hydrogen resource |
| `InventoryErrorIcon` | Error icon displayed for the Inventory percentage |
| `InventoryFullness` | Represents the fullness of the inventory. |
| `InventoryIcon` | Icon displayed for the Inventory percentage |
| `JetpackBoostFlightFuelIcon` | Icon for the jetpack boost flight fuel resource |
| `JetpackHighlightIcon` | Highlighted icon for the jetpack toggle |
| `JetpackIcon` | Icon for the jetpack toggle |
| `OxygenIcon` | Icon for the oxygen resource |
| `OxygenStat` | Character oxygen resource |
| `SpeedometerWarningIcon` | Icon displayed on the speedometer when the Jetpack is off or dampeners are disabled |
| `SpotlightAutoEnableHighlightIcon` | Highlighted icon for auto spotlight mode |
| `SpotlightAutoEnableIcon` | Icon for auto spotlight mode |
| `SpotlightHighlightIcon` | Highlighted icon for the spotlight toggle |
| `SpotlightIcon` | Icon for the spotlight toggle |
| `StatEffects` | Effects that show when stats go low |

## A real one

`Vanilla\Assets\UI\HUD\CharacterHUDConfiguration.def`

Too large to inline. Fields present:

`AntennaHighlightIcon`, `AntennaIcon`, `CharacterSpotLightAutoEnableStat`, `CharacterSpotlightStat`, `DampenerHighlightIcon`, `DampenerIcon`, `EnergyDifferenceForHUDUpdate`, `EnergyIcon`, `EnergyStat`, `Guid`, `HealthIcon`, `HealthStat`, `HydrogenStat`, `InventoryErrorIcon`, `InventoryFullness`, `InventoryIcon`, `JetpackBoostFlightFuelIcon`, `JetpackHighlightIcon`, `JetpackIcon`, `OxygenIcon`, `OxygenStat`, `SpeedometerSoftSpeedLimitIcon`, `SpeedometerWarningIcon`, `SpotlightAutoEnableHighlightIcon`, `SpotlightAutoEnableIcon`, `SpotlightHighlightIcon`, `SpotlightIcon`, `StatEffects`

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterHUDConfigurationObjectBuilder')
search_content('', type_contains='CharacterHUDConfigurationObjectBuilder')
```
