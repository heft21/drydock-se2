# InputContextDefinitionObjectBuilder

`VRage:Keen.VRage.Input.InputContextDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Input`
- definitions using it: **44**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Actions` | A set of input actions that this context can handle. |
| `CaptureAllInput` | Indicates whether this context captures all input reaching its stack level. When enabled, no input from the below layers is passed to the next context unless explicitly allowed. |
| `Layer` | Specifies the input context's layer for grouping or categorization purposes. |
| `Name` | A developer-friendly name for this input context, primarily used for debugging. NOTE: Use unique names to avoid ambiguity during debugging. |
| `PassthroughActions` | A set of input actions that bypass and are passed through to the next context. |

## A real one

`Vanilla\Assets\MainMenuData\Input\Inputs\UiContext.def`

```json
{
  "Guid": "bcae898b-6256-4bb6-ba4e-6d6628d5a4f1",
  "Name": "UI",
  "Layer": "UI",
  "CaptureAllInput": false,
  "PassthroughActions": [],
  "Actions": [
    "daa13213-b3ee-4d0b-8243-72ca9f3b17e9",
    "40e063ce-f36e-446e-9841-b4e6efd14c93",
    "d52deec7-373f-4ad0-96c0-65b4fbc3cc49",
    "feba2e7b-b552-4f23-b5fe-96f3881ebed2",
    "9ea5c1e6-22a9-4102-9734-1b0ee9287736",
    "2750799c-8031-4a4f-b599-9030c65ff5b3",
    "6c09496f-9e1b-46e0-8ef1-f7e482fd17a1",
    "3b404970-6564-4f0c-a0db-a0442e62f435",
    "13689757-49a4-4785-af39-9890cf356b8d"
  ]
}
```

Others: `MenuContext`, `ToolContext`

---

Read it with the MCP server rather than by hand:

```
describe_type('InputContextDefinitionObjectBuilder')
search_content('', type_contains='InputContextDefinitionObjectBuilder')
```
