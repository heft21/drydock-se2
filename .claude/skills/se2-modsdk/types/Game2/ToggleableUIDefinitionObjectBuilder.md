# ToggleableUIDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.UI.ToggleableUIDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.UI`
- definitions using it: **11**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\UI\ToggleableUI\FanfareScreen.def`

```json
{
  "Guid": "5f80b1d3-2c46-4a9e-b7f1-08e39dca5b24",
  "ScreenId": "FanfareScreen",
  "DisplayName": "ToggleableUIFanfare"
}
```

Others: `ReticleScreen`, `ToolbarScreen`

---

Read it with the MCP server rather than by hand:

```
describe_type('ToggleableUIDefinitionObjectBuilder')
search_content('', type_contains='ToggleableUIDefinitionObjectBuilder')
```
