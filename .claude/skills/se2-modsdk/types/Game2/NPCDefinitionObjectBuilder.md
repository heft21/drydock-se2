# NPCDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.AI.NPC.Dialog.NPCDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.AI.NPC.Dialog`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\GenericNPCDefinition.def`

```json
{
  "Guid": "34f8f555-854f-4f9c-ab45-74c7089e5371",
  "Name": "NPCEngineer",
  "Targeting": "8b85fbfb-3769-43b0-be1b-2beb0403b984"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('NPCDefinitionObjectBuilder')
search_content('', type_contains='NPCDefinitionObjectBuilder')
```
