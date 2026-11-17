# GameErrorMaterialsConfigurationObjectBuilder

`VRage:Keen.VRage.Render.Materials.GameErrorMaterialsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Render.Materials`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `VertexStreamDictionary` | Assigment of the error materials to specific vertex stream formats and error types Each of the mesh types needs own materials. If the game adds a new type of the mesh (with new vertex format) the error materials should be supplied to this field. |

## A real one

`Engine\Assets\Configurations\Setup\GameErrorMaterialsConfiguration.def`

```json
{
  "Guid": "39249ff7-10fb-49c7-a89a-8988efea3320",
  "VertexStreamDictionary": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GameErrorMaterialsConfigurationObjectBuilder')
search_content('', type_contains='GameErrorMaterialsConfigurationObjectBuilder')
```
