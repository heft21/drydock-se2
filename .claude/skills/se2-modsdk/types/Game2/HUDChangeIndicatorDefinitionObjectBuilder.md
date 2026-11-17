# HUDChangeIndicatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Flight.HUDChangeIndicatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Flight`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\UI\HUD\SpeedChangeIndicator.def`

```json
{
  "Guid": "ac333103-9892-4768-bae4-d4449a68d165",
  "LinesPerGroup": 5,
  "LineThickness": 2,
  "LineSpacing": 3,
  "MaxScrollPixelsPerSecond": 200,
  "RateForMaxScroll": 40,
  "RateDeadzone": 0.5,
  "RateSmoothing": 0.2
}
```

Others: `AltitudeChangeIndicator`

---

Read it with the MCP server rather than by hand:

```
describe_type('HUDChangeIndicatorDefinitionObjectBuilder')
search_content('', type_contains='HUDChangeIndicatorDefinitionObjectBuilder')
```
