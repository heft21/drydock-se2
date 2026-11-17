# InteractionHintConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Interaction.InteractionHintConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Interaction`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\UI\HUD\InteractionHintConfiguration.def`

```json
{
  "Guid": "e7c7c5b9-1f5c-4f8b-9d99-f78734fbb2b7",
  "OverlapWeight": 1000,
  "ConnectorLengthWeight": 0.05,
  "MovementWeight": 0.2,
  "SwitchWeight": 10,
  "OverlapDeadZone": 0.15,
  "OverlapExponent": 2,
  "TargetGap": 24,
  "ScreenMargin": 100,
  "BorderThickness": 2,
  "ConnectorThickness": 2,
  "CrosshairConnectorOffset": 16,
  "FallbackTargetSize": 32,
  "SwitchScoreMargin": 25,
  "MinSwitchInterval": 9000000,
  "PositionSmoothingTime": 100000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InteractionHintConfigurationObjectBuilder')
search_content('', type_contains='InteractionHintConfigurationObjectBuilder')
```
