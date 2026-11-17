# CharacterMultiStrategyAnimationControllerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterMultiStrategyAnimationControllerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\ComponentCharacterAnimationController.def`

```json
{
  "Guid": "78b757f0-a2ed-4fff-adc6-cec366f16940",
  "MaxAngularVelocityX": 0.78,
  "MaxAngularVelocityY": 1.57,
  "MaxAngularVelocityZ": 1.57,
  "GroundVelocityAverageSamples": 2,
  "GroundVelocityThreshold": 0.14,
  "EmptyHandToolName": "HandEmpty",
  "MaxObstacleDetectionDistance": 0.66
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterMultiStrategyAnimationControllerDefinitionObjectBuilder')
search_content('', type_contains='CharacterMultiStrategyAnimationControllerDefinitionObjectBuilder')
```
