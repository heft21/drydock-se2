# ServerJetpackBoostComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.ServerJetpackBoostComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoostHoldDuration` | Hold time necessary for the boost mode to trigger. |
| `BoostImpulseDuration` | The duration of the boost impulse. |
| `BoostImpulseEaseOutPower` | Power of the ease-out curve of the boost impulse, the higher it is, the quicker the speed will rise over the boost impulse duration. |
| `BoostImpulseTargetVelocity` | The velocity that must be reached for the boost impulse to stop. |
| `BoostTorqueMultiplier` | Multiplier of when in boost mode |
| `ForwardBoostThrustMultiplier` | Multiplier of forward when in boost mode |
| `LateralBoostThrustMultiplier` | Multiplier of lateral when in boost mode |

## A real one

`Vanilla\Assets\Characters\System\ServerJetpackBoostComponentDefinition.def`

```json
{
  "Guid": "4325391d-2dcb-4067-8981-4010365011bf",
  "BoostHoldDuration": 20000000,
  "BoostImpulseTargetVelocity": 40,
  "BoostImpulseDuration": 10000000,
  "BoostImpulseEaseOutPower": 4,
  "BoostTorqueMultiplier": 0.2,
  "ForwardBoostThrustMultiplier": 1,
  "LateralBoostThrustMultiplier": 0.2
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ServerJetpackBoostComponentDefinitionObjectBuilder')
search_content('', type_contains='ServerJetpackBoostComponentDefinitionObjectBuilder')
```
