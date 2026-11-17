# CubeGridKillingFieldDamageReceiverComponentConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Damage.CubeGridKillingFieldDamageReceiverComponentConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Damage`
- definitions using it: **1**

## What it is

Object builder for

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HighPcuAmount` | Damage by killing field is based on the amount of grid PCU. if Grid PCU is higher or equal to , Damage dealt to it will have coefficient of . if Grid PCU is lower or equal to , Damage dealt to it will have coefficient of . Values in between are interpolated |
| `HighPcuDamageCoefficient` | Damage by killing field is based on the amount of grid PCU. if Grid PCU is higher or equal to , Damage dealt to it will have coefficient of . if Grid PCU is lower or equal to , Damage dealt to it will have coefficient of . Values in between are interpolated |
| `HighPcuRegenerationPeriod` | How much time it takes for grid with pcu amount equal or higher than to be fully regenerated when outside the killing field |
| `LowPcuAmount` | Damage by killing field is based on the amount of grid PCU. if Grid PCU is lower or equal to , Damage dealt to it will have coefficient of . if Grid PCU is higher or equal to , Damage dealt to it will have coefficient of . Values in between are interpolated |
| `LowPcuDamageCoefficient` | Damage by killing field is based on the amount of grid PCU. if Grid PCU is lower or equal to , Damage dealt to it will have coefficient of . if Grid PCU is higher or equal to , Damage dealt to it will have coefficient of . Values in between are interpolated |
| `LowPcuRegenerationPeriod` | How much time it takes for grid with pcu amount equal or lower than to be fully regenerated when outside the killing field |
| `MaxDeformationCoefficient` | Deformation coefficient in the center of a killing field |
| `MinDeformationCoefficient` | Deformation coefficient on the very edge of a killing field |

## A real one

`Vanilla\Assets\System\Grid\CubeGridKillingFieldDamageReceiverComponentConfiguration.def`

```json
{
  "Guid": "39e376b3-2aec-431e-968e-8ba1a149f8f5",
  "LowPcuAmount": 0,
  "HighPcuAmount": 50000,
  "LowPcuDamageCoefficient": 0.8,
  "HighPcuDamageCoefficient": 0.1,
  "LowPcuRegenerationPeriod": 39999997,
  "HighPcuRegenerationPeriod": 100000000,
  "MinDeformationCoefficient": 0.1,
  "MaxDeformationCoefficient": 1,
  "GridDestructionExplosion": "2893f264-dca7-4904-a8e9-8c4f0e25317f"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CubeGridKillingFieldDamageReceiverComponentConfigurationObjectBuilder')
search_content('', type_contains='CubeGridKillingFieldDamageReceiverComponentConfigurationObjectBuilder')
```
