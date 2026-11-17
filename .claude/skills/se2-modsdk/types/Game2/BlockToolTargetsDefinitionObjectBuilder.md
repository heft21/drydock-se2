# BlockToolTargetsDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools.BlockToolTargetsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools`
- definitions using it: **4**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `TargetMustHaves` | Used by to automatically create tool tiles for blocks meeting this composition. Blocks MUST have all of the components listed in this collection. |
| `TargetMustNotHaves` | Used by to automatically create tool tiles for blocks meeting this composition. Blocks must NOT have any components listed in this collection. |

## A real one

`Vanilla\Assets\BlockTools\Drill\DrillBlockTool_Client_BlockToolTargetsDefinition.def`

```json
{
  "Guid": "b4f0e6cf-0ee9-44c0-95c1-7f29b82f0005",
  "TargetMustHaves": [
    {
      "Key": "0665c99b-1b59-43a9-9878-618a4fb50ea1",
      "Value": "Game2:Keen.Game2.Simulation.WorldObjects.Tools.Voxels.DrillComponent"
    }
  ],
  "TargetMustNotHaves": []
}
```

Others: `BlockToolBase_Client_BlockToolTargetsDefinition`, `WeaponBlockTool_Client_BlockToolTargetsDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockToolTargetsDefinitionObjectBuilder')
search_content('', type_contains='BlockToolTargetsDefinitionObjectBuilder')
```
