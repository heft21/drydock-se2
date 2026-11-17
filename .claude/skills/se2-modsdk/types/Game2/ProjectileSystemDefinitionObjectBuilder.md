# ProjectileSystemDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.ProjectileSystems.ProjectileSystemDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.ProjectileSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ExplosionCullingObserverTag` | Observer tag used for explosion culling. When a simulated projectile has a non-zero , this tag is used to query the nearest observer. If none is close enough, the explosion is skipped. |
| `HitscanLimitParameterName` | Name of the parameter specifying the value of the hitscan limit. |
| `HitscanLimitReachedMessageTextId` | Localization text ID for the hitscan projectile limit reached message text. |
| `HitscanProjectilesLimit` | The maximum number of hitscan projectiles that can be simulated in a frame. |
| `ProjectileSystemMessageTitleId` | Localization text ID for the projectile system message title. |
| `SimulatedLimitParameterName` | Name of the parameter specifying the value of the simulated limit. |
| `SimulatedLimitReachedMessageTextId` | Localization text ID for the simulated projectile limit reached message text. |
| `SimulatedProjectilesLimit` | The maximum number simulated projectiles that can be simulated in a frame. |

## A real one

`Vanilla\Assets\System\Projectiles\ProjectileSystem.def`

```json
{
  "Guid": "111a97db-1f47-4e93-aaef-724296e369c7",
  "HitscanProjectilesLimit": 256,
  "SimulatedProjectilesLimit": 256,
  "ProjectileSystemMessageTitleId": "ProjectileSystemMessageTitle",
  "HitscanLimitReachedMessageTextId": "HitscanLimitReachedMessage",
  "HitscanLimitParameterName": "HitscanLimit",
  "SimulatedLimitReachedMessageTextId": "SimulatedProjectileLimitReachedMessage",
  "SimulatedLimitParameterName": "SimulatedProjectileLimit"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ProjectileSystemDefinitionObjectBuilder')
search_content('', type_contains='ProjectileSystemDefinitionObjectBuilder')
```
