# ToolControllableDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.ToolControllableDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumedInputKinds` | InputKinds consumed by |
| `InputHandlerSpecificKey` | Optional name of input adapter to request for this controller. |
| `PassedInputKinds` | InputKinds passed by to other controllers further down the stack |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\ToolControllable.def`

```json
{
  "Guid": "bf318288-9b1f-4278-bd24-73d57114759c",
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
  "InputHandlerSpecificKey": ""
}
```

Others: `ToolControllableGun`, `ToolControllablePaintGun`

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolControllableDefinitionObjectBuilder')
search_content('', type_contains='ToolControllableDefinitionObjectBuilder')
```
