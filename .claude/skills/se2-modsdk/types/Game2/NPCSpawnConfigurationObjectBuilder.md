# NPCSpawnConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.NPC.NPCSpawnConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI.NPC`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\AI\NPCSpawnConfiguration.def`

```json
{
  "Guid": "13a0240d-a09b-4300-ad3d-115dc25fda04",
  "WorldNPCSpawnPrefab": "79bc629a-bea1-4844-bac6-1d6eaa9a9cc3"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('NPCSpawnConfigurationObjectBuilder')
search_content('', type_contains='NPCSpawnConfigurationObjectBuilder')
```
