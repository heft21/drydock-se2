# FlightHUDConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Flight.FlightHUDConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Flight`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HorizonImage` | Represents the horizon image used in the Flight HUD. |
| `HorizonIndicator` | Represents the horizon indicator graphic used in the Flight HUD. |
| `TerrainIcon` | Represents the terrain icon graphic used in the Flight HUD. |

## A real one

`Vanilla\Assets\UI\HUD\FlightHUDConfiguration.def`

```json
{
  "Guid": "32d6789f-4310-4fe4-937b-209c691294d1",
  "TerrainIcon": "{G}3c75cfbc-8595-4e30-88b5-1a46b0f2f233",
  "HorizonIndicator": "{G}6a242a69-91b7-49cc-b6f1-9302c2241b5b",
  "HorizonImage": "{G}10287db2-709d-4177-a7f1-c72d60344fa6",
  "SpeedChangeIndicator": "ac333103-9892-4768-bae4-d4449a68d165",
  "AltitudeChangeIndicator": "23ffd6a3-1762-4e68-ad2c-6fd739ef80c5"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FlightHUDConfigurationObjectBuilder')
search_content('', type_contains='FlightHUDConfigurationObjectBuilder')
```
