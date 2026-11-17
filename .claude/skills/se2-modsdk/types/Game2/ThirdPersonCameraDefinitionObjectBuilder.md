# ThirdPersonCameraDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Modes.ThirdPersonCameraDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Modes`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AngularSpeed` | Additional modifier affecting view rotation speed, layered on top of mouse input |
| `CameraDistanceAnimationSpeedFactor` | Affects how quickly the camera will animate towards its ideal/desired distance This is a percentage of the the gap between current camera distance and ideal distance |
| `CameraRadius` | Distance by which the camera is move towards the target when the camera is obstructed. Used to fix environment probe clipping in the voxels. |
| `DefaultPercentageDistanceFromEntity` | Percentage value between 0-100. Indicates at what percentage between max and min distances the camera will be placed at by default. E.g. if set to 0, the camera will be placed at the min distance, and if at 100 it will be placed at the max distance. |
| `DefaultPitchLengthModifier` | Reduces the pitch of the default camera angle logarithmically depending on the length of the entity Higher values means the pitch will be flattened more quickly |
| `DefaultThirdPersonCameraAngle` | Default angles. Pitch value can get overridden by . |
| `DynamicCameraHeightDistanceCheck` | Max distance to check for obstructions along camera view direction, when the camera height relative to entity needs to be adjusted to unblock it. It is a multiplier of the controlled entity size. |
| `EntitySizeZoomSpeedMultipier` | DEPRECATED - Multiplier for increasing the speed of zoom on larger grids. |
| `FirstPersonCameraOffset` | Offset for 1st person camera that the 3rd person camera switches to if obstacle detection pushes the camera inside the observer object. |
| `IgnoreCollisionVolumeThreshold` | Ignores camera collisions for objects below the specified volume |
| `IgnoreGridsInsideBoundingBoxVolumeThreshold` | If current bounding box is larger than this, ignore collisions for grids inside the bounding box. |
| `InputContextDefinition` | Third person camera input context settings |
| `LayersToCheckForObstaclesInsideVolume` | Entity layers that count as obstacles even inside the observed grid volume, e.g. to correctly detect voxels intersecting a static grid. |
| `LayersToIgnoreWhenProbingForObstacles` | Entity Layers to ignore when checking the obstacles between the camera target and its position. |
| `MaxFirstPersonCameraBounds` | Maximum size of the bounds used to detect when to switch to first person mode |
| `MaxPercentageDistanceFromEntity` | Percentage value, e.g. if set to 150, the maximal allowed distance OBB.HalfExtent.Max * 1.5. |
| `MaxY` | Maximum vertical angle that the camera can rotate to |
| `MinAbsoluteDistanceFromEntity` | Absolute value, e.g. if set to 2, the minimum allowed distance is OBB.HalfExtent.Max + 2. |
| `MinCameraDistanceIncrementPercent` | Percentage of camera distance to add to current camera distance during a single zoom tick, for smallest scroll input |
| `MinY` | Minimum vertical angle that the camera can rotate to. |
| `MouseDelta` | 2D axis input for view rotation |
| `MouseSensitivity` | Mouse sensitivity multiplier for camera rotation around target |
| `NearPlaneCollisionExtension` | Defines by how much should the near plane collider be extended so that it can take into account voxel tessellation. In meters. |
| `ObstructedCameraSnapBackDelay` | How much time it takes for an obstructed camera to return to its original position when the obstructions are cleared. |
| `ObstructionSnapBackSmoothingCoefficient` | How smoothly does the camera snap back to the unobstructed position when no longer obstructed. Values from 0 to 1, 1 = no smoothing. |
| `ResetFreeLook` | Input to reset camera offset around target to its default state |
| `ResetFreeLookThreshold` | Threshold time for the double-tap of AltPres to reset the view |
| `RotationSpringStiffnessLag` | Spring stiffness value representing camera rotation lag. Values from 0 to 1, 1 means no lag. |
| `SwitchShoulderSpeed` | How fast the camera moves when switching shoulders. It is a percentage of distance from current shoulder position to target shoulder position added to in a single zoom tick |
| `ThirdPersonCameraDistanceMaxDeltaPerSecond` | DEPRECATED - Max distance change per second. |
| `ThirdPersonCameraDistanceMultiplier` | DEPRECATED - Multiplier for tweaking camera move speed when adjusting camera distance. |
| `ThirdPersonZoomChange` | Input to adjust camera tracking distance to target |

