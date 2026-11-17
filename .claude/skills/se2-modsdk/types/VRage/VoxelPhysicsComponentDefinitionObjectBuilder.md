# VoxelPhysicsComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Components.VoxelPhysicsComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Components`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ColliderHysteresisMargin` | Final range near objects where colliders are discarded once no longer in use. Must be greater than . |
| `ColliderPredictionMargin` | Additional range near objects where colliders are generated ahead of time to prevent simulation hitches. |
| `ColliderStorageSize` | Size of generated physics colliders in voxels storage samples. The size in the world will additionally depend on the scale used by the . Smaller values mean more efficient and tight-fitting shapes but increase bookkeeping overhead. |

## A real one

`Vanilla\Assets\Environment\System\VoxelPhysicsComponentDefinition.def`

```json
{
  "Guid": "6c5a82fe-ff4e-46fd-937d-75eb8310d180",
  "QualityType": "Default",
  "DestructionLayer": "263951fe-9c25-4ba7-ac46-67bef306a0fd",
  "Material": "6dadf3ac-aa96-4b1b-a4c5-891633a0b48a",
  "EntityLayer": "Voxels",
  "ActivationControl": "Automatic",
  "MaxDepenetrationSpeed": 1,
  "ColliderStorageSize": 32,
  "ColliderPredictionMargin": 100,
  "ColliderHysteresisMargin": 160
}
```

Others: `VoxelPlanetPhysicsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelPhysicsComponentDefinitionObjectBuilder')
search_content('', type_contains='VoxelPhysicsComponentDefinitionObjectBuilder')
```
