# PlanetaryWaterLayersDefinitionObjectBuilder

`VRage:Keen.VRage.Water.Components.PlanetaryWaterLayersDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Components`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Layers` | Layers are shells around the planet with defined thickness. Each layer can define different water profiles. Layers are structured sequentially starting at the planet center. |

## A real one

`Vanilla\Assets\System\Water\PlanetaryWaterLayers\VerdureWaterLayersDefinition.def`

```json
{
  "Guid": "d287d35b-0e86-4c58-add9-fe38f992d721",
  "Layers": [
    {
      "Key": "910e12b5-eb9d-425c-ac73-b55ee12fb932",
      "Value": {
        "Thickness": 0.9,
        "Blending": 0.0035,
        "Latitudes": [
          {
            "Key": "5eeb629c-3a4d-4363-b70d-735057af179c",
            "Value": {
              "Angle": 180,
              "Blending": 0,
              "Profile": "ce788763-59f5-4947-8208-bc4f49257ab7"
            }
          }
        ]
      }
    },
    {
      "Key": "6ec859b1-903c-4890-b4ba-61cc03a409f8",
      "Value": {
        "Thickness": 0.105,
        "Blending": 0.004,
        "Latitudes": [
          {
            "Key": "660d191a-edc9-4f5e-9ecf-37860297fbc6",
            "Value": {
              "Angle": 180,
              "Blending": 0,
              "Profile": "f3758eee-d286-494d-9f43-f8cc1ba1af8f"
            }
          }
        ]
      }
    },
    {
      "Key": "e522deb7-a97a-49e8-81e8-7c00da1213f7",
      "Value": {
        "Thickness": 0.035,
        "Blending": 0.005,
        "Latitudes": [
          {
            "Key": "5ac56c63-bdb5-4289-a0af-5ff514906a1b",
            "Value": {
              "Angle": 180,
              "Blending": 0,
              "Profile": "7c97708f-e66d-4c0e-8555-b5eedeed083d"
            }
          }
        ]
      }
    },
    {
      "Key": "24850841-7c5d-45cc-bc1b-38efca7a4568",
      "Value": {
        "Thickness": 0.05,
        "Blending": 0.03,
        "Latitudes": [
          {
            "Key": "836475c6-906d-442c-ad5b-44580793ceba",
            "Value": {
              "Angle": 180,
              "Blending": 0,
              "Profile": "c89d8667-5878-4a1f-bfb1-a5087bac2861"
            }
          }
        ]
      }
    }
  ]
}
```

Others: `EarthLikeWaterLayersDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetaryWaterLayersDefinitionObjectBuilder')
search_content('', type_contains='PlanetaryWaterLayersDefinitionObjectBuilder')
```
