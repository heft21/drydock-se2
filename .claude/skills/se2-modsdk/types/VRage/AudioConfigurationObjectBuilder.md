# AudioConfigurationObjectBuilder

`VRage:Keen.VRage.Audio.Definitions.AudioConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Audio.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BusDefaultVolumes` | Default volume levels for each audio bus. Allows fine-tuning of audio playback balance across different buses. |
| `BussesOf3DScene` | Busses that count as in-World |
| `DefaultGroundType` | Default ground type to use when no physics material definition is available. |
| `EarlySpatialEventPlayDelay` | Time between each early spatial event play call |
| `FadeInSnapshot3DScene` | The FMOD path to the audio snapshot used to fade in 3D scene buses. |
| `FadeOutSnapshot3DScene` | The FMOD path to the audio snapshot used to fade out 3D scene buses. |
| `FmodStudioProjectHash` | The FMOD Studio project hash file (.fshash). Used to verify the audio project's integrity and compatibility. |
| `GroundTypeAudioParameter` | Audio event parameter to use for the ground type. |
| `MasterBank` | The identifier for the FMOD master audio bank. |
| `MaxVolumeOver100` | When volume is over 100% in UI, it is lerped between 1 and this value to prevent distortions |
| `MaximumMusicWaitTime` | The maximum time before the next track in a music category starts playing. |
| `MaximumUpdateDistance` | The maximum distance, in engine units, at which spatialized audio events update their transforms. Beyond this distance, transform updates are ignored to optimize performance. |
| `MaximumUpdateDistanceSquared` | squared for convenience |
| `MinimumMusicWaitTime` | The minimum time before the next track in a music category starts playing. |
| `MusicFadeInSnapshotPath` | The FMOD path to the audio snapshot used to fade in music during transitions. |
| `MusicFadeOutSnapshotPath` | The FMOD path to the audio snapshot used to fade out music during transitions. |
| `RealChannelCount` | Maximum number of simultaneously active audio events processed in real channels. Real channels are used for audible events actively processed by the hardware. |
| `StreamingBufferSize` | The size of the buffer, in bytes, used for streaming sound data. Larger buffers may reduce stuttering in complex audio scenes but increase memory usage. |
| `SystemAudioDeviceName` | The localized name of the default system audio device. |
| `TransformUpdateInterval` | Time between each spatial updates for 3d events |
| `TransitionWaitTime` | How much time to wait when transitioning from a track to the next |
| `VanillaBanks` | These bank are considered to be vanilla. This is used by when is toggled |
| `VirtualChannelCount` | Maximum number of additional audio events managed in virtual channels. Virtual channels handle events that are currently inaudible or deprioritized. |
| `VirtualVolume` | The linear volume threshold at which an audio event is virtualized. Virtualized audio events are silent but continue playing in the virtual channel. |

## A real one

`Vanilla\Assets\MainMenuData\Audio\AudioConfiguration.def`

```json
{
  "Guid": "022e4b87-8213-47c1-b086-8ee10ed12e64",
  "StreamingBufferSize": 65536,
  "RealChannelCount": 256,
  "VirtualChannelCount": 512,
  "MinimumMusicWaitTime": 100000000,
  "MaximumMusicWaitTime": 299999997,
  "MaximumUpdateDistance": 500,
  "VirtualVolume": 0.001,
  "MusicFadeInSnapshotPath": "snapshot:/MusicFadeIn",
  "MusicFadeOutSnapshotPath": "snapshot:/MusicFadeOut",
  "MusicFadeOutFastSnapshotPath": "snapshot:/CombatMusicFadeOut",
  "FmodStudioProjectHash": "{G}f4f99d68-757a-4c58-a3e3-19dd333876bd",
  "MasterBank": "Master.bank",
  "DefaultGroundType": "Voxel",
  "GroundTypeAudioParameter": "GroundType",
  "BusDefaultVolumes": {
    "bus:/": 1,
    "bus:/Music": 1,
    "bus:/UI": 1,
    "bus:/SFX": 1,
    "bus:/SFX/Tools": 1
  },
  "BussesOf3DScene": [
    {
      "Key": "f81a8fe8-b1a0-416f-9423-fbc11ff46918",
      "Value": "bus:/SFX"
    }
  ],
  "SystemAudioDeviceName": "SystemAudioDeviceName",
  "FadeInSnapshot3DScene": "snapshot:/FadeIn3DScene",
  "FadeOutSnapshot3DScene": "snapshot:/FadeOut3DScene",
  "VanillaBanks": [
    {
      "Key": "56d0e11d-2332-437a-bcf0-68c57f985121",
      "Value": "Master.bank"
    },
    {
      "Key": "a3994ab7-3a52-46ea-a599-52e8f1954cff",
      "Value": "Master.strings.bank"
    },
    {
      "Key": "4a41cb3e-0d8f-4730-8afb-d77c3ce6eb9f",
      "Value": "Music.bank"
    },
    {
      "Key": "c8d83070-d06c-4fe8-9b28-b9e936c19ca3",
      "Value": "UI.bank"
    },
    {
      "Key": "bf9f8655-7c5d-4573-9680-b30a6555ff18",
      "Value": "SFX.bank"
    }
  ],
  "EarlySpatialEventPlayDelay": 199998,
  "TransformUpdateInterval": 199998,
  "MaxVolumeOver100": 1.75,
  "TransitionWaitTime": 29999997,
  "TransitionFastWaitTime": 5000000,
  "MaximumUpdateDistanceSquared": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AudioConfigurationObjectBuilder')
search_content('', type_contains='AudioConfigurationObjectBuilder')
```
