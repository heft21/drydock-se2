# VoxelClipmapPredictionComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Components.VoxelClipmapPredictionComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PredictionDuration` | What duration should the camera velocity be multiplied to calculate how far the voxel resources should be predicted and prioritized. |
| `PredictionMaxDistance` | Limit the maximum distance where can predict. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\Placeholders\Planet\VoxelClipmapPredictionComponentDefinition.def`

```json
{
  "Guid": "c046a0fa-6a38-447e-8a15-523ca950007c",
  "PredictionMaxDistance": 256,
  "PredictionDuration": 50000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelClipmapPredictionComponentDefinitionObjectBuilder')
search_content('', type_contains='VoxelClipmapPredictionComponentDefinitionObjectBuilder')
```
