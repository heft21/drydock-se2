# SensorVisualizationConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Detectors.SensorVisualizationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Detectors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxFields` | Maximum number of fields that will be rendered at once. |
| `MaximumViewingDistance` | Maximum distance the field is visible. |
| `ObserverTag` | Observer used to detect field maximum range. |

## A real one

`Vanilla\Assets\System\Configurations\SensorVisualizationConfiguration.def`

```json
{
  "Guid": "28f64f5a-b56a-44b8-948e-5096a431dd48",
  "MaxFields": 20,
  "MaximumViewingDistance": 500
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SensorVisualizationConfigurationObjectBuilder')
search_content('', type_contains='SensorVisualizationConfigurationObjectBuilder')
```
