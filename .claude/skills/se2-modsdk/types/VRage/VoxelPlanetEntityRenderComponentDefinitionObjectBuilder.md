# VoxelPlanetEntityRenderComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Components.VoxelPlanetEntityRenderComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Components`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Environment\System\BoulderRender.def`

```json
{
  "Guid": "03802036-4d50-49a0-afe4-796015c584bf",
  "ClipmapSettings": "6c73c7d4-74f7-4c97-ba27-80d6b85e5b6f",
  "LodTransitionDuration": 4999999
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelPlanetEntityRenderComponentDefinitionObjectBuilder')
search_content('', type_contains='VoxelPlanetEntityRenderComponentDefinitionObjectBuilder')
```
