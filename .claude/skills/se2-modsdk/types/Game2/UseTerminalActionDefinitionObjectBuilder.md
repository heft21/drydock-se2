# UseTerminalActionDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Interaction.UseTerminalActionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Interaction`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PrimaryScreen` | The screen that will be opened when is activated. |
| `SecondaryScreen` | The screen that will be opened when is activated. |

## A real one

`Vanilla\Assets\System\UseActions\UseConveyorAction.def`

```json
{
  "Guid": "d3f7336c-2ed2-4903-ac01-1aacbcfd931f",
  "UseActionType": "Game2:Keen.Game2.Client.GameSystems.Interaction.UseConveyorAction",
  "HighlightText": "UseConveyor",
  "InputContextDefinition": "121f3ef3-bff0-45c6-bcb9-606f9966462b",
  "InteractPrimary": "72e61d01-ce14-41e2-968c-6518a35e5235",
  "InteractSecondary": "6207a6e9-aec1-47cd-a99f-7f7e19ca01f4",
  "DepositNonEssentialItems": "4fa398a2-1750-4399-bf4a-5b118e636398",
  "HighlightEffect": "9c36070a-6bad-40dc-9dc7-a8514e5e8657",
  "WorkWhenDisabled": true,
  "RequireFacingPlayer": false,
  "Inflation": {
    "X": -0.025,
    "Y": -0.025,
    "Z": 0
  },
  "PrimaryScreen": {
    "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+GridScreenSelection",
    "Panel": "Inventory"
  },
  "SecondaryScreen": {
    "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+GridScreenSelection",
    "Panel": "ControlPanel"
  }
}
```

Others: `UseTerminalAction`, `UseFloatingContainerAction`

---

Read it with the MCP server rather than by hand:

```
describe_type('UseTerminalActionDefinitionObjectBuilder')
search_content('', type_contains='UseTerminalActionDefinitionObjectBuilder')
```
