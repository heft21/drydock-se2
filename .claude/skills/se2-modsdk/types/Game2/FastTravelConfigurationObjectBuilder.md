# FastTravelConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.FastTravel.FastTravelConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.FastTravel`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FastTravelCountDown` | How much time fast travel should wait before teleporting the entities. |
| `FastTravelFadingIn` | Fading in and out from the video. |
| `FastTravelFadingOut` | Fading in and out from the video. |
| `FastTravelMinimumDuration` | Minimal time before teleporting the entities when travel is confirmed. |
| `FastTravelVideos` | Videos to play when fast travel is confirmed. |
| `FieldPrefab` | Prefab that represent a fast travel field. |
| `GPSMarkerColor` | Color of the GPS marker. |
| `GPSMarkerColorInRange` | Color of the GPS marker. |
| `GPSMarkerIcon` | Icon used on the GPS marker. |
| `GPSMarkerType` | Type definition of the GPS marker that indicate fast travel fields. |
| `SectorNotReleasedNotificationContent` | Content of notification shown when destination sector is not released. |
| `SectorNotReleasedNotificationTitle` | Title of notification shown when destination sector is not released. |

## A real one

`Vanilla\Assets\System\FastTravel\FastTravelConfiguration.def`

```json
{
  "Guid": "a92c5c16-1bb1-4ecf-b601-1e2664232afe",
  "FieldPrefab": "c39ba103-7694-455a-a897-a16e2a19e509",
  "FastTravelCountDown": 29999997,
  "FastTravelMinimumDuration": 20000000,
  "FastTravelFadingIn": 20000000,
  "FastTravelFadingOut": 5000000,
  "FastTravelVideos": [
    {
      "Key": "e6369ab7-8c81-4164-891e-64e72c7e17ce",
      "Value": "{G}e6d4c0cf-f35e-40e6-aa19-3ce3773f1bbf"
    }
  ],
  "GPSMarkerType": "f7bbe85a-46b7-41de-a5ff-af6303f6676b",
  "GPSMarkerIcon": "{G}4e98fbe5-ad79-4ac2-9534-6d5c29e57df1",
  "GPSMarkerColor": {
    "PackedValue": 4294967295
  },
  "GPSMarkerColorInRange": {
    "PackedValue": 4289507910
  },
  "SectorNotReleasedNotificationTitle": "SectorUnreleasedTitle",
  "SectorNotReleasedNotificationContent": "SectorUnreleasedText"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FastTravelConfigurationObjectBuilder')
search_content('', type_contains='FastTravelConfigurationObjectBuilder')
```
