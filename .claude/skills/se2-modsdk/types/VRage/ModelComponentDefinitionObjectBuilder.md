# ModelComponentDefinitionObjectBuilder

`VRage:Keen.VRage.Game.Components.Models.ModelComponentDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Components.Models`
- definitions using it: **238**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Dummies` | List of dummies registered on this model |
| `SubpartColliderOffset` | Optional offset to apply to colliders of subparts in case they aren't alligned with the subpart visual model |

## A real one

`Vanilla\Assets\Characters\System\ModelCharacter.def`

Too large to inline. Fields present:

`Dummies`, `Guid`, `Model`, `SubpartColliderOffset`

Others: `EmotePropModel`, `GoldOreItemModel`

---

Read it with the MCP server rather than by hand:

```
describe_type('ModelComponentDefinitionObjectBuilder')
search_content('', type_contains='ModelComponentDefinitionObjectBuilder')
```
