# CooldownCategoryDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.Consumables.CooldownCategoryDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters.Consumables`
- definitions using it: **5**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Items\Consumables\Medikit\MedikitConsumableCooldownCategory.def`

```json
{
  "Guid": "04194257-f33b-4613-9b8e-ee76f335bf6f"
}
```

Others: `ConsumableSuitBattery_CooldownCategoryDefinition`, `ConsumableOxygenRecharge_CooldownCategoryDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CooldownCategoryDefinitionObjectBuilder')
search_content('', type_contains='CooldownCategoryDefinitionObjectBuilder')
```
