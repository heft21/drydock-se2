# ToolCameraShakeDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.ToolCameraShakeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ActiveShakePower` | Camera shake power to deliver while tool is active (firing) |
| `IdleShakePower` | Camera shake power to deliver while tool is equipped but idle (not being used actively) |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\GrinderTool_Client_ToolCameraShakeDefinition.def`

```json
{
  "Guid": "bb3ea4cb-7b83-4c8c-8c4d-bf2500bb258b",
  "IdleShakePower": 0,
  "ActiveShakePower": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ToolCameraShakeDefinitionObjectBuilder')
search_content('', type_contains='ToolCameraShakeDefinitionObjectBuilder')
```
