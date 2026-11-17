# SpaceEncounterSpawnLocationDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.SpaceEncounterSpawnLocationDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters`
- definitions using it: **40**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxDistance` | Maximum spawn distance from the origin. |
| `MinDistance` | Minimum spawn distance from the origin. |

## A real one

`Vanilla\Assets\Templates\Contracts\BaseDefinitions\SpaceEncounterSpawnLocationDefinition.def`

```json
{
  "Guid": "906d63a0-337d-483d-a8b6-a1578e0aee08",
  "Locations": [
    {
      "Key": "3d91e7af-765b-44ca-8737-430818fd0a37",
      "Value": "LocationSpace"
    }
  ],
  "MinDistance": 5000,
  "MaxDistance": 50000
}
```

Others: `NPCDemoEncounter_SpaceEncounterSpawnLocationDefinition`, `Bounty8_SpaceEncounterSpawnLocationDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('SpaceEncounterSpawnLocationDefinitionObjectBuilder')
search_content('', type_contains='SpaceEncounterSpawnLocationDefinitionObjectBuilder')
```
