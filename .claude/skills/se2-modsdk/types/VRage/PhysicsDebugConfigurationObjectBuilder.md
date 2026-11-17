# PhysicsDebugConfigurationObjectBuilder

`VRage:Keen.VRage.Physics.Debug.PhysicsDebugConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Debug`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ObserverTag` | Observer tag used by physics debug systems to access camera transform |

## A real one

`Engine\Assets\Configurations\Setup\PhysicsDebugConfiguration.def`

```json
{
  "Guid": "6cd24fb0-922b-421c-aec3-fa8be9cb6b51",
  "ObserverTag": "PhysicsObserver"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PhysicsDebugConfigurationObjectBuilder')
search_content('', type_contains='PhysicsDebugConfigurationObjectBuilder')
```
