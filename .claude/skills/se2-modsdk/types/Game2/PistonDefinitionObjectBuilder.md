# PistonDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.PistonDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AttachAngleLimit` | Cosine of maximum allowed angle difference when attaching the top part. Example: 1 - base and top must be exactly aligned to connect 0 - top can be at most perpendicular to base to connect -1 - top can be in any orientation to connect It is advised to keep values below, but close to 1 to avoid violent snapping, yet give some leeway in alignment. |
| `DistanceMax` | Minimum extension of the piston head. |
| `DistanceMin` | Minimum extension of the piston head. |
| `ForceMax` | Maximum force the piston can apply when attempting to push/pull the connected part, limiting the acceleration. |
| `VelocityMax` | Maximum movement speed of the piston along its axis |
| `VelocityMin` | Minimum movement speed of the piston along its axis |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\PistonDefinition.def`

```json
{
  "Guid": "069a0fed-5810-4a26-bca4-e06ce3f63c2f",
  "ConnectionGroups": [
    {
      "Key": "82930751-abff-480f-a8f9-273a549ef53e",
      "Value": "262d50d2-7b5b-4939-a81b-70f731d0e252"
    },
    {
      "Key": "6400d941-3a93-4a3e-950b-9428fdbafc69",
      "Value": "2ed2d414-fedb-42a2-bc75-2b26417e1346"
    },
    {
      "Key": "aeb994e3-c881-415e-a6e9-50505bb75911",
      "Value": "a5bd777b-b184-41c9-af22-284d7178c267"
    }
  ],
  "AllowedTopTypes": [
    "ebb17bc8-8660-47e2-b530-851468acadb2"
  ],
  "TopPrefab": null,
  "AttachQuerySize": 1,
  "DistanceMin": 0,
  "DistanceMax": 15,
  "VelocityMin": -10,
  "VelocityMax": 10,
  "ForceMax": 100000000,
  "AttachAngleLimit": 0.985
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PistonDefinitionObjectBuilder')
search_content('', type_contains='PistonDefinitionObjectBuilder')
```
