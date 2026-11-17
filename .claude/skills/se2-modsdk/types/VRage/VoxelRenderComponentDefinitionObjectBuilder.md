# VoxelRenderComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Components.VoxelRenderComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Components`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ClipmapSettings` | Defines the preset configuration for the voxel clipmap used by this particular render component. Determines the visual quality and performance characteristics of voxel rendering. Includes quality level settings (e.g., low, normal, high) and additional rendering features such as ambient occlusion. |
| `LodTransitionDuration` | Defines the duration for transitioning between levels of detail (LOD) in the clipmap. The transition occurs as the camera moves closer to or farther from the voxel object. A longer duration creates smoother transitions but may feel less responsive. Adjust the value based on visual preference and the expected speed of camera movement. Default: 0.5 seconds. Recommended: 0.2 to 1.0 seconds. |

## A real one

`Vanilla\Assets\Environment\System\AsteroidRender.def`

```json
{
  "Guid": "3b9a3aac-7214-40d3-a700-91f9ee833fc5",
  "ClipmapSettings": "d9daa216-89c6-4101-a381-24ee95954a17",
  "LodTransitionDuration": 5000000
}
```

Others: `AsteroidClipmapRender`, `VoxelRenderComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelRenderComponentDefinitionObjectBuilder')
search_content('', type_contains='VoxelRenderComponentDefinitionObjectBuilder')
```
