# SensorFieldDrawerComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Detectors.SensorFieldDrawerComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Detectors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActiveFieldColor` | Color used in the 3D preview of the sensor field. |
| `FieldColor` | Color used in the 3D preview of the sensor field. |
| `FieldCornerRatio` | Thickness of the snap grid |
| `FieldDashRatio` | Length of the dashes in the placement preview outline, as a percentage of the length of the shortest side |
| `FieldLineThickness` | Maximum thickness of the preview block's outlines |
| `FieldTransparency` | Length of the dashes in the placement preview outline, as a percentage of the length of the shortest side |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Sensor_Client_SensorFieldDrawerComponentDefinition.def`

```json
{
  "Guid": "4ec32605-2396-41e5-8d48-be5c917b8630",
  "FieldColor": {
    "PackedValue": 4293760356
  },
  "FieldLineThickness": 1,
  "FieldCornerRatio": 0.15,
  "FieldDashRatio": 0.15,
  "FieldTransparency": 0.05
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SensorFieldDrawerComponentDefinitionObjectBuilder')
search_content('', type_contains='SensorFieldDrawerComponentDefinitionObjectBuilder')
```
