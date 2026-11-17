# UseToolbarSlotActionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseToolbarSlotActionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActivateSlotText` | Text shown when the slot has an action. |
| `InvalidSubtext` | Subtext used when the toolbar action is invalid |
| `NoActionAssignedSubtext` | Subtext used when there is no action in the slot. |
| `ToolbarGroupIndex` | What group the slot is in, 0-based. |
| `ToolbarTag` | Which toolbar component on the block this action targets |

## A real one

`Vanilla\Assets\System\UseActions\UseToolbarSlotActionDefinition.def`

```json
{
  "Guid": "48f189e1-94fb-4005-9350-37afb5384015",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UseToolbarSlotAction",
  "HighlightText": "UseTerminal",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": null,
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "WorkWhenDisabled": false,
  "PrimaryScreen": {
    "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+GridScreenSelection",
    "Panel": "ControlPanel"
  },
  "SecondaryScreen": null,
  "ActivateSlotText": "UseToolbarSlot",
  "NoActionAssignedSubtext": "ToolbarActionHintUnassigned",
  "InvalidSubtext": "ToolbarActionHintInvalid",
  "ToolbarGroupIndex": 0,
  "ToolbarTag": "BlockToolbarServerComponent"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('UseToolbarSlotActionDefinitionObjectBuilder')
search_content('', type_contains='UseToolbarSlotActionDefinitionObjectBuilder')
```
