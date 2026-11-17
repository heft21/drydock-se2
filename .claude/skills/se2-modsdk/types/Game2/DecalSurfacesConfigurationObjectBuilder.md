# DecalSurfacesConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Decals.DecalSurfacesConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Decals`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ArmorDecalsDefinition` | Special decal mapping for armors |
| `BlockMaterialsMapping` | Decal mapping for blocks |
| `DefaultGridDecalDefinition` | Decal mapping when hit material is not found in |
| `DefaultVoxelDecalDefinition` | Decal mapping when voxel hit material is not found in |
| `PhysicsMaterialsToSurfaceMapping` | Decal mapping for voxels and other entities, except blocks and block fractures |

## A real one

`Vanilla\Assets\System\Decals\SurfaceDecalConfiguration.def`

Too large to inline. Fields present:

`ArmorDecalsDefinition`, `BlockMaterialsMapping`, `DefaultGridDecalDefinition`, `DefaultVoxelDecalDefinition`, `Guid`, `PhysicsMaterialsToSurfaceMapping`

---

Read it with the MCP server rather than by hand:

```
describe_type('DecalSurfacesConfigurationObjectBuilder')
search_content('', type_contains='DecalSurfacesConfigurationObjectBuilder')
```
