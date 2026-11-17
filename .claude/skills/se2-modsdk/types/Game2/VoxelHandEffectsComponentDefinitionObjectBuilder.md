# VoxelHandEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Toolbars.VoxelHand.VoxelHandEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Toolbars.VoxelHand`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EndAudioParameter` | Audio event parameter to control if add or remove loop is played or not. |
| `EndAudioParameterOffValue` | Value sent to FMOD Studio to stop add or remove loop. |
| `EndAudioParameterOnValue` | Value sent to FMOD Studio to start add or remove loop. |
| `OnAddVoxelAudio` | Audio event to play when player adds voxel looped sound |
| `OnRemoveVoxelAudio` | Audio event to play when player removes voxel looped sound |

## A real one

`Vanilla\Assets\System\Tools\VoxelHandEffectsComponentDefinition.def`

```json
{
  "Guid": "6908252a-5a9f-4d61-819d-a4d1dcddb3c3",
  "OnAddVoxelAudio": "event:/SFX/Tool/VoxelHandAdd",
  "OnRemoveVoxelAudio": "event:/SFX/Tool/VoxelHandRemove",
  "EndAudioParameter": "End",
  "EndAudioParameterOnValue": 0,
  "EndAudioParameterOffValue": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VoxelHandEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='VoxelHandEffectsComponentDefinitionObjectBuilder')
```
