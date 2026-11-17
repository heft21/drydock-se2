# CharacterThirdPersonAdapterDefinitionObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.CameraSystems.Adapters.CharacterThirdPersonAdapterDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.CameraSystems.Adapters`
- definitions using it: **1**

## What it is

Object builder for

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CharacterBoundingBox` | Approx character bounds. Influences min/max third person camera distance from player. |
| `CrouchedCollisionDetectionFocusPointOffset` | Local-space offset applied to the camera focus point when checking for camera obstructions. This is useful when the height of the observed Entity changed and obstruction needs to account for it. For example, when the character crouches. |
| `FirstPersonCameraOffsetCrouched` | Offset applied to camera position when it is switched to first person while crouching. |
| `FirstPersonSwitchBoundingBox` | When the camera collision detection pushes the camera inside this bounding box, the camera will switch to 1st person. |
| `FirstPersonSwitchBoundingBoxCrouched` | When the camera collision detection pushes the camera inside this bounding box when character is crouched, the camera will switch to 1st person. |
| `HideReticleAngle` | Angle at which the reticle should be hidden when the camera is rotated from default forward direction. If set to zero, reticle will be always visible. |
| `RelativeTransform` | Relative offset for the camera's placement. The offset is defined in right shoulder position. |
| `ThirdPersonCameraOffsetJetpack` | Local-space offset applied to camera focus point when jetpack is used. Can be used to compensate character being shifted up in source animation during flying. |

## A real one

`Vanilla\Assets\System\Camera\CharacterThirdPersonCamera\CharacterThirdPersonCameraAdapter.def`

```json
{
  "Guid": "9cc19cb2-a0e4-44fd-9372-df79923918c6",
  "CharacterBoundingBox": {
    "Min": {
      "X": -0.225,
      "Y": 0,
      "Z": -0.225
    },
    "Max": {
      "X": 0.225,
      "Y": 1.8,
      "Z": 0.225
    }
  },
  "FirstPersonSwitchBoundingBox": {
    "Min": {
      "X": -0.675,
      "Y": -0.45,
      "Z": -0.67499995
    },
    "Max": {
      "X": 0.675,
      "Y": 2.25,
      "Z": 0.675
    }
  },
  "FirstPersonSwitchBoundingBoxCrouched": {
    "Min": {
      "X": -0.675,
      "Y": -0.45,
      "Z": -0.675
    },
    "Max": {
      "X": 0.675,
      "Y": 1.75,
      "Z": 0.675
    }
  },
  "FirstPersonCameraOffsetCrouched": {
    "X": 0,
    "Y": -0.6,
    "Z": 0
  },
  "ThirdPersonCameraOffsetJetpack": {
    "X": 0,
    "Y": 0.2,
    "Z": 0
  },
  "CrouchedCollisionDetectionFocusPointOffset": {
    "X": 0,
    "Y": -0.5,
    "Z": 0
  },
  "HideReticleAngle": 0,
  "FirstPersonMaxYawAngle": 0,
  "FirstPersonCamera": "61ab743f-29cc-4790-a7b4-2cb34c979db2",
  "RelativeTransform": {
    "Transform": {
      "Position": {
        "X": 0.2,
        "Y": 1.8,
        "Z": -0.2575
      },
      "Orientation": {
        "X": 0,
        "Y": 0,
        "Z": 0,
        "W": 1
      }
    },
    "EulerHint": {
      "X": 0,
      "Y": 0,
      "Z": 0
    }
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterThirdPersonAdapterDefinitionObjectBuilder')
search_content('', type_contains='CharacterThirdPersonAdapterDefinitionObjectBuilder')
```
