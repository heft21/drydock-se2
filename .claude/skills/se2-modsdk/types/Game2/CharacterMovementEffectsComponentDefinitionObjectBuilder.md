# CharacterMovementEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.Effects.CharacterMovementEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterVelocityAudioParameter` | Audio parameter to define character velocity in events such as |
| `DummyJetpackThrusts` | Dummy-linked thruster effects for character jetpack. Used when is true. |
| `FootstepAnimationEvent` | Animation event considered as footsteps |
| `FootstepAnimationLayerIndex` | Animation layer index to consider for footsteps |
| `FootstepDebounceTime` | Used to prevent double footstep animation events in quick succession |
| `GroundTypeAudioParameter` | Audio parameter to define material type on footsteps |
| `IdleAudio` | Audio event to play when thrusters are idle. This is launched as soon as jetpacks are turned on. This plays in parallel to the actual thrust audio when character is moving. Looped sound. Uses parameter with and to start and stop the loop. |
| `JetpackIdlePlayAudioParameter` | Audio event parameter to control if jetpack idle loop is played or not. |
| `JetpackIdlePlayAudioParameterOffValue` | Value sent to FMOD Studio to stop jetpack idle loop. |
| `JetpackIdlePlayAudioParameterOnValue` | Value sent to FMOD Studio to play jetpack idle loop. |
| `JetpackThrusts` | Thruster effects for character jetpack |
| `JumpAnimationEvent` | Animation event considered as jumping |
| `LandAnimationEvent` | Animation event considered as landing |
| `LandingParticleEffects` | Particle effect to spawn on landing. Authored as a single effect whose emitter timeline keys vary by intensity; FixEffectTime selects the timeline position from the fall distance. |
| `MagbootsAudioParameter` | Audio parameter to layer magboot audio on footsteps |
| `MagbootsPhysicsMaterial` | Physics material name needed to play magboot audio |
| `MagbootsProximityAudioAngle` | Maximum angle from parallel that the character need to be from a surface's normal to play |
| `MaxLandingEffectFallDistance` | Fall distance (meters) mapped to the end of the landing effect timeline (FixEffectTime fraction 1). 0 m maps to timeline 0; greater distances clamp to 1. |
| `OnCrouchDownAudio` | Audio event to play on crouching down. One-shot sound |
| `OnCrouchFootstepAudio` | Audio event to play on footstep when crouched. One-shot sound. Uses parameter to specify what ground the character is on |
| `OnCrouchUpAudio` | Audio event to play on crouching up. One-shot sound |
| `OnFootstepAudio` | Audio event to play on footstep. One-shot sound. Uses parameter to specify what ground the character is on |
| `OnGroundOnAudio` | Audio event to play on touching ground from other character states. One-shot sound. Uses parameter to specify what ground the character is on |
| `OnJetpackOffAudio` | Audio event to play on deactivating jetpack. One-shot sound |
| `OnJetpackOnAudio` | Audio event to play on activating jetpack. One-shot sound |
| `OnJumpAudio` | Audio event to play on jump. One-shot sound |
| `OnMagbootsOffAudio` | Audio event to play on deactivating magboots. One-shot sound |
| `OnMagbootsOnAudio` | Audio event to play on activating magboots. One-shot sound |
| `OnMagbootsProximityAudio` | Audio event to play magboots are enabled but not active. One-shot sound |
| `OnSprintAudio` | Audio event to play on sprint. One-shot sound |
| `UseDummyJetpackThrusters` | When true, use (dummy-linked) instead of . |

## A real one

`Vanilla\Assets\Characters\System\PrefabCharacterClient_CharacterMovementEffectsComponentDefinition.def`

Too large to inline. Fields present:

`CharacterVelocityAudioParameter`, `DummyJetpackThrusts`, `FootstepAnimationEvent`, `FootstepAnimationLayerIndex`, `FootstepDebounceTime`, `FootstepParticleEffects`, `GroundTypeAudioParameter`, `Guid`, `IdleAudio`, `JetpackIdlePlayAudioParameter`, `JetpackIdlePlayAudioParameterOffValue`, `JetpackIdlePlayAudioParameterOnValue`, `JetpackThrusts`, `JumpAnimationEvent`, `LandAnimationEvent`, `LandingParticleEffects`, `MagbootsAudioParameter`, `MagbootsPhysicsMaterial`, `MagbootsProximityAudioAngle`, `MaxLandingEffectFallDistance`, `OnCrouchDownAudio`, `OnCrouchFootstepAudio`, `OnCrouchUpAudio`, `OnFootstepAudio`, `OnGroundOnAudio`, `OnJetpackOffAudio`, `OnJetpackOnAudio`, `OnJumpAudio`, `OnMagbootsOffAudio`, `OnMagbootsOnAudio`, `OnMagbootsProximityAudio`, `OnSprintAudio`, `UseDummyJetpackThrusters`

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterMovementEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterMovementEffectsComponentDefinitionObjectBuilder')
```
