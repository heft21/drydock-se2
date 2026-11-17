# TrashRemovalConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.TrashRemoval.TrashRemovalConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.TrashRemoval`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackpackPrefabTag` | Tag assigned to the backpack prefab used to differentiate it from other FloatingContainerComponent-based entities |
| `Backpacks` | Floating backpacks limitations. |
| `CameraObserverTag` | Observer tag associated with camera entities. This allows to query for all player-controlled entities, as only those character have camera. |
| `CleanupBudgetTime` | The limit how much time the trash removal system can spend on removing trash per frame. |
| `Corpses` | Corpses limitations. |
| `FloatingObjects` | Floating object limitations. |
| `GridBones` | Grid bone chunk limitations. |
| `NonPlayerGridPCU` | Grid PCU limitations for NPCs. |
| `PlayerGridPCU` | Grid PCU limitations for players. |
| `VoxelModification` | Voxel modification limitations. |
| `VoxelModificationSettleTime` | Quiet period that must elapse after the last permanent voxel modification before the cleanup runs. Acts as a trailing-edge debounce so cleanup does not run while a player is actively mining. |

## A real one

`Vanilla\Assets\System\Configurations\TrashRemovalConfiguration.def`

```json
{
  "Guid": "44fc0fa9-da6e-4d7b-91fc-3e17e74ddc8b",
  "CleanupBudgetTime": 10000,
  "BackpackPrefabTag": "BACKPACK",
  "PlayerGridPCU": {
    "TargetCleanupLimit": 400000,
    "ExecuteCleanupLimit": 420000,
    "MinPlayerDistance": 0
  },
  "NonPlayerGridPCU": {
    "TargetCleanupLimit": 150000,
    "ExecuteCleanupLimit": 200000,
    "MinPlayerDistance": 50
  },
  "FloatingObjects": {
    "TargetCleanupLimit": 64,
    "ExecuteCleanupLimit": 80,
    "MinPlayerDistance": 10
  },
  "GridBones": {
    "TargetCleanupLimit": 500,
    "ExecuteCleanupLimit": 600,
    "MinPlayerDistance": 0
  },
  "Corpses": {
    "TargetCleanupLimit": 4,
    "ExecuteCleanupLimit": 5,
    "MinPlayerDistance": 50
  },
  "Backpacks": {
    "TargetCleanupLimit": 20,
    "ExecuteCleanupLimit": 30,
    "MinPlayerDistance": 15
  },
  "VoxelModification": {
    "TargetCleanupLimit": 2147483647,
    "ExecuteCleanupLimit": 2147483647,
    "MinPlayerDistance": 0
  },
  "VoxelModificationSettleTime": 50000000,
  "CameraObserverTag": "TrashRemovalObserver"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('TrashRemovalConfigurationObjectBuilder')
search_content('', type_contains='TrashRemovalConfigurationObjectBuilder')
```
