# PlayerKeybindsInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Shared`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InputContextDefinition` | Input context for all inputs in this component |
| `ScreenSelections` | When the action is pressed, the corresponding screen will be opened. If any screen is already open, the screen will be closed. |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\CharacterInputAdapter\PlayerKeybindsInputHandlerDefinition.def`

```json
{
  "Guid": "321c1b02-2eab-461d-a3bb-2fdb6d067e50",
  "InputContextDefinition": "c9732733-732a-4a8c-bba0-848023832b4e",
  "ScreenSelections": [
    {
      "Key": "9a59a3ff-60da-40dd-b3ed-d804410ab9c2",
      "Value": {
        "Action": "733786ca-552b-44dd-8de7-5e9dfed10a04",
        "Screen": {
          "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+BuildScreenSelection",
          "Panel": "Blocks"
        }
      }
    },
    {
      "Key": "f07a5e29-3aff-4c89-85f2-1a8d870b3c20",
      "Value": {
        "Action": "1b5b3b62-b783-4ebb-805a-8a4604bc2087",
        "Screen": {
          "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+BuildScreenSelection",
          "Panel": "Blueprints"
        }
      }
    },
    {
      "Key": "155cc23f-75b0-432a-bc8c-f4b411febbfe",
      "Value": {
        "Action": "bc29b930-0174-48ca-a3c8-1fdbc73c8b7c",
        "Screen": {
          "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+CharacterScreenSelection",
          "Panel": "Character"
        }
      }
    },
    {
      "Key": "ac9854c2-3312-4994-a56b-eb8a3b2d2c75",
      "Value": {
        "Action": "ceb695dd-3bb7-4c50-8549-d99f1eb92719",
        "Screen": {
          "$Type": "Game2:Keen.Game2.Client.WorldObjects.Shared.PlayerKeybindsInputHandlerDefinition+MapScreenSelection",
          "Panel": "Colonization"
        }
      }
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlayerKeybindsInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='PlayerKeybindsInputHandlerDefinitionObjectBuilder')
```
