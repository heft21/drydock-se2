# CharacterHitEffectsComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.Effects.CharacterHitEffectsComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `HitDamageOverlay` | Damage overlay to show when player takes damage |
| `OnHitAudio` | Audio event to play when player takes damage. One shot sound |

## A real one

`Vanilla\Assets\Characters\System\CharacterHitEffectsComponentDefinition.def`

```json
{
  "Guid": "14f7805a-f145-4e73-bd6a-68985e960eb7",
  "OnHitAudio": "event:/SFX/Character/VocPain",
  "OnDamageIndicatorAudio": "event:/SFX/Character/BulletHit",
  "OnCriticalHitAudio": "event:/SFX/Character/BulletHitHeadshot",
  "OnNearMissAudio": "event:/SFX/Character/BulletNearMiss",
  "CriticalHealthLoopAudio": "event:/SFX/Character/CriticalHealth",
  "CriticalHealthIntensityParameter": "Intensity",
  "HitDamageOverlay": "b8045b5b-5a92-4f7f-b1f5-b4488c3084fe",
  "HealthThreshold": 40,
  "MaxBrightnessHealthThreshold": 10,
  "HealthStepInterval": 5,
  "MinBrightness": 0.25,
  "MaxBrightness": 1,
  "BrightnessLerpTime": 2500000,
  "VignetteBitmap": "{G}13ed8ee6-6b8f-4e1d-9d03-097aa64aed15"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterHitEffectsComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterHitEffectsComponentDefinitionObjectBuilder')
```
