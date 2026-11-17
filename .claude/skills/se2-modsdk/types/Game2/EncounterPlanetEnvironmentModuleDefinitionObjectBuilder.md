# EncounterPlanetEnvironmentModuleDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounters.EncounterPlanetEnvironmentModuleDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters.PlanetEncounters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ProceduralTriggerTypes` | The type of data tags the procedural system will react to to spawn the items. |
| `SurfaceEncounters` | A list of encounter details for the planet's surface biomes. |
| `TriggerEnterMargin` | Distance at which contract entities will procedurally spawn. |
| `TriggerExitMargin` | Distance at which contract entities will procedurally despawn. For best results, it is recommended that this value is higher than the |

## A real one

`Vanilla\Assets\Templates\Planets\BaseDefinitions\EncounterPlanetEnvironmentModuleDefinition.def`

```json
{
  "Guid": "403caebe-f04a-4c63-83ab-82707e943574",
  "TriggerEnterMargin": 4000,
  "TriggerExitMargin": 5000,
  "ProceduralTriggerTypes": [
    {
      "Key": "146c72a8-57cb-42e3-8703-90aecbad3c6b",
      "Value": "Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterComponent"
    }
  ],
  "SurfaceEncounters": []
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('EncounterPlanetEnvironmentModuleDefinitionObjectBuilder')
search_content('', type_contains='EncounterPlanetEnvironmentModuleDefinitionObjectBuilder')
```
