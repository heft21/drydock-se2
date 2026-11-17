# PistonBlockColliderDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks.PistonBlockColliderDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.MechanicalBlocks`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PistonSubpartLayer` | Layer used by piston sub-parts. |
| `SubParts` | List of subparts that the piston collider consists of apart from the block collider itself. Subparts are extended sequentially based on the extension of the mechanical top part. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\PistonBlockColliderDefinition.def`

```json
{
  "Guid": "4af7cf42-84d5-420c-8f16-1e0667f02c82",
  "SubParts": [],
  "PistonSubpartLayer": "PistonSubpart"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PistonBlockColliderDefinitionObjectBuilder')
search_content('', type_contains='PistonBlockColliderDefinitionObjectBuilder')
```
