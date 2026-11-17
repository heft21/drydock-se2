# ToolbarInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.ToolbarInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **3**

## What it is

Object builder for

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InputContextDefinition` | Definition for input context for all Toolbar input actions |
| `QuickMenuDefinition` | Definition carrying input actions for the quick menu |
| `ShowPCU` | When true, the PCU will be shown with the toolbar hud |
| `ToggleRadialMenu` | Input action to show/hide the quick menu |
| `ToggleToolbars` | Input action to switch to the next toolbar |
| `Toolbars` | List of individual toolbar "tabs" and their content |
| `UnequipOnDeactivate` | Whether the toolbar should unequip tools from hand when toolbar is deactivated. If true, tool will be unequipped as if it was never equipped. If false, tool will stay in hands until toolbar reactivates or outside force destroys the tool. |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\CharacterToolbarInputAdapter.def`

```json
{
  "Guid": "e0ccba9c-3131-456c-8683-b841a58d91a8",
  "QuickMenu": {
    "RootMenu": {
      "Panels": [],
      "MiddlePanel": {
        "$Type": "Game2:Keen.Game2.Client.UI.Library.Controls.RadialMenu.BaseRadialMenuPanel",
        "DisplayName": "ToolbarInputAdapterBlank",
        "Icon": "{G}71a48d07-f9a7-42a8-b06b-39796d7c81e3",
        "HoverIcon": null,
        "IsEnabled": true
      }
    }
  },
  "InputContextDefinition": "81cd1c0e-02fd-4da9-8bf1-72bb1a7d9b0d",
  "ToggleToolbars": "d633f215-b69f-436c-97eb-0597d2dc5473",
  "ToggleRadialMenu": "6d30c631-c13b-43c9-a540-f063795abf25",
  "Toolbars": [
    {
      "Key": "c06ed0bb-61a5-498c-90cc-90531991d3e0",
      "Value": {
        "Toolbar": "cda531ec-1b7c-4c2d-aa5d-380bf1de599e",
        "AllowAutoselectWhenOpened": true
      }
    },
    {
      "Key": "e6bde937-6b6d-48ab-84bb-1b9d949683ae",
      "Value": {
        "Toolbar": "bc111f4c-3071-4567-9c32-56a3649e6018",
        "AllowAutoselectWhenOpened": false
      }
    }
  ],
  "QuickMenuDefinition": "183da096-9d49-4d8c-9954-7c00153ed90e",
  "UnequipOnDeactivate": false
}
```

Others: `SpectatorToolbarInputAdapter`, `CockpitToolbarInputHandlerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolbarInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='ToolbarInputHandlerDefinitionObjectBuilder')
```
