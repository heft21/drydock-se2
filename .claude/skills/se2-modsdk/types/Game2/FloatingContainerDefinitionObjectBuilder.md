# FloatingContainerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.FloatingObjects.FloatingContainerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.FloatingObjects`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\FloatingContainerDefinition.def`

```json
{
  "Guid": "97ce7230-a205-4c4d-929f-1a49b0f46326",
  "BoundingBoxDummyType": "93e59227-2a9d-434e-8685-a94af2b2a04d",
  "GravityType": "c575aff2-f829-47d2-8315-c81029239ccf"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FloatingContainerDefinitionObjectBuilder')
search_content('', type_contains='FloatingContainerDefinitionObjectBuilder')
```
