# VoxelDebrisModelsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.FloatingObjects.VoxelDebrisModelsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.FloatingObjects`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AmountMultiplier` | The relative amount of debris to spawn. 1 means default amount. |
| `Models` | Pool of models that can be spawned as voxel debris. |

## A real one

`Vanilla\Assets\Items\Debris\0xVoxelDebris.def`

```json
{
  "Guid": "9178bbce-0d3c-41b9-91a1-3c04d45b57b6",
  "AmountMultiplier": 0,
  "Models": [
    {
      "Key": "fbda9d9e-6cce-498f-9a9b-97e5f6a2370b",
      "Value": "{G}fda8e1b1-3477-4df5-b06e-1ef5b9aef824"
    },
    {
      "Key": "9ce1969a-e33f-47f9-8971-3af9f7508a5b",
      "Value": "{G}575c08ad-ec54-464d-a11c-a5f241961339"
    }
  ]
}
```

Others: `5xVoxelDebris`, `10xVoxelDebris`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelDebrisModelsDefinitionObjectBuilder')
search_content('', type_contains='VoxelDebrisModelsDefinitionObjectBuilder')
```
