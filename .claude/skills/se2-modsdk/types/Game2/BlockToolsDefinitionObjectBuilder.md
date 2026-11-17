# BlockToolsDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools.BlockToolsDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ToolPrefabs` | Links a toolbar action type to a tool controller entity. The controller entity will be spawned server-side and replicated back to client. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\BlockToolsDefinition.def`

```json
{
  "Guid": "1f3af9b3-cedb-4697-89bd-49202f69e9e3",
  "ToolPrefabs": {
    "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools.DrillBlockToolAction": "6d2ec680-7abf-4961-ba28-c04a47794ab9",
    "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools.IntegrityBlockToolAction": "480cf63e-a866-41b5-8c7d-ea4e7fe2d856",
    "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools.WeaponBlockToolAction": "3c10707f-08ed-49ad-b570-98fd0f39095a",
    "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools.PistonBlockToolAction": "1ea0c275-e3e1-4e9b-b042-75950ec2ee06",
    "Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Tools.HingeBlockToolAction": "a25ac990-d8b1-4afa-9fb6-647f2bf6f70b"
  }
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockToolsDefinitionObjectBuilder')
search_content('', type_contains='BlockToolsDefinitionObjectBuilder')
```
