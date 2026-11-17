# MaterialStateOptionsDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.MaterialStateOptionsDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials`
- definitions using it: **7**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FeatureName` | Name of the feature - use slashes to group the options Particles/LightingQuality, Particles/ShadowQuality |
| `OptionsList` | Available values. The first one is considered default. |

## A real one

`Engine\Assets\Materials\Options\PlanetOverlayOption.def`

```json
{
  "Guid": "6a2674f3-ca8e-491b-a650-a27f123add0d",
  "FeatureName": "Terrain/PlanetOverlay",
  "OptionsList": {
    "_data": [
      {
        "Key": "e261a4c5-7c86-4cd6-89f0-a89057dd26a8",
        "Value": {
          "OverrideName": "On",
          "Defines": {
            "_data": [
              {
                "Key": "81db86f3-fdda-47fa-a283-86a45b543e07",
                "Value": {
                  "Name": "PLANET_OVERLAY",
                  "Value": ""
                }
              }
            ]
          },
          "RenderFlagsAddition": 0
        }
      },
      {
        "Key": "ce15490e-e305-4839-9f46-d63270d40ed4",
        "Value": {
          "OverrideName": "Off",
          "Defines": {
            "_data": []
          },
          "RenderFlagsAddition": 0
        }
      }
    ]
  }
}
```

Others: `ArmorEdgeBevelOption`, `TriplanarQualityOption`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialStateOptionsDefinitionObjectBuilder')
search_content('', type_contains='MaterialStateOptionsDefinitionObjectBuilder')
```
