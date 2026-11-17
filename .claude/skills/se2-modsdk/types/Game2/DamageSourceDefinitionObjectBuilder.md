# DamageSourceDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProjectileSystems.DamageSourceDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProjectileSystems`
- definitions using it: **13**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `KillTextId` | Text shown when a player dies due to this damage type |

## A real one

`Vanilla\Assets\System\DamageSources\HeatDamageSource.def`

```json
{
  "Guid": "42427790-2e16-4b94-8cfc-3ab989e82f78",
  "KillTextId": "KillMessageHeat",
  "DamageName": "Heat"
}
```

Others: `CustomDamageSource`, `ImpactDamageSource`

---

Read it with the MCP server rather than by hand:

```
describe_type('DamageSourceDefinitionObjectBuilder')
search_content('', type_contains='DamageSourceDefinitionObjectBuilder')
```
