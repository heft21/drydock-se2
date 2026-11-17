# EntityCompositeDefinitionObjectBuilder

`VRage:Keen.VRage.DCS.Definitions.EntityCompositeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.DCS.Definitions`
- definitions using it: **210**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TagSlots` | Maps tags to the ID of a component |

## A real one

`Vanilla\Assets\System\Grid\CompositeGrid.def`

Too large to inline. Fields present:

`Components`, `Guid`, `TagSlots`

Others: `CompositeBlockBase`, `Piston150_S1`

---

Read it with the MCP server rather than by hand:

```
describe_type('EntityCompositeDefinitionObjectBuilder')
search_content('', type_contains='EntityCompositeDefinitionObjectBuilder')
```
