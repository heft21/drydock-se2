# KillOnDisconnectServerComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.KillOnDisconnectServerComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\KillOnDisconnectServerComponentDefinition.def`

```json
{
  "Guid": "18481cd8-dca2-48ed-83ae-8d3ddfe74c3e",
  "KillTimeout": 9000000000,
  "DamageSource": "b7d8f5cd-9a49-4326-90b9-650743894104"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('KillOnDisconnectServerComponentDefinitionObjectBuilder')
search_content('', type_contains='KillOnDisconnectServerComponentDefinitionObjectBuilder')
```
