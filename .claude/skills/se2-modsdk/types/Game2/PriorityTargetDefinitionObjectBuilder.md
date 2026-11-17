# PriorityTargetDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Weapons.PriorityTargetDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Weapons`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\Projectiles\HighPriorityTargetDefinition.def`

```json
{
  "Guid": "5e9d13d6-d006-4fbc-ba25-2f50a5294e34"
}
```

Others: `HighestPriorityTargetDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PriorityTargetDefinitionObjectBuilder')
search_content('', type_contains='PriorityTargetDefinitionObjectBuilder')
```
