# BlockPlacementEffectsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.BlockPlacement.BlockPlacementEffectsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.BlockPlacement`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CreativeModeParticleEffects` | Particle effect to play in creative mode |
| `OnCycleVariantAudio` | Audio event to play on cycling block size variants |
| `OnDeleteBlockAudio` | Audio event to play on deleting a block in survival mode. |
| `OnDeleteBlockCreativeAudio` | Audio event to play on deleting a block in creative mode |
| `OnPlaceBlockAudio` | Audio event to play on placing a block in survival mode. |
| `OnPlaceBlockCreativeAudio` | Audio event to play on placing a block in creative mode. |
| `SurvivalModeParticleEffects` | Particle effect to play in survival mode |

## A real one

`Vanilla\Assets\System\Configurations\BlockPlacementEffectsConfiguration.def`

```json
{
  "Guid": "2b1ecf65-77b0-4af4-8419-17c1df28e46b",
  "OnPlaceBlockAudio": "event:/UI/Block/PlaceBlockProjection",
  "OnDeleteBlockAudio": "event:/UI/Block/DeleteBlock",
  "OnPlaceBlockCreativeAudio": "event:/UI/Block/PlaceBlock",
  "OnDeleteBlockCreativeAudio": "event:/UI/Block/DeleteBlock",
  "OnCycleVariantAudio": "event:/UI/ItemSizeR",
  "SurvivalModeParticleEffects": {
    "OnPlaceBlockParticleEffect": {
      "ParticleEffect": "e6994799-17af-4e54-8600-e1425933a0ac",
      "Dummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
      "Scale": 1
    },
    "OnDeleteBlockParticleEffect": {
      "ParticleEffect": "e6994799-17af-4e54-8600-e1425933a0ac",
      "Dummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
      "Scale": 1
    },
    "OnPlaceMultipleBlocksParticleEffect": {
      "ParticleEffect": "e6994799-17af-4e54-8600-e1425933a0ac",
      "Dummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
      "Scale": 1
    }
  },
  "CreativeModeParticleEffects": {
    "OnPlaceBlockParticleEffect": {
      "ParticleEffect": "101d03c6-efda-423f-8807-35a9ba6e0af3",
      "Dummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
      "Scale": 1
    },
    "OnDeleteBlockParticleEffect": {
      "ParticleEffect": "101d03c6-efda-423f-8807-35a9ba6e0af3",
      "Dummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
      "Scale": 1
    },
    "OnPlaceMultipleBlocksParticleEffect": {
      "ParticleEffect": "03fef020-9f29-4669-be16-8ce345bf955d",
      "Dummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
      "Scale": 1
    }
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockPlacementEffectsConfigurationObjectBuilder')
search_content('', type_contains='BlockPlacementEffectsConfigurationObjectBuilder')
```
