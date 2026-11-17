# ProjectileWeaponAudioDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Weapons.ProjectileWeaponAudioDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Weapons`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FireAudioIsLooped` | will be considered as a looped sound if true. |
| `OnFireAudio` | Audio event to play when firing gun tool. One-shot or looped sound depending on |
| `OnOutOfAmmoAudio` | Audio event to play when can't reload. One-shot sound |
| `OnReloadAudio` | Audio event to play when reloading gun tool. One-shot sound |
| `OnShootingAudio` | Audio event to play when shooting target. Not to be confused with , which is for a single projectile. This one should be used for a constant looping sound while shooting Looped sound |
| `ShootingAudioEndParameter` | Parameter name to send to when aligning is done |
| `ShootingAudioEndValue` | Parameter value to send with when aligning is done |
| `ShootingAudioStartValue` | Parameter value to send with when aligning starts |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ProjectileWeaponAudioDefinition.def`

```json
{
  "Guid": "b3769b73-1829-4dcf-8749-3c6e91319d3a",
  "OnFireAudio": null
}
```

Others: `ProjectileWeaponAudioDefinition`, `DebugGun_Client_ProjectileWeaponAudioDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectileWeaponAudioDefinitionObjectBuilder')
search_content('', type_contains='ProjectileWeaponAudioDefinitionObjectBuilder')
```
