# LocalAudioEffectsConfigurationObjectBuilder

`VRage:Keen.VRage.Game.Client.Effects.Definitions.LocalAudioEffectsConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Game.Client.Effects.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CameraObserverTag` | Observer tag used by the local audio effects system to access camera transform. |
| `SpaceAmbianceAudio` | Audio event containing ambiance music played in space. |
| `SpaceMusicCategory` | Music category to play when in space |

## A real one

`Vanilla\Assets\System\Configurations\LocalAudioEffectsConfiguration.def`

```json
{
  "Guid": "f27e0ba9-f72b-453f-84ea-1372133483ae",
  "CameraObserverTag": "ClosestPlanetObserver"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('LocalAudioEffectsConfigurationObjectBuilder')
search_content('', type_contains='LocalAudioEffectsConfigurationObjectBuilder')
```
