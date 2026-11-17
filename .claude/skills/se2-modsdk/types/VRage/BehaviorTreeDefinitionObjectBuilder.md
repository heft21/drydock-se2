# BehaviorTreeDefinitionObjectBuilder

`VRage:Keen.VRage.AI.BehaviorTree.Definitions.BehaviorTreeDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.AI.BehaviorTree.Definitions`
- definitions using it: **50**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DisplayName` | Display name for debug UI. |
| `Root` | Root node of the tree. Serialized inline as a polymorphic ObjectBuilder. Hidden in PropertyInspector — tree structure is shown visually on the canvas. |
| `TickRate` | Tick rate in Hz. 0 = use global default from configuration. |

## A real one

`Vanilla\Assets\Characters\Shared\BehaviorTrees\Demos\BarkDemo.def`

Too large to inline. Fields present:

`AdditionalRoots`, `DisplayName`, `Guid`, `Root`, `TickRate`

Others: `LogAndWait`, `ReactToShot`

---

Read it with the MCP server rather than by hand:

```
describe_type('BehaviorTreeDefinitionObjectBuilder')
search_content('', type_contains='BehaviorTreeDefinitionObjectBuilder')
```
