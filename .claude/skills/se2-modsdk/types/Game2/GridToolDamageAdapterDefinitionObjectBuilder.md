# GridToolDamageAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.ToolDamage.GridToolDamageAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools.ToolDamage`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Damage` | Damage to be applied to blocks |
| `DeformationRatio` | Affects how much deformation will be applied to the hit block. Deformations are also proportional to damage inflicted. Value of 0 results in no deformation, value of 1 results in maximum deformation to be applied. |
| `FractureImpulse` | Impulse applied to the fractures |
| `Impulse` | Impulse applied to the grid for every hit block |

## A real one

`Vanilla\Assets\CharacterTools\HandDrills\Shared\HandDrill_DamageAdapterPrefab_Server_GridToolDamageAdapterDefinition.def`

```json
{
  "Guid": "6af30225-226e-4cc7-b70d-180814f6b1be",
  "Damage": 1,
  "Impulse": 100,
  "FractureImpulse": 200,
  "DeformationRatio": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GridToolDamageAdapterDefinitionObjectBuilder')
search_content('', type_contains='GridToolDamageAdapterDefinitionObjectBuilder')
```
