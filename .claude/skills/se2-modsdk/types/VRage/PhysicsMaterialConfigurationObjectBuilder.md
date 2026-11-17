# PhysicsMaterialConfigurationObjectBuilder

`VRage:Keen.VRage.Physics.Definitions.PhysicsMaterialConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FrictionCombinePolicy` | Determines how friction values from two colliding materials are combined. Affects how sliding resistance is calculated during collisions. |
| `MohsScale1` | The value of the break handler impulse that Mohs scale of 1 will correspond to. |
| `MohsScale10` | The value of the break handler impulse that Mohs scale of 10 will correspond to. |
| `MohsScale2` | The value of the break handler impulse that Mohs scale of 2 will correspond to. |
| `MohsScale3` | The value of the break handler impulse that Mohs scale of 3 will correspond to. |
| `MohsScale4` | The value of the break handler impulse that Mohs scale of 4 will correspond to. |
| `MohsScale5` | The value of the break handler impulse that Mohs scale of 5 will correspond to. |
| `MohsScale6` | The value of the break handler impulse that Mohs scale of 6 will correspond to. |
| `MohsScale7` | The value of the break handler impulse that Mohs scale of 7 will correspond to. |
| `MohsScale8` | The value of the break handler impulse that Mohs scale of 8 will correspond to. |
| `MohsScale9` | The value of the break handler impulse that Mohs scale of 9 will correspond to. |
| `RestitutionCombinePolicy` | Determines how restitution values from two colliding materials are combined. Affects how energy absorption is calculated during collisions. |
| `WeldingTolerance` | Tolerance for smoothing internal edge collisions, such as steps or misaligned triangles in landscapes. Effective only when the body quality supports welding (e.g., characters). Higher tolerance reduces sensitivity to small vertical differences but may decrease precision. Note: The final welding tolerance depends on other body materials and collider settings. Cannot exceed the maximum allowed penetration for the collider. |

## A real one

`Engine\Assets\Configurations\PhysicsMaterialConfiguration.def`

```json
{
  "Guid": "44ba86f7-add4-40b1-91c7-3a80943971d6",
  "WeldingTolerance": 0.05,
  "RestitutionCombinePolicy": "Min",
  "FrictionCombinePolicy": "GeometricMean",
  "MohsScale1": 8000,
  "MohsScale2": 50000,
  "MohsScale3": 80000,
  "MohsScale4": 140000,
  "MohsScale5": 200000,
  "MohsScale6": 500000,
  "MohsScale7": 1000000,
  "MohsScale8": 2000000,
  "MohsScale9": 60000000,
  "MohsScale10": 100000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PhysicsMaterialConfigurationObjectBuilder')
search_content('', type_contains='PhysicsMaterialConfigurationObjectBuilder')
```
