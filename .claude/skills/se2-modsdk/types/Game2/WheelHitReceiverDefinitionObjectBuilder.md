# WheelHitReceiverDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.WheelHitReceiverDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\DrivingWheel\DrivingWheelHitReceiverDefinition.def`

```json
{
  "Guid": "b7981956-7b8c-4af3-b620-ef611aeb1ac3",
  "ReceivedDamageType": "235c92de-c788-46f2-aab0-972b2e305115"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WheelHitReceiverDefinitionObjectBuilder')
search_content('', type_contains='WheelHitReceiverDefinitionObjectBuilder')
```
