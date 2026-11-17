# BehaviorTreeConfigurationObjectBuilder

`VRage:Keen.VRage.AI.BehaviorTree.Definitions.BehaviorTreeConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.AI.BehaviorTree.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultTickRate` | Default tick rate in Hz for trees that don't specify their own. |
| `MaxNodesPerFrame` | Maximum nodes to tick across all trees per frame. |

## A real one

`Vanilla\Assets\System\AI\BehaviorTreeConfiguration.def`

```json
{
  "Guid": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
  "DefaultTickRate": 10,
  "MaxNodesPerFrame": 5000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BehaviorTreeConfigurationObjectBuilder')
search_content('', type_contains='BehaviorTreeConfigurationObjectBuilder')
```
