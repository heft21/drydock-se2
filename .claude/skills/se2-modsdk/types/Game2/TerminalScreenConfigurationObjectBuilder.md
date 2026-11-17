# TerminalScreenConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.TerminalScreen.TerminalScreenConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.TerminalScreen`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CopyTooltip` | Copy block settings tooltip |
| `DoubleClickTime` | Maximum ticks that can elapse between two clicks to register as a double click in terminal |
| `GridSelectionTitle` | Title of the Selection when a Grid (root node) is Selected |
| `GroupSelectionDescription` | Description of the selection when a Group is Selected |
| `GroupSelectionTitle` | Title of the Selection when a Group is Selected |
| `MixedSelectionTitle` | Title of the Selection when grids are mixed with blocks |
| `MultiSelectionTitle` | Title of the Selection when Multiples blocks is Selected |
| `MultipleBlockTypesTooltip` | Multiple block types selected Tooltip |
| `MultipleBlocksSelectedTooltip` | Multiple blocks selected tooltip |
| `NoClipboardTooltip` | No Clipboard data Tooltip |
| `NoSelectionTooltip` | No-Selection Tooltip |
| `PasteTooltip` | Paste block settings tooltip |

## A real one

`Vanilla\Assets\UI\Screens\TerminalScreenConfiguration.def`

```json
{
  "Guid": "226a55d3-3faf-44ff-b5fc-7739e2a0933f",
  "DoubleClickTime": 250,
  "GroupSelectionTitle": "TerminalScreenGroupSelectionTitle",
  "GroupInspectorTitle": "TerminalScreenGroupInspectorTitle",
  "MultiSelectionTitle": "TerminalScreenMultiSelectionTitle",
  "MixedSelectionTitle": "TerminalScreenMixedSelectionTitle",
  "GridSelectionTitle": "TerminalScreenGridSelectionTitle",
  "GroupSelectionDescription": "TerminalScreenGroupSelectionDescription",
  "GroupInspectorDescription": "TerminalScreenGroupInspectorDescription",
  "CopyTooltip": "TerminalScreenCopy",
  "NoSelectionTooltip": "TerminalScreenNoSelection",
  "MultipleBlocksSelectedTooltip": "TerminalScreenMultipleBlocksSelected",
  "PasteTooltip": "TerminalScreenPaste",
  "NoClipboardTooltip": "TerminalScreenNoClipboard",
  "MultipleBlockTypesTooltip": "TerminalScreenMultipleBlockTypesSelected",
  "CharacterTabKey": "TerminalScreenHeaderCharacter",
  "GridTabKey": "TerminalScreenHeaderGrid",
  "BuildTabKey": "TerminalScreenHeaderBuild",
  "ContractsTabKey": "TerminalScreenHeaderContracts",
  "TradeTabKey": "TerminalScreenHeaderTrade",
  "SocialTabKey": "TerminalScreenHeaderSocial",
  "MapTabKey": "TerminalScreenHeaderMap",
  "InventorySubtabKey": "TerminalScreenHeaderInventory",
  "DatapadSubtabKey": "TerminalScreenHeaderDatapads",
  "QuestItemsSubtabKey": "TerminalScreenHeaderQuestItems",
  "BlockSchematicsSubtabKey": "TerminalScreenHeaderBlockSchematics",
  "CharacterInventorySubtabKey": "TerminalScreenHeaderInventory",
  "ControlPanelSubtabKey": "TerminalScreenHeaderControlPanel",
  "ProductionSubtabKey": "TerminalScreenHeaderProduction",
  "InfoSubtabKey": "TerminalScreenHeaderInfo",
  "FactionsSubtabKey": "TerminalScreenHeaderFactions",
  "BlueprintsSubtabKey": "Blueprints",
  "BlocksSubtabKey": "TerminalScreenHeaderBlocks",
  "ContractsSubtabKey": "TerminalScreenHeaderContractsBlock",
  "TradeBlockSubtabKey": "TerminalScreenHeaderTradeBlock",
  "ColonizationSubtabKey": "TerminalScreenHeaderMapColonization",
  "GPSMarkersSubtabKey": "TerminalScreenHeaderMapGPSMarkers",
  "PlayersSubtabKey": "TerminalScreenHeaderMapPlayersMarkers",
  "HideToggleTooltipKey": "ControlPanelHideToggleTooltipKey",
  "ShowToggleTooltipKey": "ControlPanelShowToggleTooltipKey"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TerminalScreenConfigurationObjectBuilder')
search_content('', type_contains='TerminalScreenConfigurationObjectBuilder')
```
