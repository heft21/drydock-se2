# VoxelPhysicsMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Physics.Definitions.VoxelPhysicsMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Definitions`
- definitions using it: **14**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Hardness` | Material's hardness on the Mohs scale (1 to 10). Defines its resistance to breaking during collisions. The value corresponds to the impulse thresholds defined in . |
| `OverrideMinimumPenetration` | Minimum penetration override for what voxels use. Voxel destructions set a max impulse, then observable penetration is scaled between the *other* entity and the set max impulse. If the observable penetration is greater than "MinimumPenetrationDistanceForDestruction" then this value is used to filter destructions on which the penetration distance is less than this value. |
| `SlowdownFactor` | The percentage by which a colliding object's velocity is reduced for every cubic meter of this material it destroys. Example: A grid collides with this material, destroying 10 cubic meters of it in the process. If this value set to 2, the colliding grid will experience a 20% velocity reduction in the collision direction. |
| `UseVelocityBasedPenetration` | Changes how voxel destruction works. Disabling this makes voxel holes be smaller by not accounting for object velocities, but looks more precise. |

## A real one

`Engine\Assets\Materials\Voxels\FallbackVoxelPhysicsMaterial.def`

```json
{
  "Guid": "8fabb5be-014a-4c11-a16d-8bd2dc293d9f",
  "StaticFriction": 0.9,
  "DynamicFriction": 0.4,
  "Restitution": 1,
  "Hardness": 6,
  "SlowdownFactor": 0.05
}
```

Others: `CorePhysicsMaterial`, `IceLikePhysicsMaterial`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelPhysicsMaterialDefinitionObjectBuilder')
search_content('', type_contains='VoxelPhysicsMaterialDefinitionObjectBuilder')
```
