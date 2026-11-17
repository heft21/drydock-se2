# CharacterDummyToolOriginProviderDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterDummyToolOriginProviderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\CharacterDummyToolOriginProviderDefinition.def`

```json
{
  "Guid": "fc1ff643-c42e-475d-afb6-37d74b391d5b",
  "Dummy": "fe18f491-e6d9-434f-9bfb-dd351ae68505",
  "CrouchedDummy": "9e14aa7f-9b6d-4374-b584-ab551c8a2b7a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterDummyToolOriginProviderDefinitionObjectBuilder')
search_content('', type_contains='CharacterDummyToolOriginProviderDefinitionObjectBuilder')
```
