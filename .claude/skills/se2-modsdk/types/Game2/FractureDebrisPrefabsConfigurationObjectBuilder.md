# FractureDebrisPrefabsConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.FloatingObjects.FractureDebrisPrefabsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.FloatingObjects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DamagedBlockDebrisPrefab` | Damaged block prefab to spawn for non-breakable blocks |
| `FractureDebrisPrefab` | The base prefab representing the piece of block spawned off when the block gets fractured |
| `MaxActiveDebris` | Maximum amount of debris that can be active at the same time. New debris spawning will despawn previously spawned debris. |
| `MaxDebrisSpawnedPerTick` | Maximum amount of debris that can spawn in a single tick. Any other debris trying to spawn when the limit is exceeded will not spawn. |
| `SpecializedDebrisPrefabs` | The debris prefab to use for specific implementations of |

## A real one

`Vanilla\Assets\System\Configurations\FracturesDebrisPrefabsConfiguration.def`

```json
{
  "Guid": "70563a82-6a30-4a58-af86-6b79f2ec8777",
  "DespawnTimeVariability": 19999990,
  "FractureDebrisPrefab": "3cc73a40-9e48-43a9-885f-1c28bd5b824a",
  "SpecializedDebrisPrefabs": {
    "VRage:Keen.VRage.Voxels.Components.Flora.FloraEntityBreakableComponent": "966448bf-cc95-4237-bd42-1fecb86266d3"
  },
  "DamagedBlockDebrisPrefab": "bef7011b-c06a-4be2-bf10-debc5bfe300c",
  "MaxDebrisSpawnedPerTick": 30,
  "MaxActiveDebris": 100
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FractureDebrisPrefabsConfigurationObjectBuilder')
search_content('', type_contains='FractureDebrisPrefabsConfigurationObjectBuilder')
```
