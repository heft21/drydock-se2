# VolumeDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.ProceduralGeneration.Volume.VolumeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.ProceduralGeneration.Volume`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Density` | The target number of entities to spawn per cubic kilometer, if conditions allow for it. |
| `Entities` | List of entities that can be spawned in space. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\System\Data\Volumes\InfiniteVolume-2-0.def`

```json
{
  "Guid": "82da5c8f-3871-4ef6-bb33-c539b5539e9d",
  "Density": 0.0007,
  "Entities": [
    {
      "Key": "86387d7f-91fa-47f3-85eb-caf58477bced",
      "Value": {
        "EntityPrefab": "cf73eeb4-f14b-435f-933d-9e0945e58acf",
        "Probability": 0.6,
        "RandomRotation": true,
        "VoxelGenerationData": "1e48da74-89ac-4510-b24b-ea13d5f2feef",
        "ClusterInfo": null
      }
    },
    {
      "Key": "6faeddd3-f9cb-4871-a89a-a277b9f98072",
      "Value": {
        "EntityPrefab": "cf73eeb4-f14b-435f-933d-9e0945e58acf",
        "Probability": 0.4,
        "RandomRotation": true,
        "VoxelGenerationData": "1e48da74-89ac-4510-b24b-ea13d5f2feef",
        "ClusterInfo": {
          "MinAmount": 2,
          "MaxAmount": 8,
          "MaxDistance": 256,
          "Members": [
            {
              "MemberPrefab": "cf73eeb4-f14b-435f-933d-9e0945e58acf",
              "VoxelGenerationData": "b2664161-0922-419e-b783-a1e5353b4cfa",
              "Probability": 1
            }
          ]
        }
      }
    }
  ]
}
```

Others: `InfiniteVolume-1-5`, `FieldVolumeGenerator1`

---

Read it with the MCP server rather than by hand:

```
describe_type('VolumeDefinitionObjectBuilder')
search_content('', type_contains='VolumeDefinitionObjectBuilder')
```
