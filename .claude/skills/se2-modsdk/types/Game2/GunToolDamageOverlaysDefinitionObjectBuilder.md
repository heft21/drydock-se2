# GunToolDamageOverlaysDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Tools.Effects.GunToolDamageOverlaysDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Tools.Effects`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ProjectileHit` | Overlay shown when a projectile hits something |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\GunToolDamageOverlaysDefinition.def`

```json
{
  "Guid": "5ae8151d-fbe9-43e8-b108-6089db64b3fc",
  "ProjectileHit": "b2cc0d55-7f42-4667-9fa1-09b3dab24b06"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GunToolDamageOverlaysDefinitionObjectBuilder')
search_content('', type_contains='GunToolDamageOverlaysDefinitionObjectBuilder')
```
