# AITargetingDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.AITargetingDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\GenericNPCDefinition_AITargetingDefinition.def`

```json
{
  "Guid": "8b85fbfb-3769-43b0-be1b-2beb0403b984",
  "ShootingAccuracy": 0.5,
  "MaxTargetRadius": 4,
  "MaxAimError": 0.34906584,
  "AimErrorHoldTimeMin": 4000000,
  "AimErrorHoldTimeMax": 9000000,
  "AimErrorGlideRate": 4,
  "AimSettleMultiplier": 3,
  "AimSettleTime": 10000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AITargetingDefinitionObjectBuilder')
search_content('', type_contains='AITargetingDefinitionObjectBuilder')
```
