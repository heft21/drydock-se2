# BlockDestructionExplosionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Explosions.BlockDestructionExplosionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Explosions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Explosion` | Explosion parameters. |
| `ExplosionCenter` | Dummy to center the explosion at. If not set or not present on the block, the explosion will be centered within the block's bounding box. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\BlockDestructionExplosionDefinition.def`

```json
{
  "Guid": "af9fb72c-0519-46cf-a1bd-3fcb57ef020f",
  "Explosion": null,
  "ExplosionCenter": "71e91ef6-11a4-4ba2-b034-9c8f77bee482"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockDestructionExplosionDefinitionObjectBuilder')
search_content('', type_contains='BlockDestructionExplosionDefinitionObjectBuilder')
```
