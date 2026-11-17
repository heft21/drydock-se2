# WindTurbineDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production.WindTurbineDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Production`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BaseWeatherMultiplier` | The effectiveness of the wind turbine when there is no special weather condition, from 0 to 1. A value of 0.2 means that when there's no weather event, the overall wind turbine effectiveness will be at a max of 20%, while where there's a wind event the effectiveness will increase from 20% to 100% depending on the intensity of the event. |
| `LayersForGroundProbing` | Entity Layers that are considered when checking for the ground distance. Any other Entity with a layer not included on this collection will be ignored. |
| `LayersToIgnoreForClearance` | Entity Layers that are ignored when probing for clearance (occluders for the wind turbine). |
| `MaxOutput` | Maximum amount of the resource that can be produced. |
| `OcclusionDetection` | The distance (in meters) to query for wind blockers. |
| `OptimalAirDensity` | The minimum air density (in kg/m^3) for the turbine to produce its maximum output. Any value of air density below this will produce linearly less than the maximum output. |
| `OptimalDistanceToGroundHeight` | The distance to the ground height (in meters) for the turbine to produce its maximum output. Any value of height above this (if still on atmosphere) will produce the maximum output. Any value of height below this will produce linearly less than the maximum output. Values of height below the ground height will produce no energy output. |
| `ProbingRayCount` | Number of raycasts evenly distributed around the horizontal axis (2PI / N) used to probe clearance. |
| `ProductionPriority` | Priority of this block in the resource distribution system. |
| `ResourceType` | Type of resource that is produced. |
| `TurbineOffsetToProbe` | Minimum horizontal distance at which the turbine starts probing for other entities when checking for clearance. |
| `VerticalOffsetForClearance` | The vertical offset on the block to test for clearance. Probing starts at the top of the block, so the vertical offset points to its down direction. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\WindTurbine_WindTurbineDefinition.def`

```json
{
  "Guid": "c4b48497-9e8b-4af0-9213-147c33a46c2c",
  "ResourceType": "bcded093-f5c0-4997-af3a-a6fbd853ad66",
  "MaxOutput": 400,
  "ProductionPriority": {
    "Priority": 10
  },
  "OptimalDistanceToGroundHeight": 25,
  "OptimalAirDensity": 0.8,
  "OcclusionDetection": 20,
  "ProbingRayCount": 8,
  "BaseWeatherMultiplier": 0.8,
  "VerticalOffsetForClearance": 4,
  "TurbineOffsetToProbe": 5,
  "LayersToIgnoreForClearance": [
    {
      "Key": "fb42578b-c550-4529-8960-fdd3d906c3b4",
      "Value": "Characters"
    }
  ],
  "LayersForGroundProbing": [
    {
      "Key": "85fcc826-0e10-43d6-832b-6f181fd3b358",
      "Value": "Voxels"
    }
  ]
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WindTurbineDefinitionObjectBuilder')
search_content('', type_contains='WindTurbineDefinitionObjectBuilder')
```
