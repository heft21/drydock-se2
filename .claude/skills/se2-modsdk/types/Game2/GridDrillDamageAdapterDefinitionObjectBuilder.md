# GridDrillDamageAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDamage.GridDrillDamageAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDamage`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Blocks\Drills\Drill Damage Adapter\Drill350_DamageAdapterPrefab_Server_GridDrillDamageAdapterDefinition.def`

```json
{
  "Guid": "31e02a20-3565-4a4a-a2cb-7fd51e0ebde0",
  "Damage": 10,
  "Impulse": 500,
  "FractureImpulse": 1000,
  "DeformationRatio": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridDrillDamageAdapterDefinitionObjectBuilder')
search_content('', type_contains='GridDrillDamageAdapterDefinitionObjectBuilder')
```
