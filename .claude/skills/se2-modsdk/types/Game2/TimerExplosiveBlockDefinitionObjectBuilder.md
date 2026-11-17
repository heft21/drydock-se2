# TimerExplosiveBlockDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Weapons.TimerExplosiveBlockDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Weapons`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DefaultTimeToExplosion` | Default time to explode the block. |

## A real one

`Vanilla\Assets\Blocks\Warheads\50\Warhead50_TimerExplosiveBlockDefinition.def`

```json
{
  "Guid": "e6bff6ff-0c8d-4c5e-8fc3-332728122143",
  "Explosion": "613fb81e-fe8d-40a7-9058-61c93c7cca4a",
  "MinimumIntegrityForExplosion": 0.5,
  "DestroyInExplosionRange": true,
  "UseExtendedLightRadius": true,
  "DefaultTimeToExplosion": 300000000
}
```

Others: `Warhead250_TimerExplosiveBlockDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('TimerExplosiveBlockDefinitionObjectBuilder')
search_content('', type_contains='TimerExplosiveBlockDefinitionObjectBuilder')
```
