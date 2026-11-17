# HitMarkerConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.HitMarker.HitMarkerConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.HitMarker`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\HitMarkerConfiguration.def`

```json
{
  "Guid": "179c2bd8-274b-44e8-8636-62f555998038",
  "ReticleOverlays": {
    "None": {
      "Size": {
        "X": 50,
        "Y": 50
      },
      "Texture": "{G}3db6c7a4-451b-4178-9bbe-d7ccdc4a5f3a"
    },
    "Critical": {
      "Size": {
        "X": 50,
        "Y": 50
      },
      "Texture": "{G}dfeb83c4-71ea-4b33-bdc2-30935ee0366d"
    },
    "Fatal": {
      "Size": {
        "X": 40,
        "Y": 40
      },
      "Texture": "{G}fd574792-619e-41f5-9e43-0223b3700a7f"
    },
    "Critical, Fatal": {
      "Size": {
        "X": 45,
        "Y": 45
      },
      "Texture": "{G}05f10b01-73e1-4d48-b438-9e502b1e9d27"
    },
    "Grid": {
      "Size": {
        "X": 47,
        "Y": 47
      },
      "Texture": "{G}b54730df-6709-44db-a0c5-c96038bd7b1d"
    },
    "Fatal, Grid": {
      "Size": {
        "X": 55,
        "Y": 55
      },
      "Texture": "{G}4b5f0c42-b841-4aab-8c13-cf01b07cff72"
    }
  },
  "HitAudio": {
    "Critical, Fatal": "event:/SFX/Character/BulletHitHeadshotCritical",
    "Critical": "event:/SFX/Character/BulletHitHeadshot"
  },
  "Duration": 3000000,
  "PopInTime": 1000000,
  "PopInScale": 2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('HitMarkerConfigurationObjectBuilder')
search_content('', type_contains='HitMarkerConfigurationObjectBuilder')
```
