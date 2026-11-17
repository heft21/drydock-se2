# BlockDestructionExplosionAudioConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Explosions.BlockDestructionExplosionAudioConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Explosions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `InventoryAmmoLevelAudioParameter` | Cargo ammo level parameter |
| `TankFuelLevelAudioParameter` | Tank fuel level parameter |

## A real one

`Vanilla\Assets\System\Configurations\BlockDestructionExplosionAudioConfiguration.def`

```json
{
  "Guid": "2ff552c6-eccc-4b1f-be69-69bd7ddfc548",
  "TankFuelLevelAudioParameter": "EmptyFull",
  "CargoAmmoLevelAudioParameter": "EmptyFull"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockDestructionExplosionAudioConfigurationObjectBuilder')
search_content('', type_contains='BlockDestructionExplosionAudioConfigurationObjectBuilder')
```
