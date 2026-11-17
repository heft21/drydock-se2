# CubeGridThirdPersonAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Adapters.CubeGridThirdPersonAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Adapters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DummyType` | Model dummy used for offsetting the camera. |

## A real one

`Vanilla\Assets\System\Camera\AnyGridThirdPersonCamera\CubeGridThirdPersonAdapterDefinition.def`

```json
{
  "Guid": "8867124e-01be-47a4-8d5b-259639a50962",
  "DummyType": "2f0f6710-3dc2-4ecb-bcc6-0719ad23bd07"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeGridThirdPersonAdapterDefinitionObjectBuilder')
search_content('', type_contains='CubeGridThirdPersonAdapterDefinitionObjectBuilder')
```
