# MeteorShowerSpawnerComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Weather.MeteorShowerSpawnerComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Weather`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ApproachDistance` | Distance from the impact point back along the incoming direction where meteors are spawned, effectively controlling the visible travel length of the meteor. |
| `HorizonAngleFromZenithRatio` | Controls how close to the horizon meteors are allowed to come. This is a dot-product threshold (sine-based) used when adjusting the sun direction to avoid trajectories that go below/too near the horizon relative to gravity. |
| `MeteorBlurCoefficient` | Scales how widely impact points are scattered around the event center. Higher values increase the effective hit area within the event bounding sphere. |
| `MinSpawnClearance` | Minimum clearance above terrain for meteor spawn points. If a computed spawn position is below this height above terrain, it is pushed upward. |
| `ProjectileDefinition` | Projectile definition used for each spawned meteor (spawned via ). |
| `SpawnCullingDistance` | Maximum distance from the weather event boundary at which meteor spawning is allowed. If no observer is within this distance, the spawn is skipped. Set to 0 to disable spawn culling. |
| `SpawnCullingObserverTag` | Observer tag used to find relevant entities for spawn culling. Meteors will not be spawned if no observer with this tag is within of the weather event area. This tag should be registered on players and cube grids so that meteors still occur near unattended bases. |
| `SpawnRate` | Time interval between meteor spawns while the weather event is active. |

## A real one

`Vanilla\Assets\System\Weather\MeteorShowerSpawnerComponentDefinition.def`

```json
{
  "Guid": "7ceb1d5c-90de-482f-b226-4131ea9cefd5",
  "ProjectileDefinition": "fb130746-5b7d-4d00-9521-dc43f836748e"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MeteorShowerSpawnerComponentDefinitionObjectBuilder')
search_content('', type_contains='MeteorShowerSpawnerComponentDefinitionObjectBuilder')
```
