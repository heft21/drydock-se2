# BlueprintConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Blueprints.BlueprintConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Blueprints`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultThumbnail` | Default thumbnail to display on blueprints without or with invalid thumbnails |
| `ErrorIcon` | Icon for broken or invalid (but found) blueprints |
| `MaxIconSize` | Smaller sized square icon, suitable for the toolbar |
| `MaxScreenshotSizes` | Max resolution for screenshot images. Contains fallback sizes to ensure screenshot can fit within the steam upload size limits |
| `NotFoundIcon` | Icon for missing blueprints |

## A real one

`Vanilla\Assets\MainMenuData\UGC\Blueprints\BlueprintConfiguration.def`

```json
{
  "Guid": "96ed40fd-a7bc-448e-a54a-5faa5ec16d34",
  "DefaultThumbnail": "{G}b2fde0cf-cbd4-4801-b5fe-ae8af90bcf29",
  "NotFoundIcon": "{G}bee2cacf-7661-4e74-a7c4-9bbdd5f95caa",
  "ErrorIcon": "{G}b72417b1-7c64-4b6c-a587-706f6b3e45e3",
  "MaxScreenshotSizes": [
    {
      "Key": "c15aa68d-ea8f-46f1-9425-f5457a838561",
      "Value": {
        "X": 1920,
        "Y": 1080
      }
    },
    {
      "Key": "2c5e2045-3fd9-4479-a64c-2127e350030f",
      "Value": {
        "X": 1280,
        "Y": 720
      }
    },
    {
      "Key": "732f5da4-536a-4e73-9fe3-aa88d1d3c01b",
      "Value": {
        "X": 896,
        "Y": 504
      }
    },
    {
      "Key": "650cb25f-9d95-4356-9c62-153a0b077ec5",
      "Value": {
        "X": 640,
        "Y": 360
      }
    },
    {
      "Key": "27c51470-a381-4f7b-bf1e-c9a390824709",
      "Value": {
        "X": 384,
        "Y": 214
      }
    }
  ],
  "MaxIconSize": {
    "X": 200,
    "Y": 200
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlueprintConfigurationObjectBuilder')
search_content('', type_contains='BlueprintConfigurationObjectBuilder')
```
