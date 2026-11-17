# DoorServerDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Doors.DoorServerDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Doors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OpeningDuration` | Time it takes to open the door. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DoorServerDefinition.def`

```json
{
  "Guid": "82be044d-44ad-4fc7-ab3e-f1335d110d3b",
  "OpeningDuration": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DoorServerDefinitionObjectBuilder')
search_content('', type_contains='DoorServerDefinitionObjectBuilder')
```
