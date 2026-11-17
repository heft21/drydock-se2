# VoxelRenderMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Definitions.VoxelRenderMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Definitions`
- definitions using it: **114**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Icon` | A prerendered image representing how the voxel material should appear visually. |
| `RenderMaterial` | Defines the triplanar render material used to display this voxel material. |
| `VoxelMaterial` | Specifies the voxel material definition associated with this render material. |

## A real one

`Vanilla\Assets\Environment\Materials\Soil.def`

```json
{
  "Guid": "bed525dd-ca48-4344-84fa-2bef6c0fc332",
  "VoxelMaterial": "00109137-7fcf-4ae4-a687-241f9d0a2fbc",
  "RenderMaterial": "f08460fa-51dc-4201-b98d-1321844a547e",
  "Icon": "{G}ae973c9b-e517-4cda-8622-82672f446945"
}
```

Others: `Forest`, `IceOre`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelRenderMaterialDefinitionObjectBuilder')
search_content('', type_contains='VoxelRenderMaterialDefinitionObjectBuilder')
```
