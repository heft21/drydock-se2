# MagneticBlockEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Effects.MagneticBlockEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FailedStateParameterValue` | Value sent to FMOD Studio to play failed state audio. |
| `LockStateToggleParameter` | Audio event parameter to control if locking or unlocking. |
| `LockedStateParameterValue` | Value sent to FMOD Studio to play locked state audio. |
| `OnLockStateChangedAudio` | Audio event to play on changing lock state. One shot |
| `ReadyToLockStateParameterValue` | Value sent to FMOD Studio to play ready to lock state audio. |
| `UnlockedStateParameterValue` | Value sent to FMOD Studio to play unlocked state audio. |

## A real one

`Vanilla\Assets\Templates\Blocks\BlockEffects\MagneticBlockEffectsComponentDefinition.def`

```json
{
  "Guid": "7ad29674-0cb9-437c-a4e7-0ee10df558b6",
  "LockStateToggleParameter": "ready_lock_unlock",
  "LockedStateParameterValue": "lock",
  "UnlockedStateParameterValue": "unlock",
  "FailedStateParameterValue": "Not",
  "OnLockStateChangedAudio": "event:/SFX/Block/LandingGear"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MagneticBlockEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='MagneticBlockEffectsComponentDefinitionObjectBuilder')
```
