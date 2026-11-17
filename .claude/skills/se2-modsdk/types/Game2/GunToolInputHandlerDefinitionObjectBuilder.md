# GunToolInputHandlerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers.GunToolInputHandlerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PlayerControl.PlayerInput.InputHandlers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GunReload` | Input for gun reload action |
| `ReloadHint` | Hint shown for action |
| `ToolPrimaryHint` | Hint shown for action |
| `ToolSecondaryHint` | Hint shown for action |

## A real one

`Vanilla\Assets\System\Input\Input Adapters\GunToolInputAdapter\GunToolInputAdapterDefinition.def`

```json
{
  "Guid": "d02c12ef-9c49-471a-89f7-a4dcdac7cd1c",
  "InputContextDefinition": "5c45f08f-6517-456d-a971-449eedba56f2",
  "ToolPrimary": "7dff0428-9066-423e-abb6-0561ffe02ce1",
  "ToolSecondary": "f1789abd-986b-464a-9c2a-7ebd13c53c25",
  "ToolTertiary": null,
  "GunReload": "ef513d1b-5abf-44b3-9f41-10c354610a33",
  "ToolPrimaryHint": "GunShoot",
  "ToolSecondaryHint": "GunADS",
  "ReloadHint": "ReloadGunTool"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GunToolInputHandlerDefinitionObjectBuilder')
search_content('', type_contains='GunToolInputHandlerDefinitionObjectBuilder')
```
