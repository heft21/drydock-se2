# DoorClientDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Doors.DoorClientDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Doors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ServerDefinition` | Server door definition this client door definition is associated with. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DoorClientDefinition.def`

```json
{
  "Guid": "51b06007-072f-43da-82ae-ac7c1f0a4e03",
  "ServerDefinition": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DoorClientDefinitionObjectBuilder')
search_content('', type_contains='DoorClientDefinitionObjectBuilder')
```
