# HingeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.HingeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AttachAngleLimit` | Cosine of maximum allowed angle difference when attaching the top part. Example: 1 - base and top must be exactly aligned to connect 0 - top can be at most perpendicular to base to connect -1 - top can be in any orientation to connect It is advised to keep values below, but close to 1 to avoid violent snapping, yet give some leeway in alignment. |
| `ForceMax` | Maximum force the hinge can apply when attempting to rotate connected part, limiting the acceleration. |
| `Limits` | Optional minimum and maximum angle deviation from resting position. No limits allow complete rotation (rotor) X is minimum angle in degrees, defined in range [-180, 180] Y is maximum angle in degrees, defined in range [-180, 180] |
| `VelocityMax` | Maximum rotation speed. |
| `VelocityMin` | Minimum rotation speed. |
| `VerticalOffsetMax` | Maximum possible vertical offset along the rotation axis that can be set for the block. /// Note: if and are equal, offset is not configurable in terminal. |
| `VerticalOffsetMin` | Minimum possible vertical offset along the rotation axis that can be set for the block. Note: if and are equal, offset is not configurable in terminal. |
| `WrapAngle` | When true, negative angle values are wrapped back to positive values |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\HingeDefinition.def`

```json
{
  "Guid": "6259b0bf-4e5f-4394-834f-80f43f128fe7",
  "ConnectionGroups": [
    {
      "Key": "b720682b-6b3f-499e-b7c2-f5104e1d82e1",
      "Value": "262d50d2-7b5b-4939-a81b-70f731d0e252"
    },
    {
      "Key": "f78b9c8a-865d-4195-97f3-dba8b9fd07b0",
      "Value": "2ed2d414-fedb-42a2-bc75-2b26417e1346"
    },
    {
      "Key": "71623e15-bd0e-4b85-be05-3d4e7b68eec9",
      "Value": "a5bd777b-b184-41c9-af22-284d7178c267"
    }
  ],
  "AllowedTopTypes": [
    "1a87027d-8857-4cc8-9b16-bef26d04a1fd"
  ],
  "TopPrefab": null,
  "AttachQuerySize": 1,
  "Limits": {
    "X": 0,
    "Y": 180
  },
  "VelocityMin": -6.28,
  "VelocityMax": 6.28,
  "ForceMax": 1000000,
  "AttachAngleLimit": 0.985,
  "VerticalOffsetMin": 0,
  "VerticalOffsetMax": 0
}
```

Others: `Rotors_HingeDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('HingeDefinitionObjectBuilder')
search_content('', type_contains='HingeDefinitionObjectBuilder')
```
