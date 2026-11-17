# PlanetMaterialMapDefinitionObjectBuilder

`VRage:Keen.VRage.Voxels.Storage.Planet.PlanetMaterialMapDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Voxels.Storage.Planet`
- definitions using it: **107**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ColorKey` | Specifies the red channel color value that corresponds to this material map. Links regions of the planet's surface to the appropriate material rules defined in this map. |
| `MaterialRules` | A set of material placement rules for this material map. Each rule specifies the conditions and constraints for placing materials within the corresponding region. |

## A real one

`Vanilla\Assets\Procedural\VS2_0\Planets\Verdure\Biomes\MaterialMaps\SoilMaterialMap.def`

```json
{
  "Guid": "cac71b2a-2bb8-4054-9569-0e396c7597e0",
  "ColorKey": 45,
  "MaterialRules": [
    {
      "Key": "14938959-ace3-4e45-87d7-e9fe9db8c4a0",
      "Value": "c00a2bde-a903-4dbf-aed5-3067f503e312"
    },
    {
      "Key": "067556cc-26be-43d3-b0be-7eb1abfa7874",
      "Value": "ae0b8c89-5687-40c6-9871-323ee66b3ed6"
    }
  ]
}
```

Others: `StoneMaterialMap`, `CliffsMaterialMap`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlanetMaterialMapDefinitionObjectBuilder')
search_content('', type_contains='PlanetMaterialMapDefinitionObjectBuilder')
```
