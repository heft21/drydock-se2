# ContractPlanetEnvironmentModuleDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounters.ContractPlanetEnvironmentModuleDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ProceduralTriggerTypes` | The type of data tags the procedural system will react to to spawn the items. |
| `TriggerEnterMargin` | Distance at which contract entities will procedurally spawn. |
| `TriggerExitMargin` | Distance at which contract entities will procedurally despawn. For best results, it is recommended that this value is higher than the |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\ContractPlanetEnvironmentModuleDefinition.def`

```json
{
  "Guid": "a3bfa524-7b91-4395-b9d2-5d271790c99d",
  "TriggerEnterMargin": 2500,
  "TriggerExitMargin": 3000,
  "ProceduralTriggerTypes": [
    {
      "Key": "873c064f-3907-446c-9aa5-055ab4ea9f9a",
      "Value": "Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterComponent"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ContractPlanetEnvironmentModuleDefinitionObjectBuilder')
search_content('', type_contains='ContractPlanetEnvironmentModuleDefinitionObjectBuilder')
```
