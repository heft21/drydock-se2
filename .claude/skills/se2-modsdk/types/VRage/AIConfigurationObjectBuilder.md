# AIConfigurationObjectBuilder

`VRage:Keen.VRage.AI.Definitions.AIConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.AI.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AgentHeight` | Minimum walkable height clearance (meters). Should match character capsule Height. |
| `AgentMaxClimb` | Maximum step height the agent can climb (meters). Should match character SupportDistance. |
| `AgentMaxSlope` | Maximum walkable slope angle (degrees). Should match character MaxSlopeAngle. |
| `AgentRadius` | Agent radius for navmesh erosion (meters). Should match character capsule Radius. |
| `CoverAnalysisTraceDepthHint` | Depth hint for cover analysis ray traces (meters). Default: 1.0. |
| `CoverBucketSize` | Spatial bucket size for cover point storage (meters). Default: 0.25. |
| `CoverMaxVerticalGap` | Maximum vertical gap in a wall before it is no longer considered solid cover (meters). Default: 0.2. |
| `CoverMinEdgeProximity` | Minimum distance from navmesh edge for a valid cover point (meters). Default: 0.3 (agent radius). |
| `CoverPeekMaxEdgeProximity` | Maximum distance from corner edge for peek cover (meters). Default: 1.0. |
| `CoverPeekMinHeight` | Minimum cover wall height for peek classification (meters). Default: 1.5. |
| `CoverPeekMinPeekGap` | Minimum gap width to peek through (meters). Default: 1.0. |
| `FullCoverMinHeight` | Minimum wall height to classify as full cover (meters). Default: 1.5 (standing height). |
| `LowCoverMaxHeight` | Maximum wall height for low/partial cover (meters). Default: 1.5 (above this = full cover). |
| `LowCoverMinHeight` | Minimum wall height to classify as low/partial cover (meters). Default: 0.5. |

## A real one

`Vanilla\Assets\System\AI\AIConfiguration.def`

```json
{
  "Guid": "5f4ff0b8-7123-43a4-be6d-ec73aaa9dc42",
  "NavMeshGenerationRadius": 40,
  "NavMeshTilesPerChunk": 1,
  "FullCoverMinHeight": 1.8,
  "LowCoverMinHeight": 0.5,
  "LowCoverMaxHeight": 1.8,
  "CoverMinEdgeProximity": 0.3,
  "CoverMaxVerticalGap": 0.2,
  "CoverBucketSize": 0.25,
  "CoverAnalysisTraceDepthHint": 1,
  "CoverPeekMinPeekGap": 0.5,
  "MaxThread": 4
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AIConfigurationObjectBuilder')
search_content('', type_contains='AIConfigurationObjectBuilder')
```
