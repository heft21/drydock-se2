# WheelColliderDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels.WheelColliderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.Wheels`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `WheelMass` | Mass of the wheel object. |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\DrivingWheel\DrivingWheelColliderDefinition.def`

```json
{
  "Guid": "b0fc3dbb-b18d-449c-b980-968987f58784",
  "WheelMass": 100
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('WheelColliderDefinitionObjectBuilder')
search_content('', type_contains='WheelColliderDefinitionObjectBuilder')
```
