# OreDetectionEffectsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.OreDetection.OreDetectionEffectsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.OreDetection`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OnNewOreMarkerAudio` | Audio event to play when ore is detected. One-shot sound |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\OreDetectionEffectsConfiguration.def`

```json
{
  "Guid": "6279a524-59d2-49b4-8a6e-603b4fa5e01c",
  "OnNewOreMarkerAudio": "event:/UI/OreDetector"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('OreDetectionEffectsConfigurationObjectBuilder')
search_content('', type_contains='OreDetectionEffectsConfigurationObjectBuilder')
```
