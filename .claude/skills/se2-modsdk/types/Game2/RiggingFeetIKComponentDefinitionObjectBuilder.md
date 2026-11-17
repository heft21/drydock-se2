# RiggingFeetIKComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Character.RiggingFeetIKComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Character`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Characters\System\IK\PrefabCharacterClient_RiggingFeetIKComponentDefinition.def`

```json
{
  "Guid": "0d78d49a-e884-4286-9728-a12801ddb33d",
  "DescentSlopeAngleThreshold": 50,
  "Bones": [
    {
      "Key": "89e876ad-a1f6-4da0-b3b2-c6ff88d7704a",
      "Value": "fe930ba5-bf7b-4061-90d3-8679fadcf694"
    },
    {
      "Key": "d44fca43-87b8-4152-a559-cd70aa352e99",
      "Value": "976e7fc7-8952-41bb-ae17-9bb16f64ac05"
    }
  ],
  "RootBoneName": "Root_M",
  "MaxFootHeight": 0.5,
  "MaxFootHeightRelativeToHip": -0.1,
  "MaxSkeletonDescent": 0.45,
  "SurfaceDetectionExcessDistance": 0.6,
  "ActivationSmoothingTime": 3000000,
  "SkeletonDescendAverageWindow": 2000000,
  "SurfaceNormalAverageWindow": 1000000,
  "GroundOffset": 0,
  "FootSurfaceOrientationInfluenceMaxHeight": 0.2,
  "OptimizationRaycastDistance": 40,
  "OptimizationDisableDistance": 100
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RiggingFeetIKComponentDefinitionObjectBuilder')
search_content('', type_contains='RiggingFeetIKComponentDefinitionObjectBuilder')
```