## A real one

`Vanilla\Assets\System\Camera\AnyGridThirdPersonCamera\ThirdPersonCamera.def`

```json
{
  "Guid": "6f36f44b-9793-44c1-8356-984901b14f89",
  "MinAbsoluteDistanceFromEntity": 1,
  "DefaultPercentageDistanceFromEntity": 2.44,
  "MaxPercentageDistanceFromEntity": 2500,
  "MaxY": 1.3962634,
  "MinY": -1.5707964,
  "DefaultThirdPersonCameraAngle": {
    "X": 0,
    "Y": -0.45,
    "Z": 0
  },
  "DefaultPitchLengthModifier": 0.25,
  "MouseSensitivity": 0.002,
  "AngularSpeed": 1,
  "InputContextDefinition": "aca4c9ac-04d4-4f45-9e30-3505fe2fd5ee",
  "FreeLookInputContextDefinition": "b7e4c2a9-3f16-4d8b-9c05-7a1e2d6f48b3",
  "ObstructedCameraSnapBackDelay": 0,
  "IgnoreCollisionVolumeThreshold": 0.5,
  "IgnoreGridsInsideBoundingBoxVolumeThreshold": 10,
  "RotationSpringStiffnessLag": 0.09375,
  "NearPlaneCollisionExtension": 0.15,
  "CameraRadius": 0.04,
  "MouseDelta": "45dcca79-8b8b-461d-b72f-6967c44b2683",
  "ThirdPersonZoomChange": "7256c48a-ae15-42eb-80b4-3489e8a953ad",
  "ResetFreeLook": "b03bdab2-0082-4c38-b272-c2156ab765f2",
  "ResetFreeLookThreshold": 4999997,
  "ObstructionSnapBackSmoothingCoefficient": 0.25,
  "FirstPersonCameraOffset": {
    "X": 0,
    "Y": 0,
    "Z": 0
  },
  "MaxFirstPersonCameraBounds": {
    "Min": {
      "X": -5,
      "Y": -5,
      "Z": -5
    },
    "Max": {
      "X": 5,
      "Y": 5,
      "Z": 5
    }
  },
  "CameraDistanceAnimationSpeedFactor": 0.1825,
  "MinCameraDistanceIncrementPercent": 0.33,
  "SwitchShoulderSpeed": 0.2,
  "DynamicCameraHeightDistanceCheck": 3,
  "LayersToIgnoreWhenProbingForObstacles": [
    {
      "Key": "c467b9c0-0636-4a5b-b8e2-bdd62318966a",
      "Value": "Characters"
    },
    {
      "Key": "aefbf263-aae3-425f-9e89-018d69c16055",
      "Value": "FloatingObjects"
    },
    {
      "Key": "f10fd560-bbe0-4683-a3b6-a343ca625b62",
      "Value": "DeadRagdolls"
    },
    {
      "Key": "995e7f48-950a-48aa-81a5-d0c52d84236f",
      "Value": "Debris"
    },
    {
      "Key": "bfc66406-5adb-4e39-b61e-455b08d4af3f",
      "Value": "FloraDebris"
    },
    {
      "Key": "2228cdac-4c95-4610-9f41-ddd3598a24b2",
      "Value": "Ragdolls"
    }
  ],
  "LayersToCheckForObstaclesInsideVolume": [
    {
      "Key": "605e2c29-ad91-4ac2-92cd-8ec098c7c408",
      "Value": "Voxels"
    }
  ],
  "ThirdPersonCameraDistanceMaxDeltaPerSecond": 300,
  "ThirdPersonCameraDistanceMultiplier": 1.2,
  "EntitySizeZoomSpeedMultipier": 10
}
```

Others: `CharacterThirdPersonCamera`

---

Read it with the MCP server rather than by hand:

```
describe_type('ThirdPersonCameraDefinitionObjectBuilder')
search_content('', type_contains='ThirdPersonCameraDefinitionObjectBuilder')
```
