# GunToolDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.GunToolDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxADSAngleDeviation` | The maximum half cone angle that the projectile can deviate from the intended path when aiming down sights. |
| `Projectile` | The projectile the weapon will shoot when fired. |
| `ProjectileLead` | How much to lead the Projectile spawn position to prevent self-hitting |

## A real one

`Vanilla\Assets\Templates\CharacterTools\BaseDefinitions\DebugGunTool.def`

```json
{
  "Guid": "7cded4ae-2f66-4279-9078-0fd018bc721f",
  "CooldownTime": 0,
  "MaxAngleDeviation": 0,
  "BarrelDummyType": "6fc9829d-3ee4-4735-b229-e00157f67a42",
  "Recoil": 0,
  "Projectile": "e4f90b71-d9d1-4722-9ce7-6c3a23e198fa",
  "ProjectileLead": 0.2
}
```

Others: `GunToolDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('GunToolDefinitionObjectBuilder')
search_content('', type_contains='GunToolDefinitionObjectBuilder')
```
