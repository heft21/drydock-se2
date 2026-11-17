# CockpitControllableComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Cockpit.CockpitControllableComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Cockpit`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConsumedInputKinds` | InputKinds consumed by cockpit |
| `InputHandlerSpecificKey` | Optional name of specific input adapter to request by this controllable. |
| `PassedInputKinds` | InputKinds forwarded to other controllers further down the stack |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ControllableSeatComponent.def`

```json
{
  "Guid": "81e8ecc9-a40d-43a9-b4f6-d20f5891ce4a",
  "InputHandlerSpecificKey": null,
  "ConsumedInputKinds": [
    "Movement",
    "Rotation",
    "Utility",
    "Toolbar"
  ],
  "PassedInputKinds": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CockpitControllableComponentDefinitionObjectBuilder')
search_content('', type_contains='CockpitControllableComponentDefinitionObjectBuilder')
```
