# AmmoDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProjectileSystems.AmmoDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProjectileSystems`
- definitions using it: **5**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Capacity` | Number of shots we get for each unit of ammo resource/item consumed |
| `ProjectileDefinition` | Projectile fired by this ammo type |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\Projecticles\AmmoRifle.def`

```json
{
  "Guid": "c95b8a8b-4741-4147-99ad-2a8f4b500a05",
  "Capacity": 30,
  "ProjectileDefinition": "12953d5b-2c87-4f9b-8375-edbe4b25fbdb",
  "ExplosiveRisk": 1
}
```

Others: `AmmoPistol`, `AmmoGatling`

---

Read it with the MCP server rather than by hand:

```
describe_type('AmmoDefinitionObjectBuilder')
search_content('', type_contains='AmmoDefinitionObjectBuilder')
```
