# GPSMarkersSessionComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.GPS.GPSMarkersSessionComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.GPS`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArrowIcon` | Icon to use when a marker is outside of screen |
| `BunchColor` | Color for bunched markers |
| `BunchIcon` | Icon to use when markers are bunched |
| `EllipseHeight` | The height of the ellipse which is used to project markers on screen. |
| `EllipseHorizontalOffset` | Horizontal offset of the ellipse which is used to project markers on screen. |
| `EllipseVerticalOffset` | Vertical offset of the ellipse which is used to project markers on screen. For example, we don't want to project markers at the bottom of the screen because of the toolbar would obstruct them. |
| `EllipseWidth` | The width of the ellipse which is used to project markers on screen. |
| `FocusFontSize` | Font size when marker is in focus. |
| `FocusedBunchMaxMarkers` | Amount of markers to display when markers are bunched together and in focus. |
| `Font` | Font to use to render GPS markers. |
| `MarkersBunchingScreenDistance` | Distance between markers in screen percentage under which markers will be bunched together. |
| `OutsideScreenFontSize` | Font size when marker is outside of screen. |
| `RegualarFontSize` | Regular font size. |
| `ShortBunchMaxMarkers` | Amount of markers to display when markers are bunched together. |
| `TextShadowOffset` | Offset of the text shadow defined as portion of the vertical screen size |

## A real one

`Vanilla\Assets\System\Session\World_GpsMarkersSessionComponentDefinition.def`

```json
{
  "Guid": "7346601e-d0be-49a0-8778-fa57dcb6017d",
  "Font": "0c519c1d-22ea-49ea-b82c-70e3a937f193",
  "RegualarFontSize": 0.65,
  "OutsideScreenFontSize": 0.55,
  "FocusFontSize": 0.7,
  "MarkersBunchingScreenDistance": 0.04,
  "ShortBunchMaxMarkers": 10,
  "FocusedBunchMaxMarkers": 20,
  "EllipseVerticalOffset": 0.15,
  "EllipseHorizontalOffset": 0.1,
  "EllipseHeight": 0.9,
  "EllipseWidth": 0.9,
  "ArrowIcon": "{G}9aed98e1-5034-4359-80a7-90d1be02d621",
  "BunchIcon": "{G}29415b69-2eb9-4bf3-bb55-717e67842575",
  "BunchColor": {
    "PackedValue": 4289702014
  },
  "TextShadowOffset": 0.0015
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GPSMarkersSessionComponentDefinitionObjectBuilder')
search_content('', type_contains='GPSMarkersSessionComponentDefinitionObjectBuilder')
```
