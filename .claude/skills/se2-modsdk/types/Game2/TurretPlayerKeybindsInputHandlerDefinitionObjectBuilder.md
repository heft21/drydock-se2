# TurretPlayerKeybindsInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.TurretPlayerKeybindsInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Input\Input Adapters\TurretInputAdapter\TurretPrefabInputAdapter_TurretPlayerKeybindsInputHandlerDefinition.def`

```json
{
  "Guid": "7c0ff424-3986-47cb-8519-e26611c8258b",
  "InputContextDefinition": "c9732733-732a-4a8c-bba0-848023832b4e",
  "ScreenSelections": [
    {
      "Key": "8d7ee191-31ee-4ce5-aa4e-90cf9480720a",
      "Value": {
        "Action": "1b5b3b62-b783-4ebb-805a-8a4604bc2087",
        "Screen": {
          "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+BuildScreenSelection",
          "Panel": "Blueprints"
        }
      }
    },
    {
      "Key": "1ba9df81-d920-4aab-834e-ce25e9406976",
      "Value": {
        "Action": "ceb695dd-3bb7-4c50-8549-d99f1eb92719",
        "Screen": {
          "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+MapScreenSelection",
          "Panel": "Colonization"
        }
      }
    },
    {
      "Key": "e8251cb7-c7a0-47ca-b609-d40b4aec7de3",
      "Value": {
        "Action": "934928b6-f8dd-417f-9e92-4c50eaa46721",
        "Screen": {
          "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+GridScreenSelection",
          "Panel": "ControlPanel"
        }
      }
    },
    {
      "Key": "c5ed3e26-9a26-4f4c-ac10-69859b52fb25",
      "Value": {
        "Action": "bc29b930-0174-48ca-a3c8-1fdbc73c8b7c",
        "Screen": {
          "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+GridScreenSelection",
          "Panel": "Inventory"
        }
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TurretPlayerKeybindsInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='TurretPlayerKeybindsInputHandlerDefinitionObjectBuilder')
```
