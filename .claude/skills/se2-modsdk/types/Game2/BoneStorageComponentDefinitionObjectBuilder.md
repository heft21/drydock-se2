# BoneStorageComponentDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.BoneStorage.BoneStorageComponentDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.BoneStorage`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\BoneStorageComponent.def`

```json
{
  "Guid": "1490fd85-15c6-453f-aad9-4e18478b33c1",
  "ChunkSize": 8,
  "BoneSize": 4
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BoneStorageComponentDefinitionObjectBuilder')
search_content('', type_contains='BoneStorageComponentDefinitionObjectBuilder')
```
