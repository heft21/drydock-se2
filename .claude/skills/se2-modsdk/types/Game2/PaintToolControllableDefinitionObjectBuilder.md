# PaintToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.PaintToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BrushSizes` | Selections of different brush sizes for UI |
| `HoverBrushSizes` | Selections of different hovered brush sizes for UI |
| `MaxPaintDistance` | Max length of the paint ray |
| `PaintGridHoldTime` | The amount of time needed to hold paint on a block until the entire grid gets painted |
| `QuickMenuDefinition` | Definition for opening the quick menu |

## A real one

`Vanilla\Assets\CharacterTools\PaintGun\PaintToolControllableDefinition.def`

```json
{
  "Guid": "cc5499ce-44ce-4893-acca-aa7eda1e77fe",
  "QuickMenuDefinition": "183da096-9d49-4d8c-9954-7c00153ed90e",
  "MaxPaintDistance": 100,
  "PaintGridHoldTime": 40000000,
  "BrushSizes": {
    "0": "{G}9d185db6-e06b-455d-af7c-dc129513386c",
    "2": "{G}5abd51d9-9638-4c40-9b74-59eaf1d9cdda",
    "5": "{G}17771b06-4f77-4f6c-b509-c38698dc24ed"
  },
  "HoverBrushSizes": {
    "0": "{G}9d185db6-e06b-455d-af7c-dc129513386c",
    "2": "{G}5abd51d9-9638-4c40-9b74-59eaf1d9cdda",
    "5": "{G}17771b06-4f77-4f6c-b509-c38698dc24ed"
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PaintToolControllableDefinitionObjectBuilder')
search_content('', type_contains='PaintToolControllableDefinitionObjectBuilder')
```
