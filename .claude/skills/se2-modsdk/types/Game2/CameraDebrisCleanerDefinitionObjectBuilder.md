# CameraDebrisCleanerDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.CameraDebrisCleanerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TriggerRadius` | Radius within debris is removed |

## A real one

`Vanilla\Assets\System\Camera\RenderCamera\PrefabRenderCamera_CameraDebrisCleanerDefinition.def`

```json
{
  "Guid": "568edb8c-bb44-4ad8-a359-928d86a7c1fc",
  "TriggerRadius": 0.1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CameraDebrisCleanerDefinitionObjectBuilder')
search_content('', type_contains='CameraDebrisCleanerDefinitionObjectBuilder')
```
