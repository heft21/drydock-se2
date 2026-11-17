# CharacterAnimationBlackboardServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterAnimationBlackboardServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EmptyHandToolName` | Default value for when no hand tool is equipped |
| `GroundVelocityAverageSamples` | Number of samples to average ground velocity over. Larger values can smoothen out movement noise of the physical character capsule at the cost of responsiveness. |
| `GroundVelocityThreshold` | Threshold for ground velocity to be considered zero. Helps to filter out jittering of the character animations due to character capsule experiencing low magnitude high frequency velocity noise. Represented as fraction of maximum ground velocity. |
| `MaxAngularVelocityX` | Angular velocity the character has when blackboard value "AngularVelX_driver" reports 1. |
| `MaxAngularVelocityY` | Angular velocity the character has when blackboard value "AngularVelY_driver" reports 1. |
| `MaxAngularVelocityZ` | Angular velocity the character has when blackboard value "AngularVelZ_driver" reports 1. |
| `MaxObstacleDetectionDistance` | Furthest distance reported by the obstacle detector, used for normalizing the blackboard value to [0, 1] range. |

## A real one

`Vanilla\Assets\Characters\System\PrefabCharacterClient_CharacterAnimationBlackboardServerDefinition.def`

```json
{
  "Guid": "1981b639-34c7-41dc-918c-c909042a5e4e",
  "MaxAngularVelocityX": 0.78,
  "MaxAngularVelocityY": 1.57,
  "MaxAngularVelocityZ": 1.57,
  "GroundVelocityAverageSamples": 2,
  "GroundVelocityThreshold": 0.05,
  "EmptyHandToolName": "HandEmpty",
  "MaxObstacleDetectionDistance": 0.66
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterAnimationBlackboardServerDefinitionObjectBuilder')
search_content('', type_contains='CharacterAnimationBlackboardServerDefinitionObjectBuilder')
```
