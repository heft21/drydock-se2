# BlockEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.BlockEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AudioStageConstructionValueFirst` | Parameter value to send to during and for first stage |
| `AudioStageConstructionValueLast` | Parameter value to send to during and for last stage |
| `AudioStageConstructionValueMid` | Parameter value to send to during and for mid stages |
| `BuildProgressAudioParameter` | Audio parameter sent to and to communicate build progress |
| `DamageIntegrityThresholds` | Each element represents a block integrity value at which is played when integrity goes below it |
| `HitDamageOverlay` | Optional damage overlay to show when block takes damage |
| `OffParameterValue` | Parameter value for off state |
| `OnConstructionAudio` | Audio event to play when block is constructed. This event is triggered whether the block is built at each stage. One shot sound. |
| `OnDamagedAudio` | Audio event to play when block takes damage. One shot sound. |
| `OnDeconstructionAudio` | Audio event to play when block is deconstructed. This event is triggered whether the block is ground down at each stage. One shot sound. |
| `OnDestroyedAudio` | Audio event to play when block is fully destroyed. This should not be an explosion event, as this is handled by explosion effects. One shot sound. |
| `OnOffParameterName` | Parameter name for on/off state |
| `OnParameterValue` | Parameter value for on state |
| `OnUseAudio` | Audio event containing sounds related to this block. The exact sound to play depends on the current state of the block and is decided based on the audio parameters. |
| `ProcessOffValue` | Parameter value for process off state |
| `ProcessOnValue` | Parameter value for process on state |
| `ProcessParameterName` | Parameter name for process state |
| `UseRestart` | When true, will be restarted immediately when the block is working again, without waiting for end transitions. |

## A real one

`Vanilla\Assets\Templates\Blocks\BlockEffects\BlockEffectsComponentDefinition.def`

```json
{
  "Guid": "4c5e740b-35f4-4d29-8a23-ac484aa499b8",
  "OnDamagedBlockParticleEffect": [
    {
      "Key": "3ce2745e-0989-4256-86e6-76d5fa6100b7",
      "Value": {
        "HealthIntegrityLowerThreshold": 0,
        "HealthIntegrityUpperThreshold": 1,
        "ParticleEffects": [
          {
            "Key": "34f51798-45e7-45fd-b686-2193aa107733",
            "Value": {
              "ParticleEffect": "153c14c0-07c3-4bc2-b73e-0d848202dde7",
              "Dummy": null,
              "Scale": 1
            }
          },
          {
            "Key": "92d61473-88b0-416b-a1f0-272b0e1c4c8f",
            "Value": {
              "ParticleEffect": "d3f3bead-ff88-4359-9ef8-25058108c4d9",
              "Dummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
              "Scale": 4
            }
          }
        ]
      }
    }
  ],
  "OnFractureBlockParticleEffect": {
    "ParticleEffect": "cf82bb19-55be-4fb8-b251-888f57ded7fd",
    "Dummy": null,
    "Scale": 1
  },
  "FractureGroupsOnFractureBlockParticle": null,
  "OnConstructionStateChangedParticleEffect": {
    "ParticleEffect": "4cd12375-db35-4bee-a2b2-aa258a1eac57",
    "Dummy": null,
    "Scale": 1
  },
  "ConstructionStateChangedParticleEffectInterval": 1,
  "OnActivationParticleEffects": {
    "ParticleEffect": null,
    "Dummy": null,
    "Scale": 1
  },
  "OnUsedParticleEffects": {
    "ParticleEffect": null,
    "Dummy": null,
    "Scale": 1
  },
  "OnBlockDeathParticleEffect": {
    "ParticleEffect": null,
    "Dummy": "e9f28118-a0cf-4c6c-b6ad-2e0719e6cf5a",
    "Scale": 1
  },
  "OnUseAudio": null,
  "OnDamagedAudio": "event:/SFX/Explosions/DamageIncrementalMetal",
  "OnDestroyedAudio": null,
  "OnConstructionAudio": "event:/SFX/Progress/Progress_Construction",
  "OnDeconstructionAudio": "event:/SFX/Progress/Progress_Deconstruction",
  "BuildProgressAudioParameter": "123",
  "DamageIntegrityThresholds": [
    {
      "Key": "9b2ede73-9fd3-4e07-82d9-36c7cbe8cfe1",
      "Value": 0.25
    },
    {
      "Key": "d4996607-516d-4663-bcfc-0f9e596ec352",
      "Value": 0.5
    },
    {
      "Key": "81b27e83-6edd-485c-aba9-fb96cddc91a6",
      "Value": 0.75
    }
  ],
  "UseRestart": true,
  "OnOffParameterName": "OnOff",
  "OnParameterValue": "On",
  "OffParameterValue": "Off",
  "ProcessParameterName": "Process",
  "ProcessOnValue": 1,
  "ProcessOffValue": 0,
  "AudioStageConstructionValueFirst": 1,
  "AudioStageConstructionValueMid": 2,
  "AudioStageConstructionValueLast": 3,
  "HitDamageOverlay": "cb02cce0-f29f-4fe0-9e58-985691e6e70b"
}
```

Others: `Cockpit150_Client_BlockEffectsComponentDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='BlockEffectsComponentDefinitionObjectBuilder')
```
