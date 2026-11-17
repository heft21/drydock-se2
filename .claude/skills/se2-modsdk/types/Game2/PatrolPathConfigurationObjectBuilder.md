# PatrolPathConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.Patrol.PatrolPathConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI.Patrol`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GridAttachedPathPrefab` | Prefab for a patrol path entity attached as a child of a grid. |
| `WorldPathPrefab` | Prefab for a standalone world-anchored patrol path entity. |

## A real one

`Vanilla\Assets\System\AI\PatrolPathConfiguration.def`

```json
{
  "Guid": "e55f76f6-f697-4455-b6f9-fe1cd0d5c5cb",
  "WorldPathPrefab": "097472c6-503d-461e-b866-cc3ffed01113"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PatrolPathConfigurationObjectBuilder')
search_content('', type_contains='PatrolPathConfigurationObjectBuilder')
```
