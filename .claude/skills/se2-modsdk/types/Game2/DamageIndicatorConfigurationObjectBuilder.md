# DamageIndicatorConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.DamageIndicator.DamageIndicatorConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.DamageIndicator`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\DamageIndicatorConfiguration.def`

```json
{
  "Guid": "1bff65f5-33c7-4be6-98cb-ee90f6d560f4",
  "Tiers": {
    "Light": {
      "MinDamageFraction": 0,
      "Size": {
        "X": 250,
        "Y": 250
      },
      "Texture": "{G}1d1563ed-9477-47f1-a84a-1bc40ee56d1b"
    },
    "Moderate": {
      "MinDamageFraction": 0.1,
      "Size": {
        "X": 250,
        "Y": 250
      },
      "Texture": "{G}e628959e-f1d7-4e89-a76f-7bd7aff952bf"
    },
    "Heavy": {
      "MinDamageFraction": 0.25,
      "Size": {
        "X": 250,
        "Y": 250
      },
      "Texture": "{G}9ebff3fa-9c81-4184-9fd0-173e0e33d2c4"
    }
  },
  "CriticalOverrideTexture": "{G}060ff5d4-c12d-461d-896d-0d2fe927ead3",
  "Radius": 200,
  "MaxIndicators": 4,
  "DamageAccumulationWindow": 4000000,
  "HoldDuration": 3000000,
  "FadeOutDuration": 15000000,
  "UnknownSourceAnchorDistance": 50,
  "TrackSourceEntity": true,
  "NearMissVisuals": {
    "MinDamageFraction": 0,
    "Size": {
      "X": 96,
      "Y": 96
    },
    "Texture": "{G}060ff5d4-c12d-461d-896d-0d2fe927ead3"
  },
  "NearMissRadius": 1,
  "NearMissFullIntensityRadius": 0.5,
  "NearMissMaxOpacity": 0.5,
  "NearMissHoldDuration": 1000000,
  "NearMissFadeOutDuration": 4000000,
  "NearMissCooldownPerSource": 2000000,
  "MaxNearMissesPerFrame": 8
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DamageIndicatorConfigurationObjectBuilder')
search_content('', type_contains='DamageIndicatorConfigurationObjectBuilder')
```
