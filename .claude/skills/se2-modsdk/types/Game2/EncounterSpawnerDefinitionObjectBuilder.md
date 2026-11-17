# EncounterSpawnerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.EncounterSpawnerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters`
- definitions using it: **42**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Candidates` | List of spawn candidates. |

## A real one

`Vanilla\Assets\Templates\Contracts\BaseDefinitions\EncounterSpawnerDefinition.def`

```json
{
  "Guid": "7255d580-366f-4ac7-9f3e-74bcf1d62280",
  "Candidates": []
}
```

Others: `NPCDemoEncounterSpawnerDefinition`, `Bounty6_EncounterSpawnerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('EncounterSpawnerDefinitionObjectBuilder')
search_content('', type_contains='EncounterSpawnerDefinitionObjectBuilder')
```
