# RespawnPointDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Respawn.RespawnPointDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Respawn`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RespawnDummyType` | Dummy that identifies where players can spawn from. Multiple dummies of the same type can be present and the order of them will determine priority. |
| `RespawnSearchBaseDistance` | The base distance from the spawn point the game will start searching for an empty spot. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\RespawnPointDefinition.def`

```json
{
  "Guid": "1e9d8734-0454-4e29-acd3-94df79a30986",
  "RespawnDummyType": "ee2b294b-a9a2-4321-a0bb-e699f2894724"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RespawnPointDefinitionObjectBuilder')
search_content('', type_contains='RespawnPointDefinitionObjectBuilder')
```
