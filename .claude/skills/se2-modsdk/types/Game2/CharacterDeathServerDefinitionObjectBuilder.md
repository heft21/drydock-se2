# CharacterDeathServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterDeathServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\CharacterDeathServerDefinition.def`

```json
{
  "Guid": "7a1f4c2e-9b83-4d16-8f52-31c6e0a47b95",
  "DropActiveTool": false
}
```

Others: `NPCCharacterDeathServerDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterDeathServerDefinitionObjectBuilder')
search_content('', type_contains='CharacterDeathServerDefinitionObjectBuilder')
```
