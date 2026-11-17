# ArmorCollectorDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeGrids.Armors.ArmorCollectorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeGrids.Armors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BlocksPerSector` | Number of blocks per armor sector axis. Armor blocks are grouped by sectors of BlocksPerSector x BlocksPerSector x BlocksPerSector blocks. |

## A real one

`Vanilla\Assets\System\Grid\ArmorCollectorDefinition.def`

```json
{
  "Guid": "ed9a8299-83d2-4e36-8753-f5fa2c0fc06b",
  "BlocksPerSector": 32
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ArmorCollectorDefinitionObjectBuilder')
search_content('', type_contains='ArmorCollectorDefinitionObjectBuilder')
```
