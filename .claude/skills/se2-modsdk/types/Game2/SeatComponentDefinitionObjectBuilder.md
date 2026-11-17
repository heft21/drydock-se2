# SeatComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Pilotable.SeatComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Pilotable`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ConveyorSubgraphNodeIndex` | Optional index referencing a node within the of the This node will be accessed by the pilot when attempting to transfer or use items in inventories. If null, the pilot does not have access to the inventory. Every ConveyorSubgraph has at least node with index 0. |
| `Inventory` | Optional Inventory component tag that identifies which inventory should be displayed in case cockpit does not have conveyor capabilities. |
| `PilotDummy` | Dummy on the pilot that will be used for positioning. It will be placed into position and rotated to align correctly. If the pilot does not have the dummy, its origin will be used for aligning. |
| `SeatDummy` | Dummy indicating where the pilot will be placed into cockpit. |
| `SeatType` | Information about what type of seat it is. Usable to distinguish different kinds of seats for various sitting animations for example. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\SeatComponentDefinition.def`

```json
{
  "Guid": "6fdb9a2d-8886-44ae-b956-aa19aa72c64a",
  "SeatType": {
    "Id": "Seat"
  },
  "PilotDummy": "a28b206d-33f2-46f5-b018-2445b1d6ae4b",
  "SeatDummy": "8e581544-8c74-4c85-be9f-5e175f2792c1",
  "ConveyorSubgraphNodeIndex": null,
  "Inventory": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('SeatComponentDefinitionObjectBuilder')
search_content('', type_contains='SeatComponentDefinitionObjectBuilder')
```
