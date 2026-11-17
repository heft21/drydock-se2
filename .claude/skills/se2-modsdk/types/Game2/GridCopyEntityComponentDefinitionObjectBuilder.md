# GridCopyEntityComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Game.EntityComponents.Toolbar.BlockPlacer.GridCopyEntityComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Game.EntityComponents.Toolbar.BlockPlacer`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\BlockPlacer\GridCopyTool.def`

```json
{
  "Guid": "b95ab35d-93be-4fb5-b80b-2027d95e5187",
  "InputContextDefinition": "9116fca6-7d1a-4f0d-8c6c-981068044cbf",
  "SizeInputContextDefinition": "d98c4658-4035-427b-877a-8720298667e8",
  "ConsumedInputKinds": [
    "Tools"
  ],
  "PassedInputKinds": [
    "Movement",
    "Rotation",
    "Interaction",
    "Utility",
    "Toolbar"
  ],
  "ConfirmStep": "3233ae1c-af85-462b-9077-ab8a51e73483",
  "CancelStep": "a329c46d-2583-4929-b695-3526980b4f7b",
  "CancelTool": "1b1ac6ed-ae92-4803-a1d9-a872902696ed",
  "ChangeSelectionSize": "62111ac9-868a-44a3-8f1d-70bb71707301",
  "ChangeSelectionSizePrecision": "0f1028bd-dd84-47bd-998c-70d06cc58b74",
  "SelectSide1": "d85f5142-0059-4a66-9754-156d12952ec5",
  "SelectSide2": "9eac2a79-3a35-47cd-b9a1-85bc1f0438a2",
  "SelectSide3": "2ad42005-1c94-480a-a603-ac86d495d81a",
  "SelectSide4": "e38118c4-3ec5-4a39-ad31-322791541d75",
  "SelectSide5": "052c2aa4-3b10-4c65-a490-7b45c4e28a1c",
  "SelectSide6": "1b37315a-7c2b-4b2a-9f7e-1b482c755714",
  "SelectionSizeSensitivity": 1,
  "MaxDistance": 1000,
  "SelectionBoxInactiveFaceColor": {
    "PackedValue": 176193664
  },
  "SelectionBoxColor": {
    "PackedValue": 350680575
  },
  "SelectionBoxOutlineColor": {
    "PackedValue": 4278230271
  },
  "SelectionBoxOutlineThickness": 2.25,
  "SelectionBoxOutlineColorBehind": {
    "PackedValue": 4294967295
  },
  "SelectionBoxOutlineThicknessBehind": 0.75,
  "SelectionBoxOutlineDashSizeBehind": 0.2,
  "CopiedBlockOutlineColor": {
    "PackedValue": 2566914303
  },
  "CopiedBlockOutlineThickness": 2,
  "SelectedBlockOutlineColor": {
    "PackedValue": 4294901760
  },
  "SelectedBlockOutlineThickness": 3,
  "SelectStartingPointHint": "SelectStartingPoint",
  "CancelToolHint": "CancelTool",
  "ConfirmSelectionHint": "ConfirmSelection",
  "CancelStartingPointHint": "SelectDifferentStartingPoint",
  "ChangeSelectionSizeHint": "SelectSize",
  "ChangeSelectionSizePrecisionHint": "SelectSizePrecision",
  "ControlGroupHint": "PartialSelectionControlGroup",
  "SideSelectionHint": "PartialSelectionToggleSides"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridCopyEntityComponentDefinitionObjectBuilder')
search_content('', type_contains='GridCopyEntityComponentDefinitionObjectBuilder')
```
