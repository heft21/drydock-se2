# ParallaxDecalMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Render.Materials.Decals.ParallaxDecalMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials.Decals`
- definitions using it: **40**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ExtensionsTexture` | Extension texture with AO (R), Emissive (G), Displacement (B), and Alpha (A) |
| `MaxDisplacement` | Max displacement of the surface relative to the decal Z-Size |

## A real one

`Vanilla\Assets\System\Projectiles\Voxels\DecalMaterial_Drill_Voxel_Ice_Parallax.def`

```json
{
  "Guid": "a47e76fd-e63e-4cb6-8eb7-356fe3beac6e",
  "ColorMetalTexture": "{G}de6cf77a-a826-4190-bcf7-6988d2c35be6",
  "NormalRoughnessTexture": "{G}cf103504-65f5-486d-8502-f0bab538c26a",
  "ExtensionsTexture": "{G}ef847c39-1b7c-461c-b911-46e4017c9aad",
  "EmissivityMultiplier": 0,
  "GradientRevealThreshold": 0.1,
  "MaxDisplacement": 0.15,
  "DisplacementType": "None",
  "Flags": "Albedo, Normal, Roughness, Metalness, AmbientOcclusion, Emissivity, GradientReveal"
}
```

Others: `DecalMaterial_Drill_Voxel_Ores_Parallax`, `DecalMaterial_Drill_Voxel_Rock_Parallax`

---

Read it with the MCP server rather than by hand:

```
describe_type('ParallaxDecalMaterialDefinitionObjectBuilder')
search_content('', type_contains='ParallaxDecalMaterialDefinitionObjectBuilder')
```
