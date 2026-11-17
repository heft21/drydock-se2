# NPCSpawnPointDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.NPC.NPCSpawnPointDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI.NPC`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\NPCSpawnPointDefinition.def`

```json
{
  "Guid": "c53d8099-4b20-47f7-8f3c-92a601616998",
  "Prefab": "38df3352-aaa4-47a0-a6a6-38b42af72aac",
  "Count": 1,
  "SpawnWithEncounter": true,
  "BehaviorTree": "81462847-3012-4ade-8fa6-a9d79ff0231b"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('NPCSpawnPointDefinitionObjectBuilder')
search_content('', type_contains='NPCSpawnPointDefinitionObjectBuilder')
```
