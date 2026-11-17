# VoxelHandTileDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.StreamedUI.Categories.VoxelHandTileDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.StreamedUI.Categories`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Description` | Tool description |
| `Icon` | The icon for the tool |
| `Operator` | The tool in this group |

## A real one

`Vanilla\Assets\UI\Screens\GScreen\CreativeTools\VoxelHand_ResetVoxels.def`

```json
{
  "Guid": "3e743a1a-c97d-4b5a-95a2-71ea74d8fdb5",
  "Name": "ResetAllVoxelChanges",
  "Order": 0,
  "Subcategories": [
    {
      "Key": "58a08e14-9450-4c1f-b826-72bcfb38b927",
      "Value": "8999e3b4-6d51-4e3f-91d8-459a40ef4601"
    }
  ],
  "Operator": {
    "Name": "ResetAllVoxelChanges",
    "Icon": "{G}156950da-fc22-4d96-b82f-9d8e79596569",
    "Overlays": [
      "{G}156950da-fc22-4d96-b82f-9d8e79596569"
    ],
    "Settings": null,
    "OperationName": "ResetAllVoxelChanges",
    "Primary": "Reset",
    "Secondary": null,
    "DefaultShape": "Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.TerrainBrushes.SphereShapeDefinition",
    "DefaultMaterialGroupIndex": 0,
    "DefaultMaterialIndex": 0,
    "DefaultProjectBrush": true
  },
  "Icon": "{G}156950da-fc22-4d96-b82f-9d8e79596569",
  "Description": "ResetAllVoxelChangesDesc"
}
```

Others: `VoxelHand_AddRemoveVoxels`, `VoxelHand_ChangeResetVoxelMaterial`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelHandTileDefinitionObjectBuilder')
search_content('', type_contains='VoxelHandTileDefinitionObjectBuilder')
```
