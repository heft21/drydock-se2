# VoxelPlanetRenderComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Client.Components.VoxelPlanetRenderComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Client.Components`
- definitions using it: **8**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PlanetOverlay` | Represents a set of textures used to enhance the visual representation of planets at greater viewing distances. The overlay is displayed in place of detailed voxel rendering when the camera is sufficiently far away. |
| `Spherization` | Settings for planet spherization |

## A real one

`Vanilla\Assets\Environment\Planets\Byblos\ByblosOverlay_root.def`

```json
{
  "Guid": "60792765-3262-46fe-b913-500c902128e4",
  "ClipmapSettings": "e54bacbf-7671-4d39-931c-cd2f0e506a37",
  "LodTransitionDuration": 0,
  "PlanetOverlay": "55a22811-6361-48fb-b9ed-9acf1fd5ed69",
  "Spherization": "401e6761-3dda-4745-96a3-6c372eb19c9c"
}
```

Others: `VoxelPlanetRenderComponentDefinition`, `PlanetRenderComponent`

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelPlanetRenderComponentDefinitionObjectBuilder')
search_content('', type_contains='VoxelPlanetRenderComponentDefinitionObjectBuilder')
```
