# WaterDomainDefinitionObjectBuilder

`VRage:Keen.VRage.Water.Components.WaterDomainDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Water.Components`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultAbandonedWaterCountThreshold` | The abandoned drop removal will not remove any water body with more cells in it than this threshold. |
| `DefaultAbandonedWaterDensityThreshold` | The abanoned drop removal will not remove any water body that has any cell with a density greater than this threshold. |
| `DefaultAbandonedWaterSolidnessThreshold` | The abandoned drop removal will not floodfill across any cells with a solidness greater than or equal to this threshold. This means that cells with a solidness greater than or equal to this threshold will define the borders between water bodies, together with air cells. |
| `DynamicDomain` | Domain is attached to dynamic block grids |
| `WaterGridPrefab` | The prefab that can be used to create water grids. |

## A real one

`Vanilla\Assets\System\Water\WaterDomain\WaterDomainDefinition.def`

```json
{
  "Guid": "d62af029-845e-4af8-a51e-fb096f516c1a",
  "WaterGridPrefab": "5c1f6e91-4f1f-4430-8916-4b4628c25f94",
  "DefaultAbandonedWaterSolidnessThreshold": 0.5,
  "DefaultAbandonedWaterDensityThreshold": 1.9,
  "DefaultAbandonedWaterCountThreshold": 1000,
  "DynamicDomain": false
}
```

Others: `DynamicWaterDomainDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('WaterDomainDefinitionObjectBuilder')
search_content('', type_contains='WaterDomainDefinitionObjectBuilder')
```
