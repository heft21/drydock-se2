# CharacterPhysicsEntityComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Characters.CharacterPhysicsEntityComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Characters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BaseHeight` | Height of the base section of the capsule |
| `BaseRadius` | Radius of the base section of the capsule |
| `Height` | Character capsule height |
| `HeightCrouched` | Character capsule height |
| `Radius` | Character capsule radius |
| `TopHeight` | Height of the top section of the capsule |
| `TopRadius` | Radius of the top section of the capsule |

## A real one

`Vanilla\Assets\Characters\System\CharacterPhysics.def`

```json
{
  "Guid": "80400e4a-57d6-4478-9b46-8a6fe652f5c9",
  "QualityType": "Character",
  "DestructionLayer": "75d8d0e8-4ea7-4751-9a52-4c665c71b1d3",
  "Material": "d99da81f-5ee1-4fa1-b96d-fcf0c18feef4",
  "EntityLayer": "Characters",
  "ActivationControl": "Automatic",
  "MaxDepenetrationSpeed": 1,
  "MaterialInAir": "661e0887-54b7-42d2-8b71-d24534e57576",
  "MaterialInAirResting": "6e67c09c-8100-46e6-9008-1052ee2a1f28",
  "JumpHeight": 0.8,
  "JumpReferenceGravity": 9.81,
  "AirtimeControl": 0.01,
  "BaseGroundVelocity": 10,
  "MaxVelocity": 310,
  "MaxSlopeAngle": 65,
  "SupportDistance": 0.5,
  "MinimumLandingDistance": 0.05,
  "StickyFactor": 1,
  "StickyTimeout": 1000000,
  "Mass": 80,
  "CenterOfMass": {
    "X": 0,
    "Y": 0.9,
    "Z": 0
  },
  "Simulated": true,
  "MinTeleportDistance": 1,
  "MinTeleportAngleDegrees": 2000,
  "MaxAcceleration": 200,
  "MaxAppliedForce": 1000000,
  "MinSurfaceDistanceExcess": 0.01,
  "MinMagbootsAlignmentAngle": 87,
  "MinGravityAlignmentAngle": 75,
  "MaxGravityAlignmentAngle": 30,
  "UseFiniteInertiaWhileFlying": true,
  "FlyingAngularInertiaMultiplier": 0.8,
  "LayersToIgnoreWhenCheckingForStanding": [
    {
      "Key": "0f15539a-19ef-4840-81e5-c6d150276a01",
      "Value": "Characters"
    }
  ],
  "Height": 1.74,
  "HeightCrouched": 1.24,
  "Radius": 0.45,
  "BaseHeight": 0.525,
  "TopHeight": 0.2,
  "BaseRadius": 0.2,
  "TopRadius": 0.35
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('CharacterPhysicsEntityComponentDefinitionObjectBuilder')
search_content('', type_contains='CharacterPhysicsEntityComponentDefinitionObjectBuilder')
```
