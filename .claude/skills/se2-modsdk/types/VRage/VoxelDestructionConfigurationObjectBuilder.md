# VoxelDestructionConfigurationObjectBuilder

`VRage:Keen.VRage.Voxels.Definitions.VoxelDestructionConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CapsuleMaxDistanceFromFirst` | When splitting capsules into clusters, the algorithm will check how far is each capsule from the first in the cluster. If the distance exceeds this value the cluster will be disconnected. |
| `CapsuleMaxGap` | When splitting capsules into clusters, the algorithm checks capsules for connectivity. The gap allows some capsules that are disconnected to be kept in the same cluster. Use 0 for strict connectivity checks. |
| `CapsuleMergeAggressiveness` | Controls the merging behavior of destruction capsules based on proximity. Lower values make merging less aggressive, requiring capsules to be closer to merge, while higher values increase merging likelihood. For example, values like 1 or 2 are highly aggressive, while 0.1 allows merging only when capsules are very close. |
| `CapsuleMinimumRadius` | The minimum radius of destruction capsules. Smaller voxel holes created during destruction will be inflated in order to reach this minimum. |
| `EnableDebugDrawCapsules` | Toggles the debug draw of destruction capsules. Useful for verifying capsule behavior during voxel destruction events. |
| `MinimumPenetrationDistanceForDestruction` | Specifies the minimum penetration distance required for voxels to apply destruction. Example: If a voxel receives an impulse with a penetration of 0.5m and this value is set to 0.7m, no destruction occurs. However, if the same impulse is applied and this value is set to 0.1m, the voxel will be destroyed. Important: Consult your physics programmer before modifying this value. |

## A real one

`Engine\Assets\Configurations\VoxelDestructionConfiguration.def`

```json
{
  "Guid": "ac9fb69f-9bf0-4cbf-bbf1-d99016955f86",
  "CapsuleMinimumRadius": 1.5,
  "CapsuleMergeAggressiveness": -1,
  "MinimumPenetrationDistanceForDestruction": 0.035,
  "EnableDebugDrawCapsules": false
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelDestructionConfigurationObjectBuilder')
search_content('', type_contains='VoxelDestructionConfigurationObjectBuilder')
```
