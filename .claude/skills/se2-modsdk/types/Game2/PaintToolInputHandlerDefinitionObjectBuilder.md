# PaintToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.PaintToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CyclePaintColor` | Keybind for switching to the next/previous color in the palette |
| `OpenQuickSelectMenu` | Opens the quick painting menu |
| `PickColor` | Sets the active color to that of the targeted block |
| `SwapShipColor` | Swaps all instances of a color on a ship (including the subgrids) with the active color |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\PaintToolInputAdapter\PaintToolInputAdapter.def`

```json
{
  "Guid": "738e035f-1046-4a57-bc8d-da01f34ea038",
  "InputContextDefinition": "b2a6c6df-3932-449c-8d31-9858c4b43f4e",
  "ToolPrimary": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "ToolSecondary": null,
  "ToolTertiary": null,
  "CyclePaintColor": "39873574-65ed-4cca-881c-03a90278ca94",
  "PickColor": "4a3d5a12-1c80-4693-b18c-c4530212cde2",
  "SwapShipColor": "ba689cc1-83f3-4473-aef6-882607dd3467",
  "OpenQuickSelectMenu": "74fe4c01-4fa6-4a10-95ff-6c6a8bab08bc",
  "HintsTitle": "PaintTool",
  "OpenQuickSelectMenuHint": "PaintToolQuickMenu",
  "PickColorHint": "PaintToolPick",
  "SwapShipColorHint": "PaintToolSwapColor",
  "PaintHint": "PaintToolPaint",
  "PaintAllHint": "PaintToolPaintAll",
  "ShiftGroupHint": "PaintToolShiftGroup"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PaintToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='PaintToolInputHandlerDefinitionObjectBuilder')
```
