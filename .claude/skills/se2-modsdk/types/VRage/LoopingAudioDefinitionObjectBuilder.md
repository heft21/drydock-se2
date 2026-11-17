# LoopingAudioDefinitionObjectBuilder

`VRage:Keen.VRage.Audio.Components.LoopingAudioDefinitionObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Components`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LoopAudio` | Audio event to play. Must be a looping sound. |

## A real one

`Vanilla\Assets\System\Weather\MeteorProjectilePrefab_Client_LoopingAudioDefinition.def`

```json
{
  "Guid": "29ca234b-2337-433b-9c18-aabab4fe8e4d",
  "LoopAudio": "event:/SFX/Explosions/MeteorFly"
}
```

Others: `RocketLauncherProjectile_Client_LoopingAudioDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('LoopingAudioDefinitionObjectBuilder')
search_content('', type_contains='LoopingAudioDefinitionObjectBuilder')
```
