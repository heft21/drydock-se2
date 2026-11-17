# WindGeneratorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.RangedAffectGenerators.Wind.WindGeneratorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.RangedAffectGenerators.Wind`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BaseSpeed` | Base ambient wind speed, in m/s, applied when no gust is active. |
| `FalloffStartDistance` | Distance from the generator origin at which edge-of-event strength attenuation begins. Inside this radius the wind is at full strength. Between this and it linearly fades to zero. |
| `MaxGustDuration` | Maximum duration of a single gust (full ramp), in seconds. |
| `MaxGustInterval` | Maximum delay between consecutive gusts, in seconds. |
| `MaxGustStrength` | Maximum gust speed multiplier reached at gust peak. |
| `MaxOccludedEntities` | Maximum number of affected entities that receive active occlusion sampling. Sorted by distance to the nearest observer. The closest are sampled normally. Anything beyond N has its occlusion locked and is treated as fully sheltered. (no wind force) |
| `MaxSamples` | Maximum number of occlusion samples per entity. Larger grids with bigger projected areas fan out up to this count to capture partial shadowing. |
| `MinAffectAcceleration` | Peak wind acceleration below which an entity is unaffectable by this generator and gets skipped: no occlusion entry, no force, no round-robin slot. |
| `MinGustDuration` | Minimum duration of a single gust (full ramp), in seconds. |
| `MinGustInterval` | Minimum delay between consecutive gusts, in seconds. |
| `MinGustStrength` | Minimum gust speed multiplier. A multiplier on . |
| `MinSamples` | Minimum number of occlusion samples per entity. Floating objects with a tiny silhouette still take at least this many ring-buffer slots. |
| `ObserverTag` | Observer tag used to gate occlusion raycasts and force application by distance. The tag must be registered on players so the wind sim goes quiet when no observer is around. |
| `OcclusionCullDistance` | Beyond this distance from the generator to the nearest observer, the sparse occlusion update skips entirely (no raycasts dispatched for any affected entity). |
| `OcclusionEnabled` | When true, wind strength on each affected entity is multiplied by an occlusion factor derived from the environment around the entity (terrain, structures, etc.). |
| `OcclusionRaysPerFrame` | Number of occlusion raycasts dispatched per frame, total, across all affected entities. Entities are round-robined in observer distance order: each frame the next N entities each get one ray, and after a full pass through the active set the per-entity ring buffer slot advances. Capped at the active entity count so no entity fires twice in the same frame. |
| `OcclusionStrengthMultiplier` | Strength multiplier applied when an entity is fully occluded. 0.0 = no wind in fully sheltered spots, 1.0 = occlusion has no effect. Only used when is true. |
| `RevalidationIntervalSeconds` | Period in seconds between re evaluations of each affected entity's negligibility (handles grids gaining or losing blocks while inside the sphere). |
| `SamplesPerSqMeter` | Sample density along the upwind facing projected area. Entry sample count = ceil(area * SamplesPerSqMeter), clamped to [, ]. |

## A real one

`Vanilla\Assets\System\Weather\SandStormWindGeneratorDefinition.def`

```json
{
  "Guid": "873e0247-99f9-45cf-87b9-41947fe0d3e2",
  "MaxAffectDistance": 100000,
  "TriggerSettings": null,
  "BaseSpeed": 25,
  "MinGustStrength": 1,
  "MaxGustStrength": 1.5,
  "MinGustInterval": 4,
  "MaxGustInterval": 8,
  "MinGustDuration": 1,
  "MaxGustDuration": 3,
  "FalloffStartDistance": 0,
  "OcclusionEnabled": true,
  "OcclusionStrengthMultiplier": 0
}
```

Others: `SnowStormWindGeneratorDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('WindGeneratorDefinitionObjectBuilder')
search_content('', type_contains='WindGeneratorDefinitionObjectBuilder')
```
