# FloraSectorToolDamageAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.ToolDamage.FloraSectorToolDamageAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.ToolDamage`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Damage` | Damage to be applied to flora items |
| `MaxDamageDistance` | How far away from the source can the hit position be to damage flora items |

## A real one

`Vanilla\Assets\Blocks\Drills\Drill Damage Adapter\Drill350_DamageAdapterPrefab_Server_FloraSectorDrillDamageAdapterDefinition.def`

```json
{
  "Guid": "48013bd9-c745-42f0-829c-1260f81a19d8",
  "Damage": 1000,
  "MaxDamageDistance": 3
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraSectorToolDamageAdapterDefinitionObjectBuilder')
search_content('', type_contains='FloraSectorToolDamageAdapterDefinitionObjectBuilder')
```
