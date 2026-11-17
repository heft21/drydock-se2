# DoorSegmentTransformSLERPDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Doors.DoorSegmentTransformSLERPDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Doors`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ClosedPositionDummy` | Dummy on the parent model representing the closed position of the door segment. |
| `OpenPositionDummy` | Dummy on the parent model representing the open position of the door segment. |

## A real one

`Vanilla\Assets\Blocks\Doors\SlideDoorNarrow\250\Subparts\SlideDoorNarrow_250_LeftDoor_Client_DoorSegmentTransformSLERPDefinition.def`

```json
{
  "Guid": "f90ed091-47e1-4c3f-84fd-0b1c769ea76a",
  "ClosedPositionDummy": "4ac1d272-c931-4ab3-bebe-355a850437a0",
  "OpenPositionDummy": "75c525e6-d31b-4f19-ab95-cd63621b8e71"
}
```

Others: `SlideDoorNarrow_250_RightDoor_Client_DoorSegmentTransformSLERPDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('DoorSegmentTransformSLERPDefinitionObjectBuilder')
search_content('', type_contains='DoorSegmentTransformSLERPDefinitionObjectBuilder')
```
