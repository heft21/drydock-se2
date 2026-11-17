# EditorObserverConfigurationObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.Observers.EditorObserverConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.Observers`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CameraObserverDefinitionDebugName` | Debug name to look for in DebugName for camera observer tags |

## A real one

`Engine\Assets\Core\EditorObserverConfiguration.def`

```json
{
  "Guid": "9e196678-bbda-46d0-b4e9-82dba6037c3b",
  "CameraObserverDefinitionDebugName": "Camera"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EditorObserverConfigurationObjectBuilder')
search_content('', type_contains='EditorObserverConfigurationObjectBuilder')
```
