# InventoryOccupancyLcdDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Lcd.InventoryOccupancyLcdDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Lcd`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Blocks\Contracts\ContractsTerminal\250\ContractBlock250_InventoryOccupancyLcdDefinition.def`

```json
{
  "Guid": "c1797b0a-44a1-44ea-95ab-b6e9c6d736de",
  "SurfaceIndex": 0,
  "Text": {
    "RawText": "{Loc:RewardAvailable}"
  },
  "FontSize": 80,
  "HorizontalAlignment": "Center",
  "VerticalAlignment": "Top",
  "TextColor": {
    "PackedValue": 4278242559
  },
  "BackgroundColor": {
    "PackedValue": 4279504655
  },
  "Images": [],
  "ImageIntervalSeconds": 1,
  "Padding": 20
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryOccupancyLcdDefinitionObjectBuilder')
search_content('', type_contains='InventoryOccupancyLcdDefinitionObjectBuilder')
```
