# VoxelDebrisConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.FloatingObjects.VoxelDebrisConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.FloatingObjects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AngularVelocityMultiplier` | Multiplier to scale the angular velocity of voxel debris. By default, the angular velocity is random within the range (0, 0, 0) to (1, 1, 1), measured in radians/second. |
| `BaseDebrisAmount` | Base amount of voxel debris fragments to spawn in regular circumstances. Game systems can scale this amount when requesting debris to spawn. |
| `LinearVelocityMultiplier` | Multiplier to scale the linear velocity of voxel debris. By default, the linear velocity is random within the range (0, 0, 0) to (1, 1, 1), measured in meters/second. |
| `VoxelDebrisPrefab` | Voxel debris fragment prefab to spawn while drilling |

## A real one

`Vanilla\Assets\System\Configurations\VoxelDebrisConfiguration.def`

```json
{
  "Guid": "937f087d-a484-4250-90ee-8b71a5c0f201",
  "DespawnTimeVariability": 19999990,
  "VoxelDebrisPrefab": "710e6756-39bd-4dce-9eb3-4bda5d0f34b2",
  "BaseDebrisAmount": 25,
  "LinearVelocityMultiplier": 4,
  "AngularVelocityMultiplier": 3
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelDebrisConfigurationObjectBuilder')
search_content('', type_contains='VoxelDebrisConfigurationObjectBuilder')
```
