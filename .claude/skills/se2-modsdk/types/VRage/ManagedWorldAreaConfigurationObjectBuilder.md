# ManagedWorldAreaConfigurationObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.ManagedWorldAreas.ManagedWorldAreaConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.ManagedWorldAreas`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Client` | Client settings. |
| `Server` | Server settings. |

## A real one

`Engine\Assets\Configurations\ManagedWorldAreaConfiguration.def`

```json
{
  "Guid": "ea7e8e17-5681-4e61-9ef0-960bbc35e10c",
  "Client": "12c5b471-ddc4-4151-87c7-6fca21883522",
  "Server": "9201ef1a-f288-4821-b3ce-39e76381f2b5"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ManagedWorldAreaConfigurationObjectBuilder')
search_content('', type_contains='ManagedWorldAreaConfigurationObjectBuilder')
```
