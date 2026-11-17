# DoorBlockColliderDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Doors.DoorBlockColliderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Doors`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ModelDefinition` | Base door model definition, to compute the closed door collider from. |
| `SubPartsProvider` | Definition providing the door sub-parts, to compute the closed door collider from. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\DoorBlockColliderDefinition.def`

```json
{
  "Guid": "3069cd0b-62fb-47c9-aabd-34a84b5091bc",
  "SubPartsProvider": null,
  "ModelDefinition": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DoorBlockColliderDefinitionObjectBuilder')
search_content('', type_contains='DoorBlockColliderDefinitionObjectBuilder')
```
