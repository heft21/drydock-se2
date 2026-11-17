# DamageOverlayDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Damage.DamageOverlayDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Damage`
- definitions using it: **3**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FadeOutTime` | Time to fade out the screen from UI |
| `ReticleType` | Optional reticle type to be displayed |
| `Screen` | Screen to be displayed |

## A real one

`Vanilla\Assets\UI\Screens\DamageOverlays\GridDamageOverlayDefinition.def`

```json
{
  "Guid": "cb02cce0-f29f-4fe0-9e58-985691e6e70b",
  "Screen": "Game2:Keen.Game2.Client.UI.Damage.Overlays.GridHitDamageOverlayScreen",
  "FadeOutTime": 30000000,
  "ReticleType": null
}
```

Others: `CharacterHitDamageOverlayDefinition`, `ProjectileHitDamageOverlayDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DamageOverlayDefinitionObjectBuilder')
search_content('', type_contains='DamageOverlayDefinitionObjectBuilder')
```
