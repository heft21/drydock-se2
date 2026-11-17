# KillingFieldComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.BrownDwarf.KillingFieldComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.BrownDwarf`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DamageRadius` | Radius at which killing field starts dealing damage |
| `DamageSource` | Damage type dealt by the killing field |
| `MaxDamage` | Maximal possible damage that can deal |
| `MaxDamageRadius` | Inner radius of the killing field. At this radius and closer to the center The maximum damage is applied |
| `MinDamage` | Minimal possible damage that can deal |
| `Radius` | Radius of the killing field notification sphere |

## A real one

`Vanilla\Assets\Procedural\VS1_5\Planets\BrownDwarf\Data\Delfos_Client_KillingFieldComponentDefinition.def`

```json
{
  "Guid": "0670f288-2ce1-4e9c-baf7-125986ccbe47",
  "Radius": 700000,
  "DamageRadius": 695000,
  "MaxDamageRadius": 300000,
  "DamageSource": "42427790-2e16-4b94-8cfc-3ab989e82f78",
  "MinDamage": 1,
  "MaxDamage": 100
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('KillingFieldComponentDefinitionObjectBuilder')
search_content('', type_contains='KillingFieldComponentDefinitionObjectBuilder')
```
