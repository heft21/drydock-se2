# DrillDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AutoConversions` | After mining, this collection is probed for conversion, should there be a match on input side, the output items are produced instead. Only fractional items are expected, so that any amount can be converted. Conversions are instant. |
| `DetectionArgs` | Target entity detection settings |
| `DropOreAsFallback` | When true, an ore item will spawn when the inventory is full. Otherwise the items will be lost |
| `PrimaryActionDummy` | Primary brush offset transform. |
| `PrimaryBrushShape` | Brush shape used by primary tool action. |
| `PrimaryDrillingTimeModifier` | Multiplier applied on drill time associated to the material of the current drill target. 1 is standard rate. Less means faster drilling, more slower drilling. Applies to primary tool action. |
| `SecondaryActionDummy` | Secondary brush offset transform. |
| `SecondaryBrushShape` | Brush shape used by secondary tool action. |
| `SecondaryDrillingTimeModifier` | Multiplier applied on drill time associated to the material of the current drill target. 1 is standard rate. Less means faster drilling, more slower drilling. Applies to secondary tool action. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DrillDefinition.def`

```json
{
  "Guid": "f2fddbc5-562d-4c37-99ff-76d3734a33b9",
  "DetectionArgs": {
    "DetectDummies": false,
    "UsePreciseColliderForBlocks": false,
    "DetectChildEntities": false,
    "DetectTopMostEntities": true,
    "DetectProjections": false,
    "Frequency": 15,
    "Occlusion": true,
    "FirstHit": true,
    "AllowDuplication": false,
    "DummyOcclusionEpsilon": 0,
    "LayerFilter": "58e106fe-ab5e-4e66-a9b8-10fd46ba786d"
  },
  "PrimaryActionDummy": "8f20b1ae-4081-48fc-8b3a-8c7846af1a98",
  "PrimaryDrillingTimeModifier": 1,
  "SecondaryActionDummy": "3ecafef7-62ee-40e0-ba00-46d1d089934e",
  "SecondaryDrillingTimeModifier": 0.5,
  "PrimaryBrushShape": null,
  "SecondaryBrushShape": null,
  "DropOreAsFallback": true,
  "AutoConversions": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DrillDefinitionObjectBuilder')
search_content('', type_contains='DrillDefinitionObjectBuilder')
```
