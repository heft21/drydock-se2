# MotionParentConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Multiplayer.MotionParentConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Multiplayer`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Configurations\MotionParentConfiguration.def`

```json
{
  "Guid": "869aa61c-f1b7-4cbe-a4f6-1cc2d0cd729e",
  "RootRelativeTolerance": 0.5,
  "RootAbsoluteTolerance": 0.01,
  "LinkRequestDelay": 2500000,
  "LinkRequestInterval": 10000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MotionParentConfigurationObjectBuilder')
search_content('', type_contains='MotionParentConfigurationObjectBuilder')
```
