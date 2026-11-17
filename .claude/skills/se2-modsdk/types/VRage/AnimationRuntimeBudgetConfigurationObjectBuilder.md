# AnimationRuntimeBudgetConfigurationObjectBuilder

`VRage:Keen.VRage.Animation.Client.Configurations.AnimationRuntimeBudgetConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Animation.Client.Configurations`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxUpdateInterval` | The maximum update interval for optimized animations, measured in frames. Higher values reduce animation detail during full optimization. |
| `MeasureWindowTicks` | The number of frames over which the average runtime is measured for animation budgeting purposes. Higher values increase stability but reduce responsiveness to runtime changes. |
| `ObserverTag` | The tag used to identify the observer channel via the ObserverComponent. Used to determine how far the model is during animation optimization calculations. |
| `TargetAverageRuntimeMs` | The optimal per-frame runtime for animations, in milliseconds. When the actual runtime exceeds this value, animation quality is reduced to maintain performance. |

## A real one

`Engine\Assets\Configurations\Setup\AnimationRuntimeBudgetConfiguration.def`

```json
{
  "Guid": "dab8cc73-69fa-42f1-98e3-287270c3c6fc",
  "TargetAverageRuntimeMs": 2,
  "MeasureWindowTicks": 20,
  "MaxUpdateInterval": 3,
  "ObserverTag": "AnimationObserver"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AnimationRuntimeBudgetConfigurationObjectBuilder')
search_content('', type_contains='AnimationRuntimeBudgetConfigurationObjectBuilder')
```
