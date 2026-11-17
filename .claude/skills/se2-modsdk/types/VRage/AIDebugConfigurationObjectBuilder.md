# AIDebugConfigurationObjectBuilder

`VRage:Keen.VRage.AI.Definitions.AIDebugConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.AI.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AIDebugCameraObserverTag` | Observer tag used by AI to access camera transform. |

## A real one

`Vanilla\Assets\System\Configurations\AiConfiguration.def`

```json
{
  "Guid": "29255fc7-59d0-43f9-bd03-126d182b4171",
  "AIDebugCameraObserverTag": "AICameraObserver"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AIDebugConfigurationObjectBuilder')
search_content('', type_contains='AIDebugConfigurationObjectBuilder')
```
