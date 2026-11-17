# ConsumablesToolDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.ConsumablesToolDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumedInputKinds` | Inputs consumed by component |
| `InputContext` | Input context for the tool |
| `PassedInputKinds` | Inputs ignored/passed-through by component |
| `TooltipText` | Localization keys for control hints tooltip title text |
| `UseConsumable` | Input action to use the selected consumable |
| `UseConsumableLocKey` | Localization key for the use control hint. Format keys: consumable. |

## A real one

`Vanilla\Assets\System\Tools\ConsumablesToolDefinition.def`

```json
{
  "Guid": "7a9971e1-aeaf-43d4-a44d-3e3c31e71d72",
  "InputContext": "ac1f3108-b609-459a-a3b0-c385f34b7252",
  "UseConsumable": "c368e556-5145-47be-b9bf-8f37212c495d",
  "UseConsumableLocKey": "ConsumablesToolUseConsumable",
  "ConsumedInputKinds": [
    "Tools"
  ],
  "PassedInputKinds": [
    "Movement",
    "Rotation",
    "Interaction",
    "Toolbar",
    "Utility"
  ],
  "TooltipText": "ConsumablesToolTooltipText"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ConsumablesToolDefinitionObjectBuilder')
search_content('', type_contains='ConsumablesToolDefinitionObjectBuilder')
```
