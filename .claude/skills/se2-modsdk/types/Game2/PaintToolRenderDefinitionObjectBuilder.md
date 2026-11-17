# PaintToolRenderDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.PaintToolRenderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AddedWidth` | The amount of width to add to the circle's radius, so a radius of 0 is still visible |
| `HighlightColor` | An override of the outline color when drawing the paint grid highlight When null, the active paint color will be used |
| `HighlightCornerLengthRatio` | When drawing the paint grid highlight, the length of the corner lines relative to the minimum extent of the grid |
| `HighlightDotsCount` | Amount of dots/dashes along the outline edges when drawing the paint grid highlight. Doesn't draw any when zero |
| `HighlightDotsSize` | Size of the dots along the outline edges of the paint grid highlight |
| `HighlightThickness` | Thickness of the lines when drawing the paint grid highlight |
| `MinPaintGridCountdown` | Minimum amount of time the paint grid action must be held before the countdown text shows Used to prevent flashing text when painting in strokes |
| `ShrinkDistance` | When the circle is closer to the camera than this distance, start shrinking the added width down, in order for a radius 0 "dot" to not be too big on screen |
| `SphereModel` | Model of the sphere paint brush |

## A real one

`Vanilla\Assets\CharacterTools\PaintGun\PaintToolRenderDefinition.def`

```json
{
  "Guid": "20731b3e-e94f-40c7-9870-e1ceaeebb100",
  "HighlightColor": null,
  "HighlightThickness": 0.5,
  "AddedWidth": 0.1,
  "ShrinkDistance": 0.5,
  "HighlightDotsCount": 7,
  "HighlightDotsSize": 3.5,
  "HighlightCornerLengthRatio": 0.5,
  "MinPaintGridCountdown": 8000000,
  "SphereModel": "{G}b385f984-e69b-41c5-9a02-bfdc1e147db2"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PaintToolRenderDefinitionObjectBuilder')
search_content('', type_contains='PaintToolRenderDefinitionObjectBuilder')
```
