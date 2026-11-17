# ClientRespawnPointDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Respawn.ClientRespawnPointDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Respawn`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\ClientRespawnPointDefinition.def`

```json
{
  "Guid": "13352be4-7ec9-4348-b34e-2bd724f72a8a",
  "RespawnDummyType": "ee2b294b-a9a2-4321-a0bb-e699f2894724"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ClientRespawnPointDefinitionObjectBuilder')
search_content('', type_contains='ClientRespawnPointDefinitionObjectBuilder')
```
