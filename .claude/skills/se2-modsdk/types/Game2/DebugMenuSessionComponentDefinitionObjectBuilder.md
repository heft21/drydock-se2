# DebugMenuSessionComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.Debugging.DebugMenuSessionComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.Debugging`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DebugMenuViewToggle` | Input for toggling debug menu (F12) |
| `InputContextDefinition` | DebugMenu input context |

## A real one

`Vanilla\Assets\MainMenuData\UI\DebugMenu.def`

```json
{
  "Guid": "c4e3d293-3c21-47a5-9be8-4e4cc9e54e4d",
  "InputContextDefinition": "d8974fc1-41bb-4bce-9ee1-eea5c6f649ea",
  "DebugMenuViewToggle": "6c09496f-9e1b-46e0-8ef1-f7e482fd17a1"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DebugMenuSessionComponentDefinitionObjectBuilder')
search_content('', type_contains='DebugMenuSessionComponentDefinitionObjectBuilder')
```
