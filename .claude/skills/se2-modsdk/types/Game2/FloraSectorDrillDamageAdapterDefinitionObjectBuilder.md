# FloraSectorDrillDamageAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDamage.FloraSectorDrillDamageAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDamage`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\IntegrityToolFloraaSectorDamageAdapterDefinition.def`

```json
{
  "Guid": "ab115c21-ab3f-41f5-9214-193b96fd6b9f",
  "Damage": 100,
  "MaxDamageDistance": 3
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloraSectorDrillDamageAdapterDefinitionObjectBuilder')
search_content('', type_contains='FloraSectorDrillDamageAdapterDefinitionObjectBuilder')
```
