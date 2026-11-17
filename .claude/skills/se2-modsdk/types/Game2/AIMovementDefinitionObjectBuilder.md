# AIMovementDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.AIMovementDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\AI\AIControllerPrefab_AIMovementDefinition.def`

```json
{
  "Guid": "17299a02-8896-4f8f-8b06-884a006a0077",
  "DoorOpenDistance": 2,
  "GridFilter": "eeb28fb3-e5bf-485c-849e-8d86954c028e",
  "Acceleration": 4.5,
  "Deceleration": 3.5,
  "MaxTurnSpeed": 0,
  "TurnAcceleration": 270,
  "TurnDeceleration": 0,
  "TurnStopThreshold": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AIMovementDefinitionObjectBuilder')
search_content('', type_contains='AIMovementDefinitionObjectBuilder')
```
