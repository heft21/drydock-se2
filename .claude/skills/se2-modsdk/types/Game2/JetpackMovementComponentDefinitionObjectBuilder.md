# JetpackMovementComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.JetpackMovementComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BoostModeSpeedLimit` | When in jetpack boost mode and dampeners are on, the character is not allowed to accelerate past this speed limit. This speed limit is enforced by dampeners (the player can be pushed past the limit by another ship or gravity) |
| `BoostMovementDefinition` | that is applied when in jetpack boost mode |
| `BoostThrustMultiplier` | Multiplier of when in jetpack boost mode |
| `BoostTorqueMultiplier` | Multiplier of when in jetpack boost mode |
| `MaxThrust` | Maximum amplitude of the character propulsion force when in precision mode |
| `MaxTorque` | Maximum amplitude of the character rotational force |
| `PrecisionModeSpeedLimit` | When out of jetpack boost mode and dampeners are on, the character is not allowed to accelerate past this speed limit. This speed limit is enforced by dampeners (the player can be pushed past the limit by another ship or gravity) |

## A real one

`Vanilla\Assets\Characters\System\JetpackMovementComponentDefinition.def`

```json
{
  "Guid": "76487d13-1aba-4689-9ba1-fc57c49fbb40",
  "MaxThrust": 1000,
  "BoostThrustMultiplier": 1.5,
  "MaxTorque": 65,
  "BoostTorqueMultiplier": 0.4,
  "BoostMovementDefinition": "93977c5f-ca4b-4b15-a124-ccf019bcdbcd",
  "PrecisionModeSpeedLimit": 20,
  "BoostModeSpeedLimit": 30
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('JetpackMovementComponentDefinitionObjectBuilder')
search_content('', type_contains='JetpackMovementComponentDefinitionObjectBuilder')
```
