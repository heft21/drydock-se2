# CharacterDrillDamageAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDamage.CharacterDrillDamageAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillDamage`
- definitions using it: **2**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\IntegrityToolCharacterDamageAdapterDefinition.def`

```json
{
  "Guid": "01a41051-f5cf-4869-b099-e2a23224ccef",
  "Damage": 10,
  "Impulse": 1000,
  "DamageSource": "71f8b73e-6081-4bd4-95ed-4437802150e3"
}
```

Others: `Drill350_DamageAdapterPrefab_Server_CharacterDrillDamageAdapterDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterDrillDamageAdapterDefinitionObjectBuilder')
search_content('', type_contains='CharacterDrillDamageAdapterDefinitionObjectBuilder')
```
