# NPCSpawnerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.NPC.NPCSpawnerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI.NPC`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Procedural\VS4_0\Space\Encounters\NPCDemo\NPCDemoEncounter_NPCSpawnerDefinition.def`

```json
{
  "Guid": "42c71632-add8-49b6-be61-5255e5b00ef9",
  "SpawnHostileNPCs": true,
  "OwnGridsAsHostile": true
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('NPCSpawnerDefinitionObjectBuilder')
search_content('', type_contains='NPCSpawnerDefinitionObjectBuilder')
```
