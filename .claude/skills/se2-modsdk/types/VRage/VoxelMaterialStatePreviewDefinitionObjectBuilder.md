# VoxelMaterialStatePreviewDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Materials.Previews.VoxelMaterialStatePreviewDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials.Previews`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Models` | Voxel map assets that can be used to preview the material |

## A real one

`Engine\Assets\Preview\Materials\VoxelMaterialStatePreviewDefinition.def`

```json
{
  "Guid": "09e041a0-cde8-4055-981b-037bb5b69002",
  "Models": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelMaterialStatePreviewDefinitionObjectBuilder')
search_content('', type_contains='VoxelMaterialStatePreviewDefinitionObjectBuilder')
```
