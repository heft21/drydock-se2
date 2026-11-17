# WaterOperatorDefinitionObjectBuilder

`VRage:Keen.VRage.Water.Components.WaterOperatorDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `WaterAddArea` | The area in which water is added |
| `WaterRemoveArea` | The area in which water is removed |

## A real one

`Vanilla\Assets\System\Creative Tools\Water Hand\WaterHandOperator\WaterHandWaterOperator.def`

```json
{
  "Guid": "36245f47-cce6-46e5-9cf9-a0227ad208a0",
  "WaterAddArea": {
    "Name": "SmallDumpingArea",
    "Transform": {
      "Transform": {
        "Position": {
          "X": 0,
          "Y": 0,
          "Z": 0
        },
        "Orientation": {
          "X": 0,
          "Y": 0,
          "Z": 0,
          "W": 1
        }
      },
      "EulerHint": {
        "X": 0,
        "Y": 0,
        "Z": 0
      }
    },
    "Scale": {
      "X": 3,
      "Y": 3,
      "Z": 3
    },
    "Type": "e730dd0e-b06a-4108-b96d-21c2e1b53bce",
    "SupportingFracture": null
  },
  "WaterRemoveArea": {
    "Name": "SmallPumpingArea",
    "Transform": {
      "Transform": {
        "Position": {
          "X": 0,
          "Y": 0,
          "Z": 0
        },
        "Orientation": {
          "X": 0,
          "Y": 0,
          "Z": 0,
          "W": 1
        }
      },
      "EulerHint": {
        "X": 0,
        "Y": 0,
        "Z": 0
      }
    },
    "Scale": {
      "X": 3,
      "Y": 3,
      "Z": 3
    },
    "Type": "071da1d1-6bba-4367-9700-cceda8082aa9",
    "SupportingFracture": null
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterOperatorDefinitionObjectBuilder')
search_content('', type_contains='WaterOperatorDefinitionObjectBuilder')
```
