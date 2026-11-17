# DynamicVoxelRenderComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Components.DynamicVoxelRenderComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Components`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Procedural\VS2_0\System\Prefabs\Voxel\PrefabDynamicVoxel_Client_DynamicVoxelRenderComponentDefinition.def`

```json
{
  "Guid": "ef710dfd-8a98-48fc-a5cd-db446e97d2c6",
  "ClipmapSettings": "6c73c7d4-74f7-4c97-ba27-80d6b85e5b6f",
  "LodTransitionDuration": 4999997
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DynamicVoxelRenderComponentDefinitionObjectBuilder')
search_content('', type_contains='DynamicVoxelRenderComponentDefinitionObjectBuilder')
```
