# GameManagedAreaControllerConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ManagedAreas.GameManagedAreaControllerConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ManagedAreas`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ManagedMissionEntityIdPrefab` | Prefab needed to restore mission entity id on managed world area entities. |
| `ManagedMissionEntityPrefab` | prefab to spawn for managed mission projections |

## A real one

`Vanilla\Assets\System\Configurations\GameManagedAreaControllerConfiguration.def`

```json
{
  "Guid": "9a5fe3ea-e69b-4875-8ee9-88153462ba04",
  "ManagedMissionEntityPrefab": "7e6526cd-6cf9-4f37-8ca0-b3ff847d034e",
  "ManagedMissionEntityIdPrefab": "b0903bf1-543d-41e7-98a8-26a2467c24a9"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GameManagedAreaControllerConfigurationObjectBuilder')
search_content('', type_contains='GameManagedAreaControllerConfigurationObjectBuilder')
```
