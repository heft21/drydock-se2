# BlockPlacerConfiguration+SizeGroupDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.Tools.BlockPlacerConfiguration+SizeGroupDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.Tools`
- definitions using it: **4**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\BlockPlacer\HugeSizeGroupDefinition.def`

```json
{
  "Guid": "19631bec-f739-4e5d-b684-cb353cd5b70e",
  "LowerBound": 20
}
```

Others: `LargeSizeGroupDefinition`, `SmallSizeGroupDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockPlacerConfiguration+SizeGroupDefinitionObjectBuilder')
search_content('', type_contains='BlockPlacerConfiguration+SizeGroupDefinitionObjectBuilder')
```
