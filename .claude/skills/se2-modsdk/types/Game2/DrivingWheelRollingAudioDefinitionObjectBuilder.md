# DrivingWheelRollingAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.DrivingWheelRollingAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RollingAudio` | Audio event to play looped when wheels are rolling on the surface. |

## A real one

`Vanilla\Assets\System\Configurations\Effects\AudioVisualEffects\Wheels\RockRollingAudio.def`

```json
{
  "Guid": "47753f38-2c54-4a72-aed1-29802d63c123",
  "RollingAudio": "event:/SFX/Block/Wheels/SurfaceRolling/WheelsRollingRocks"
}
```

Others: `SandRollingAudio`, `SnowRollingAudio`

---

Read it with the MCP server rather than by hand:

```
describe_type('DrivingWheelRollingAudioDefinitionObjectBuilder')
search_content('', type_contains='DrivingWheelRollingAudioDefinitionObjectBuilder')
```
