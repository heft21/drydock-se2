# InventoryExplosionConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Explosions.InventoryExplosionConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Explosions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EmptyDamageScalar` | Scalar applied to the damage dealt by when the inventory is empty. |
| `EmptyRadiusScalar` | Scalar applied to the explosion radius of when the inventory is empty. |
| `Explosion` | Explosion parameters. |
| `ExplosionCenter` | Dummy to center the explosion at. If not set or not present on the block, the explosion will be centered within the block's bounding box. |
| `ExplosionTriggerThreshold` | If the inventory is filled to at least this ammunition explosive risk, the explosion will be triggered. If null, the explosion is always triggered. |
| `FullDamageScalar` | Scalar applied to the damage dealt by when the inventory is full. |
| `FullRadiusScalar` | Scalar applied to the explosion radius of when the inventory is full. |
| `MaxExplosiveRisk` | Maximum ammunition explosive risk after which we consider the inventory full |

## A real one

`Vanilla\Assets\System\Configurations\InventoryExplosionConfiguration.def`

```json
{
  "Guid": "9d0ae351-d942-4b0a-ad5a-e40d2e76dd47",
  "Explosion": "e936cb9f-3445-4efd-988f-d292770b2ddd",
  "ExplosionCenter": "71e91ef6-11a4-4ba2-b034-9c8f77bee482",
  "EmptyRadiusScalar": 1,
  "FullRadiusScalar": 6,
  "EmptyDamageScalar": 1,
  "FullDamageScalar": 35,
  "ExplosionTriggerThreshold": 999,
  "MaxExplosiveRisk": 250000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('InventoryExplosionConfigurationObjectBuilder')
search_content('', type_contains='InventoryExplosionConfigurationObjectBuilder')
```
