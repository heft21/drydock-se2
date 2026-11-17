# PaintToolConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.PaintToolConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultBrushRadius` | Default radius of the paint brush. When 0, the brush is a single line. |
| `DefaultColors` | Default color palette |
| `DefaultPaletteIndex` | Index of the default color to select in |
| `MaxBrushRadius` | Maximum allowed radius for the paint brush. |

## A real one

`Vanilla\Assets\System\Configurations\PaintToolConfiguration.def`

```json
{
  "Guid": "5862b5da-1891-4fb2-ae40-65eefbf8f498",
  "DefaultColors": [
    {
      "Key": "dccf50da-ec01-48b5-97f0-b1ff3021eb98",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0,
          "Z": 0.45,
          "W": 1
        }
      }
    },
    {
      "Key": "feb0cca3-e268-4bc6-a791-2228b3ae7108",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0,
          "Z": 0.65,
          "W": 1
        }
      }
    },
    {
      "Key": "a3c18aa0-6009-44d6-ba06-bb5d39c180eb",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0.8,
          "Z": 0.5,
          "W": 1
        }
      }
    },
    {
      "Key": "e6f42ae1-d38d-442d-87c7-cb5e8d8341d6",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0.95,
          "Z": 0.7,
          "W": 1
        }
      }
    },
    {
      "Key": "0c7948ee-4a18-49f9-82e3-921ae790fce3",
      "Value": {
        "Values": {
          "X": 0.33333334,
          "Y": 0.32,
          "Z": 0.2,
          "W": 1
        }
      }
    },
    {
      "Key": "45e0893c-4d94-4164-9ea2-94cc2ed4c40e",
      "Value": {
        "Values": {
          "X": 0.33333334,
          "Y": 0.47,
          "Z": 0.4,
          "W": 1
        }
      }
    },
    {
      "Key": "755b8b44-4e55-48aa-a0aa-079cc6ba3e3f",
      "Value": {
        "Values": {
          "X": 0.575,
          "Y": 0.8,
          "Z": 0.45,
          "W": 1
        }
      }
    },
    {
      "Key": "05170d65-efe4-4768-bff7-e965bf088770",
      "Value": {
        "Values": {
          "X": 0.575,
          "Y": 0.95,
          "Z": 0.65,
          "W": 1
        }
      }
    },
    {
      "Key": "3a10b12e-6395-433b-b721-5b0295edc380",
      "Value": {
        "Values": {
          "X": 0.12222222,
          "Y": 0.7,
          "Z": 0.71,
          "W": 1
        }
      }
    },
    {
      "Key": "87d65552-b0da-4fe6-8a84-40d82821637a",
      "Value": {
        "Values": {
          "X": 0.12222222,
          "Y": 0.85,
          "Z": 0.91,
          "W": 1
        }
      }
    },
    {
      "Key": "82968422-1b65-4763-b8a9-f8ed8a93c811",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0,
          "Z": 0.85,
          "W": 1
        }
      }
    },
    {
      "Key": "b3c4f3c4-3ccd-4245-b23b-85205217a993",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0,
          "Z": 1,
          "W": 1
        }
      }
    },
    {
      "Key": "b5e2d9a0-476b-4dce-8f92-e6908fe91939",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0,
          "Z": 0,
          "W": 1
        }
      }
    },
    {
      "Key": "c19c272e-d1a7-4d78-89e8-baf59fa4ce96",
      "Value": {
        "Values": {
          "X": 0,
          "Y": 0,
          "Z": 0.15,
          "W": 1
        }
      }
    }
  ],
  "DefaultPaletteIndex": 7,
  "DefaultBrushRadius": 0,
  "MaxBrushRadius": 20
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PaintToolConfigurationObjectBuilder')
search_content('', type_contains='PaintToolConfigurationObjectBuilder')
```
