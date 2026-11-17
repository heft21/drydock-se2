# GPSMarkersConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.GPS.GPSMarkersConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.GPS`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Colors` | Possible colors for markers |
| `DefaultColor` | Default color to use when no color is specified |
| `DefaultIcon` | Icon to use when no icon is specified |
| `DescriptionMaxLength` | Maximum length of marker description |
| `FullDisplayMarkerTypes` | GPS Types that will be always fully visible and will not be grouped together. |
| `GenericGPSAudio` | A generic one-shot sound that can be used for various GPS-related actions. |
| `GroupNameKey` | Key Group text |
| `Icons` | Possible icons for markers |
| `NameMaxLength` | Maximum length of marker name |
| `NewMarkerDialogNameKey` | Default marker name in dialog screen |
| `OnCreateMarkerAudio` | Played upon creating a GPS marker. |
| `OnDeleteMarkerAudio` | Played upon deleting a GPS marker. |
| `OnHideMarkerAudio` | Played on GPS marker hide. |
| `OnShareMarkerAudio` | Played upon sharing a GPS marker. |
| `OnShowMarkerAudio` | Played on GPS marker show. |
| `OnSortMarkersAudio` | Played on sorting GPS markers. |
| `PlayerBackpackColor` | Default color for player backpack spawned on death |
| `PlayerBackpackIcon` | Default icon for player backpack spawned on death |
| `PlayerBackpackMarkerType` | This type is used for spawning player backpacks on death |
| `PlayerCreatedMarkerIcon` | Icon to use when player creates GPS marker |
| `PlayerMadeMarkerType` | This type is used for creating user markers |
| `SortDistanceKey` | Key of sort by Distance text |
| `SortNameKey` | Key of sort by Name text |

## A real one

`Vanilla\Assets\System\Configurations\GPSMarkersConfiguration.def`

```json
{
  "Guid": "ab128087-07a3-4360-aad3-ef5ad65f59f8",
  "DefaultIcon": "{G}d5af2a12-1508-4046-944f-fccf44723e9e",
  "PlayerCreatedMarkerIcon": "{G}3028b8a5-ea46-402a-9317-ee0cadc8a87d",
  "Icons": [
    {
      "Key": "86e7855a-ad7f-4f48-a7ae-a7eb5ae4e090",
      "Value": "{G}d5af2a12-1508-4046-944f-fccf44723e9e"
    },
    {
      "Key": "74779889-ff0a-4138-8df2-13bc64b98957",
      "Value": "{G}3028b8a5-ea46-402a-9317-ee0cadc8a87d"
    }
  ],
  "DefaultColor": {
    "PackedValue": 4279077600
  },
  "Colors": [],
  "PlayerMadeMarkerType": "d648e558-2e34-4b80-9d58-5bd678c4db18",
  "PlayerBackpackMarkerType": "8c49fa4e-7111-44f1-9cda-7ea89abaab2a",
  "PlayerBackpackColor": {
    "PackedValue": 4282400956
  },
  "PlayerBackpackIcon": "{G}6f7b8023-bc20-4ff3-b289-392552a16a07",
  "BlockMarker": "fb0df784-eb2d-4e5c-a7a9-8119f6399501",
  "FullDisplayMarkerTypes": [
    "3d5ca81c-5453-4012-869e-e7c07080b5d3",
    "3399d226-1713-49e5-82d2-9ba3a8c9ce89"
  ],
  "NameMaxLength": 50,
  "DescriptionMaxLength": 250,
  "SortNameKey": "SortName",
  "SortDistanceKey": "SortDistance",
  "GroupNameKey": "GroupNameKey",
  "ToggleGroupKey": "MapScreenToggleGroup",
  "ToggleGroupDisabledKey": "MapScreenToggleGroupDisabled",
  "NewMarkerDialogNameKey": "NewMarkerDialogText",
  "PersonalMarkersCategoryKey": "MapScreenPersonalMarkersCategory",
  "SystemMarkersCategoryKey": "MapScreenSystemMarkersCategory",
  "DeadBackpackGroupKey": "MapScreenDeadBackpackGroup",
  "ContractsGroupKey": "MapScreenContractsGroup",
  "FastTravelGroupKey": "MapScreenFastTravelGroup",
  "MarkerNameKey": "Name",
  "CoordinatesKey": "GPSScreenCoordinates",
  "AxisXKey": "AxisX",
  "AxisYKey": "AxisY",
  "AxisZKey": "AxisZ",
  "OnCreateMarkerAudio": "event:/UI/gps_create",
  "OnDeleteMarkerAudio": "event:/UI/gps_delete",
  "OnShowMarkerAudio": "event:/UI/gps_show",
  "OnHideMarkerAudio": "event:/UI/gps_hide",
  "OnSortMarkersAudio": "event:/UI/gps_sort",
  "OnShareMarkerAudio": "event:/UI/gps_share",
  "GenericGPSAudio": "event:/UI/gps_generic"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GPSMarkersConfigurationObjectBuilder')
search_content('', type_contains='GPSMarkersConfigurationObjectBuilder')
```
