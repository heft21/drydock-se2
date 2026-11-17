# ErrorMaterialsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Materials.ErrorMaterialsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `VertexStreamDictionary` | Assigment of the error materials to specific vertex stream formats. Vertex stream formats allows to support multiple types of meshes (static model, animated model, terrain). Each of the mesh types needs own materials. If new type of mesh (with new vertex format) is created the error materials should be supplied to this field. |

## A real one

`Engine\Assets\Configurations\Setup\ErrorMaterialsConfiguration.def`

Too large to inline. Fields present:

`Guid`, `VertexStreamDictionary`

---

Read it with the MCP server rather than by hand:

```
describe_type('ErrorMaterialsConfigurationObjectBuilder')
search_content('', type_contains='ErrorMaterialsConfigurationObjectBuilder')
```
