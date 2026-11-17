# VoxelMaterialGameDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.VoxelMaterialGameDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels`
- definitions using it: **17**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DrillTime` | Base drill time in seconds required to drill voxels with this material |
| `VoxelMaterialDefinition` | Base voxel material settings |
| `YieldAmountPerM` | Quantity of produced for each unit of voxel resource drilled/mined |
| `YieldType` | Type of item/resource received from drilling voxels with this material |

## A real one

`Vanilla\Assets\Environment\System\VoxelMaterialGameDefinitions\IceVoxelMaterialGameDefinition.def`

```json
{
  "Guid": "3a3dfdc0-eb62-4cf6-9ab6-64af9a2f3e3f",
  "VoxelMaterialDefinition": [
    {
      "Key": "c0058cf6-2518-49df-a55c-0ff6053fc007",
      "Value": "35aca48e-3a67-419e-8d1c-e53f12691dc2"
    }
  ],
  "DrillTime": 19999990,
  "YieldType": "6ae64849-8c10-4341-88da-dbe385cbb3bb",
  "YieldAmountPerM": 16
}
```

Others: `IronVoxelMaterialGameDefinition`, `LeadVoxelMaterialGameDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelMaterialGameDefinitionObjectBuilder')
search_content('', type_contains='VoxelMaterialGameDefinitionObjectBuilder')
```
