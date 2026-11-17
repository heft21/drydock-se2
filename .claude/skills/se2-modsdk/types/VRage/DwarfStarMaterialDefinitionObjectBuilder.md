# DwarfStarMaterialDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Render.Materials.DwarfStarMaterialDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Render.Materials`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FresnelOpacity` | how dark is the fresnel effect |
| `FresnelPower` | size of fresnel effect |

## A real one

`Vanilla\Assets\Environment\Planets\BrownDwarf\Textures\BrownDwarfMaterial.def`

```json
{
  "Guid": "7c049a4d-cf8a-4b11-bb95-fa8db4294381",
  "DefaultState": "a710b9e9-72e9-4005-938b-301409e25d72",
  "PinTextures": false,
  "CustomTexelDensity": 2e-05,
  "ColorMetalTexture": "{G}3d6d16e6-d76a-484d-bb8b-7645b1130828",
  "NormalRoughnessTexture": "{G}dd3d6b8f-7209-4946-87f9-913f0adb496a",
  "ExtensionsTexture": "{G}0b06437d-cb19-4073-a70c-f388970dc970",
  "EmissivityMultiplier": 350,
  "FresnelPower": 2.8,
  "FresnelOpacity": 0.7
}
```

Others: `DelfosColonization`

---

Read it with the MCP server rather than by hand:

```
describe_type('DwarfStarMaterialDefinitionObjectBuilder')
search_content('', type_contains='DwarfStarMaterialDefinitionObjectBuilder')
```
