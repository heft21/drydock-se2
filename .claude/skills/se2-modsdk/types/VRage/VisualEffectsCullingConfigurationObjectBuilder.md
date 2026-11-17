# VisualEffectsCullingConfigurationObjectBuilder

`VRage:Keen.VRage.Core.Game.GameSystems.VisualEffects.VisualEffectsCullingConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Core.Game.GameSystems.VisualEffects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxDistance` | Maximum distance at which visual effects are enabled |
| `ObserverTag` | Tag associated to the observable entity whose transform we should use as ventage point for this system (e.g. camera) |

## A real one

`Engine\Assets\Configurations\Setup\VisualEffectsCullingConfiguration.def`

```json
{
  "Guid": "bf71d372-1fa4-47fa-beec-9eb623b6c243",
  "MaxDistance": 250,
  "ObserverTag": "VisualEffectsObserver"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VisualEffectsCullingConfigurationObjectBuilder')
search_content('', type_contains='VisualEffectsCullingConfigurationObjectBuilder')
```
