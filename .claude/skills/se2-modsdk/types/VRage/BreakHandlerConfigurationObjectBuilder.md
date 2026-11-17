# BreakHandlerConfigurationObjectBuilder

`VRage:Keen.VRage.Physics.Definitions.BreakHandlerConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Physics.Definitions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `CollisionSpeedThreshold` | If bodies in a collision have their separation contact speed below this value, the collision between them will not be considered for destructions. |
| `DefaultLayer` | The default break handler layer that is applied when no specific layer is assigned. |
| `LayerMask` | Matches layers that interact with each other. Layer pairs that are not configured here will not break when bodies corresponding to them collide. |
| `MaximumWeldingVelocity` | Velocity past which welding is disabled by destructions. |
| `RestitutionForDestructions` | Restitution used for bodies being destroyed. They will bounce with a percent of the energy spent on the destruction and velocity reduction. Example: With value of 0.1 (10%), a body at 100 m/s crashing against a wall will bounce with a velocity of 10 m/s. |
| `StepCount` | The amount of steps the break handler does for finding breached groups. More steps result in a better quality, but have a higher performance impact. |

## A real one

`Engine\Assets\Configurations\Collision\BreakHandlerConfiguration.def`

```json
{
  "Guid": "a5603acd-70a3-444e-891f-0145ea6fbc19",
  "DefaultLayer": "6a9dfefe-2b7b-4bee-b767-cba4b5f54d0e",
  "LayerMask": [
    {
      "Key": "a3e153ee-4b12-4e27-80a4-ad013cfe02fa",
      "Value": {
        "LayerA": "6a9dfefe-2b7b-4bee-b767-cba4b5f54d0e",
        "LayerB": "6a9dfefe-2b7b-4bee-b767-cba4b5f54d0e"
      }
    },
    {
      "Key": "03f30835-bffc-4faf-9191-1c5ebc609322",
      "Value": {
        "LayerA": "6a9dfefe-2b7b-4bee-b767-cba4b5f54d0e",
        "LayerB": "a02aebf9-2641-4823-ad2d-edfdc6e3e6de"
      }
    },
    {
      "Key": "25bdc379-bb10-4dbf-bd19-c3a4526675e6",
      "Value": {
        "LayerA": "6a9dfefe-2b7b-4bee-b767-cba4b5f54d0e",
        "LayerB": "263951fe-9c25-4ba7-ac46-67bef306a0fd"
      }
    },
    {
      "Key": "1dda09d2-0a7f-4d92-8f8c-a6a3634dafc8",
      "Value": {
        "LayerA": "263951fe-9c25-4ba7-ac46-67bef306a0fd",
        "LayerB": "263951fe-9c25-4ba7-ac46-67bef306a0fd"
      }
    },
    {
      "Key": "023199ed-3131-4bf3-a187-79e703323d0b",
      "Value": {
        "LayerA": "a02aebf9-2641-4823-ad2d-edfdc6e3e6de",
        "LayerB": "263951fe-9c25-4ba7-ac46-67bef306a0fd"
      }
    }
  ],
  "CollisionSpeedThreshold": 5,
  "StepCount": 4,
  "RestitutionForDestructions": 0.25,
  "MinimumPenetrationAllowed": 0.1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BreakHandlerConfigurationObjectBuilder')
search_content('', type_contains='BreakHandlerConfigurationObjectBuilder')
```
