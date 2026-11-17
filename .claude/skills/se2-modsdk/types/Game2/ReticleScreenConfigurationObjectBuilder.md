# ReticleScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Reticle.ReticleScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Reticle`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArrowIndicator` | Visual data for the arrow indicators on controlled grid. In normalized screen coordinates. |
| `FullOpacityAngle` | Angle difference between observed entity and camera under which reticle will be completely visible. |
| `NoOpacityAngle` | Angle difference between observed entity and camera above which reticle will be completely invisible. |
| `Reticles` | Mapping of reticle types to corresponding visual data that defines the size and texture of each reticle. |

## A real one

`Vanilla\Assets\System\Configurations\ReticleScreenConfiguration.def`

```json
{
  "Guid": "36d776aa-632a-4b65-bcec-c2c39048cf5d",
  "Reticles": {
    "Default": {
      "Size": {
        "X": 4,
        "Y": 4
      },
      "Texture": "{G}c1af0591-0a5d-41a9-9815-d033171247c7"
    },
    "Character": {
      "Size": {
        "X": 4,
        "Y": 4
      },
      "Texture": "{G}c1af0591-0a5d-41a9-9815-d033171247c7"
    },
    "Grid": {
      "Size": {
        "X": 32,
        "Y": 32
      },
      "Texture": "{G}945a77c1-fb87-42b7-a637-81f03bb52c4d"
    }
  },
  "ArrowIndicator": {
    "RelativeScale": 0.4,
    "MinCenterDistance": 1,
    "MaxCenterDistance": 2,
    "InitialSpacing": 3,
    "Spacing": 4
  },
  "DeviationIndicator": {
    "Size": {
      "X": 58,
      "Y": 58
    },
    "Texture": "{G}8ea162a6-8441-4586-8159-a6532e8b0a94"
  },
  "DeviationIndicatorScale": 1200,
  "DeviationIndicatorOffset": 11,
  "DeviationSmoothingTime": 200000,
  "FullOpacityAngle": 15,
  "NoOpacityAngle": 30
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ReticleScreenConfigurationObjectBuilder')
search_content('', type_contains='ReticleScreenConfigurationObjectBuilder')
```
