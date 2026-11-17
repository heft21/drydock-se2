# PlacementDefinition+BlockSymmetriesDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.PlacementDefinition+BlockSymmetriesDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks`
- definitions using it: **36**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\Blocks\WedgeBlockSymmetries.def`

```json
{
  "Guid": "e62c6bf0-8da4-45f4-a55d-25e6acadab4a",
  "XAxis": {
    "X": 0,
    "Y": 0,
    "Z": 0
  },
  "YAxis": {
    "X": 0,
    "Y": 0,
    "Z": 2
  },
  "ZAxis": {
    "X": 0,
    "Y": 2,
    "Z": 0
  }
}
```

Others: `CornerBlockSymmetries`, `FlipBlockSymmetriesDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('PlacementDefinition+BlockSymmetriesDefinitionObjectBuilder')
search_content('', type_contains='PlacementDefinition+BlockSymmetriesDefinitionObjectBuilder')
```
