# DamageTypeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Explosions.DamageTypeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Explosions`
- definitions using it: **7**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\DamageTypes\Block.def`

```json
{
  "Guid": "235c92de-c788-46f2-aab0-972b2e305115"
}
```

Others: `Flora`, `NPC_Character`

---

Read it with the MCP server rather than by hand:

```
describe_type('DamageTypeDefinitionObjectBuilder')
search_content('', type_contains='DamageTypeDefinitionObjectBuilder')
```
