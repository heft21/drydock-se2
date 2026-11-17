# IntegrityHandToolDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.IntegrityHandToolDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\IntegrityToolDefinition.def`

```json
{
  "Guid": "ce1a17a7-94c3-4036-9d54-11d98685082e",
  "IntegrityChange": 0,
  "CanDeformBones": false,
  "CanAffectProjections": true,
  "MaxInteractionDistance": 1.7,
  "ActivationDelay": 2499999,
  "ReactivationDelay": 1000000,
  "IsAreaTool": false
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('IntegrityHandToolDefinitionObjectBuilder')
search_content('', type_contains='IntegrityHandToolDefinitionObjectBuilder')
```
