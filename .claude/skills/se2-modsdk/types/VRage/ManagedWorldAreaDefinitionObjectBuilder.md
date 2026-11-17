# ManagedWorldAreaDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.ManagedWorldAreas.ManagedWorldAreaDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.ManagedWorldAreas`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AsyncLoadDistanceFactor` | Distance factor for starting non-blocking managed area load. The actual distance value is clamped between and times this value |
| `BlockingLoadDistanceMax` | Blocking load distance for a managed area of size . The distance can never go over this value no matter the managed area bounds |
| `BlockingLoadDistanceMin` | Blocking load distance for a managed area of size . The distance can never go under this value no matter the managed area bounds |
| `BoundsMax` | Managed area bound size is interpolated between and this value to get trigger distances |
| `BoundsMin` | Managed area bound size is interpolated between this value and to get trigger distances |
| `UnloadSpawnDistanceFactor` | Distance factor for managed area unload. The actual distance value is clamped between and times this value |

## A real one

`Engine\Assets\Configurations\ManagedWorldAreaDefinition_Client.def`

```json
{
  "Guid": "12c5b471-ddc4-4151-87c7-6fca21883522",
  "BoundsMin": 20,
  "BoundsMax": 500,
  "BlockingLoadDistanceMin": 250,
  "BlockingLoadDistanceMax": 500,
  "AsyncLoadDistanceFactor": 20,
  "UnloadSpawnDistanceFactor": 25
}
```

Others: `ManagedWorldAreaDefinition_Server`

---

Read it with the MCP server rather than by hand:

```
describe_type('ManagedWorldAreaDefinitionObjectBuilder')
search_content('', type_contains='ManagedWorldAreaDefinitionObjectBuilder')
```
