# InputGameComponentConfigurationObjectBuilder

`Game2:Keen.Game2.Client.Input.InputGameComponentConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.Input`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CloseStats` | Input action to close the render stats |
| `CycleStats` | Input action to cycle through the various render stats pages |
| `Exit` | Input action to exit game |
| `InputContextDefinition` | Settings of the created during initialization of |
| `LoadGame` | Input action for invoking (when set) |
| `OpenDebugMenu` | Action to open debug menu (F12) |
| `OpenHelpScreen` | Input action to open the help screen |
| `ReloadShaders` | Input action to force shaders to reload |

## A real one

`Vanilla\Assets\MainMenuData\Input\ComponentInputGame.def`

```json
{
  "Guid": "3dc0ab11-87e8-474f-b16d-55f487acc5c6",
  "InputContextDefinition": "bcae898b-6256-4bb6-ba4e-6d6628d5a4f1",
  "Exit": "40e063ce-f36e-446e-9841-b4e6efd14c93",
  "LoadGame": "daa13213-b3ee-4d0b-8243-72ca9f3b17e9",
  "CycleStats": "d52deec7-373f-4ad0-96c0-65b4fbc3cc49",
  "CloseStats": "3b404970-6564-4f0c-a0db-a0442e62f435",
  "ReloadShaders": "feba2e7b-b552-4f23-b5fe-96f3881ebed2",
  "CaptureOptick": "13689757-49a4-4785-af39-9890cf356b8d",
  "OpenHelpScreen": "2750799c-8031-4a4f-b599-9030c65ff5b3",
  "OpenDebugMenu": "6c09496f-9e1b-46e0-8ef1-f7e482fd17a1"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InputGameComponentConfigurationObjectBuilder')
search_content('', type_contains='InputGameComponentConfigurationObjectBuilder')
```
