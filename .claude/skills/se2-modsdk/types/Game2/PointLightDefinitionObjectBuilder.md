# PointLightDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Shared.Visuals.Lights.Point.PointLightDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Shared.Visuals.Lights.Point`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\PointLightDefinition.def`

```json
{
  "Guid": "2e284287-2f05-40ee-8a2d-610c3fc9176a",
  "MaxLightBrightness": 1000,
  "FalloffRangeMultiplier": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PointLightDefinitionObjectBuilder')
search_content('', type_contains='PointLightDefinitionObjectBuilder')
```
