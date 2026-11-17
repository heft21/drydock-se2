# MaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.MaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials`
- definitions using it: **24**

## What it is

Object builder for the material base definition.

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CustomTexelDensity` | Custom min texels per meter in the world space, that is applied to standard textures (no voxels, overlays). The entry is optional, if not set, the texel density is determined by the internal rules. |
| `DefaultState` | DefaultState to be used if the material is freshly set to the mesh part. |
| `PinTextures` | Pin textures to load the best appropriate mips ignoring resource prioritization. |

## A real one

`Vanilla\Assets\System\UI3D\UI3DMaterial.def`

```json
{
  "Guid": "cf2f28b4-52af-439d-8f9f-cb3cb4136659",
  "DefaultState": "33d02a1d-c74b-4ee3-a099-25c9341b4373",
  "PinTextures": false
}
```

Others: `WaterParticle`, `BakedImpostor`

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialDefinitionObjectBuilder')
search_content('', type_contains='MaterialDefinitionObjectBuilder')
```
