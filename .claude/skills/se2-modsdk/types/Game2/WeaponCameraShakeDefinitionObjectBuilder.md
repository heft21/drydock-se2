# WeaponCameraShakeDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.WeaponCameraShakeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ShakeSettings` | Camera shake settings for the weapon. |
| `ShotShakePower` | Camera shake power to deliver when weapon is fired. |

## A real one

`Vanilla\Assets\CharacterTools\DebugGun\WeaponCameraShakeDefinition.def`

```json
{
  "Guid": "efc92c24-6c88-4e93-b0a4-e72f2e3cebef",
  "ShakeSettings": "c1e752bf-f9d5-4109-9e14-ebbce7f1dfbc",
  "ShotShakePower": 2e-05
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WeaponCameraShakeDefinitionObjectBuilder')
search_content('', type_contains='WeaponCameraShakeDefinitionObjectBuilder')
```
