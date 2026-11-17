# SymmetryModeConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.SymmetryMode.SymmetryModeConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.SymmetryMode`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PlaneExtendAmount` | Defines the extra distance to extend symmetry planes beyond their grid |
| `PreviewPlaneAlpha` | Override the opacity for the plane when being placed |
| `XAxisColor` | Color for the X axis plane |
| `YAxisColor` | Color for the Y axis plane |
| `ZAxisColor` | Color for the Z axis plane |

## A real one

`Vanilla\Assets\System\Configurations\SymmetryModeConfiguration.def`

```json
{
  "Guid": "68b12e9a-a43b-48f3-bdb8-540e20e7c2ee",
  "XAxisColor": {
    "PackedValue": 1073742079
  },
  "YAxisColor": {
    "PackedValue": 1073807104
  },
  "ZAxisColor": {
    "PackedValue": 1090453504
  },
  "PreviewPlaneAlpha": 128,
  "PlaneExtendAmount": 2.5
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SymmetryModeConfigurationObjectBuilder')
search_content('', type_contains='SymmetryModeConfigurationObjectBuilder')
```
