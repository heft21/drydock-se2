# IntegrityToolEffectDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.Effects.IntegrityToolEffectDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools.Effects`
- definitions using it: **6**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Barrel` | Dummy from where a raycast should spawn to find an accurate contact particle location in third person. Uses real interaction point when not provided |
| `ContactAudio` | Audio event to play when tool is active and has contact. Looped |
| `ContactEndAudio` | Audio event to play when tool stops being active and has contact. One shot |
| `ContactStartAudio` | Audio event to play when tool starts being active and has contact. One shot |
| `DistanceScale` | By how much the array is enlarged at 1m. |
| `EffectArrayHeight` | Distance between the top and bottom effects in the array |
| `EffectArrayWidth` | Distance between the left-most and right-most effects in the array |
| `EnableEffectArray` | Uses an array of effects instead of a single effect |
| `ForceRestartOnIntegrityChange` | If true, the audio will be restarted when block integrity changes. |
| `GridMaterial` | Value to send to on instance when used on entities like grids and other characters. |
| `NoContactAudio` | Audio event to play when tool is active but has no contact. Looped |
| `NoContactEndAudio` | Audio event to play when tool stops being active and has no contact. One shot |
| `NoContactStartAudio` | Audio event to play when tool starts being active and has no contact. One shot |
| `NoContactStartFromContactAudio` | Audio event to play when tool starts being active and had contacts but doesn't anymore. One shot |
| `NoGround` | Value to send to on instance when there is no contact. |
| `NumEffectsHorizontally` | Number of effects horizontally in the array |
| `NumEffectsVertically` | Number of effects vertically in the array |
| `OffParameterValue` | Value to send to to end the audio. |
| `OnActivationParticleEffect` | Particle Effect to spawn when the welder or grinder is activated |
| `OnOffParameterName` | Parameter to use to indicate audio starting or ending based on the current state. |
| `OnParameterValue` | Value to send to to start the audio. |
| `OnPrimaryActionConstructionParticleEffect` | Particle Effect to spawn when the welder or grinder is activated, and is affecting a block that's in construction stage (not built yet) |
| `OnPrimaryActionContactPointParticleEffect` | Particle effect to spawn at the contact point of the affected block. |
| `OnPrimaryActionParticleEffect` | Particle Effect to spawn when the welder or grinder is activated, and is affecting an already existing block |
| `OnUseAudio` | Audio event to play when using the tool. |
| `StartAudioOnActive` | If true, the block audio will be on when it becomes active. |
| `UseV2Audio` | If true, will use the new audio events in the V2 group rather than . |
| `VoxelMaterial` | Value to send to on instance when used on voxels. |

## A real one

`Vanilla\Assets\Blocks\Welder\350\Welder350IntegrityToolEffectDefinition.def`

```json
{
  "Guid": "d3436aef-9866-4dac-b8a7-8aedef77ee75",
  "OnActivationParticleEffect": {
    "ParticleEffect": "f69253bd-1380-4d29-97c9-5d6dce3e4e85",
    "Dummy": "0cdc5a5e-8d33-4f57-b7b3-010102591463",
    "Scale": 1
  },
  "OnPrimaryActionParticleEffect": {
    "ParticleEffect": "e5f2e383-9fb7-44ca-b3a1-314f3db23bd9",
    "Dummy": "0cdc5a5e-8d33-4f57-b7b3-010102591463",
    "Scale": 1
  },
  "OnPrimaryActionConstructionParticleEffect": {
    "ParticleEffect": "e5f2e383-9fb7-44ca-b3a1-314f3db23bd9",
    "Dummy": "0cdc5a5e-8d33-4f57-b7b3-010102591463",
    "Scale": 1
  },
  "OnPrimaryActionContactPointParticleEffect": {
    "ParticleEffect": null,
    "Dummy": null,
    "Scale": 0
  },
  "Barrel": null,
  "EnableEffectArray": false,
  "NumEffectsHorizontally": 1,
  "NumEffectsVertically": 1,
  "EffectArrayWidth": 0,
  "EffectArrayHeight": 0,
  "DistanceScale": 0,
  "OnUseAudio": "event:/SFX/Block/WelderBlockSmall",
  "OnOffParameterName": "End",
  "OnParameterValue": 0,
  "OffParameterValue": 1,
  "StartAudioOnActive": false,
  "ForceRestartOnIntegrityChange": false,
  "NoGround": "NoContact",
  "VoxelMaterial": "Voxel",
  "GridMaterial": "GridPhysicsMaterial",
  "UseV2Audio": true,
  "NoContactAudio": "event:/SFX/Block/Welder/Welder350Idle",
  "NoContactStartAudio": "event:/SFX/Block/Welder/Welder350IdleStart",
  "NoContactEndAudio": "event:/SFX/Block/Welder/Welder350IdleEnd",
  "ContactAudio": "event:/SFX/Block/Welder/Welder350Contact",
  "ContactStartAudio": "event:/SFX/Block/Welder/Welder350ContactStart",
  "ContactEndAudio": "event:/SFX/Block/Welder/Welder350ContactEnd"
}
```

Others: `Welder400IntegrityToolEffectDefinition`, `Grinder350IntegrityToolEffectDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('IntegrityToolEffectDefinitionObjectBuilder')
search_content('', type_contains='IntegrityToolEffectDefinitionObjectBuilder')
```
