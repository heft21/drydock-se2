# BreakHandlerLayerDefinitionObjectBuilder

`VRage:Keen.VRage.Physics.Definitions.BreakHandlerLayerDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Definitions`
- definitions using it: **7**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AllowBreakingBetweenBodiesOnConstraint` | Specifies whether entities on this layer can break connections with other entities that are directly or indirectly linked by constraints. |

## A real one

`Engine\Assets\Configurations\Collision\Grids.def`

```json
{
  "Guid": "a02aebf9-2641-4823-ad2d-edfdc6e3e6de",
  "AllowBreakingBetweenBodiesOnConstraint": false
}
```

Others: `Voxels`, `Default`

---

Read it with the MCP server rather than by hand:

```
describe_type('BreakHandlerLayerDefinitionObjectBuilder')
search_content('', type_contains='BreakHandlerLayerDefinitionObjectBuilder')
```
