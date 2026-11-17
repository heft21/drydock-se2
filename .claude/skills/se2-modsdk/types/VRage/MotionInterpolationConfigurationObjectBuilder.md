# MotionInterpolationConfigurationObjectBuilder

`VRage:Keen.VRage.Multiplayer.Replications.MotionInterpolationConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Multiplayer.Replications`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\MotionInterpolationConfiguration.def`

```json
{
  "Guid": "bce2c248-4778-4bbe-9d4e-0eaeb55baad1",
  "MaxNudgeRate": 0.1,
  "MinServerRate": 0.05,
  "MaxServerRate": 2,
  "RebaseThreshold": 5000000,
  "StallThreshold": 5000000,
  "RateWindow": 10000000,
  "MaxExtrapolationGaps": 2,
  "MaxExtrapolation": 50000000,
  "MaxParentDepth": 8
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MotionInterpolationConfigurationObjectBuilder')
search_content('', type_contains='MotionInterpolationConfigurationObjectBuilder')
```
