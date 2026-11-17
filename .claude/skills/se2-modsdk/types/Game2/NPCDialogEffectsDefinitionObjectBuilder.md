# NPCDialogEffectsDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.AI.NPC.NPCDialogEffectsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.AI.NPC`
- definitions using it: **3**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\Shared\NPC\GenericNPCDialogEffectsDefinition.def`

```json
{
  "Guid": "a1b9cdf4-d210-416c-9a89-cdde01670b25",
  "TextDirection": {
    "X": 0,
    "Y": 1,
    "Z": 0
  },
  "Font": null,
  "TextScale": 0.5,
  "TextDepth": false,
  "TimePerCharacter": 1000000
}
```

Others: `MaleALLNPCDialogEffectsDefinition`, `FemaleALLNPCDialogEffectsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('NPCDialogEffectsDefinitionObjectBuilder')
search_content('', type_contains='NPCDialogEffectsDefinitionObjectBuilder')
```
