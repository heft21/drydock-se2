# PrefabDefinitionObjectBuilder

`VRage:Keen.VRage.Core.Game.Definitions.PrefabDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.Definitions`
- definitions using it: **180**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `_entity` | Serializable Entity object builder specified by composition and object builders. |

## A real one

`Vanilla\Assets\System\Grid\Grid_Client.def`

Too large to inline. Fields present:

`Guid`, `_entity`

Others: `Grid_Server`, `NPCSpawnPrefab`

---

Read it with the MCP server rather than by hand:

```
describe_type('PrefabDefinitionObjectBuilder')
search_content('', type_contains='PrefabDefinitionObjectBuilder')
```
