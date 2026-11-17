# ParticleEffectsConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Components.ParticleEffectsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Components`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CameraObserverTag` | Observer tag used by ParticleEffectsSystem to access camera transform. |
| `GravityProbePrefab` | Gravity probe entity for particle effects |

## A real one

`Engine\Assets\Configurations\ParticleEffectsConfiguration.def`

```json
{
  "Guid": "2f42bba1-d11d-47ab-b37d-84d6d6f7a4c8",
  "CameraObserverTag": "AnimationObserver",
  "GravityProbePrefab": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ParticleEffectsConfigurationObjectBuilder')
search_content('', type_contains='ParticleEffectsConfigurationObjectBuilder')
```
