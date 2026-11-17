# ResourceContainerBlockDestructionExplosionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Explosions.ResourceContainerBlockDestructionExplosionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Explosions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `EmptyDamageScalar` | Scalar applied to the damage dealt by when the container is empty. |
| `EmptyRadiusScalar` | Scalar applied to the explosion radius of when the container is empty. |
| `ExplosionTriggerThreshold` | If the container is filled to at least this percentage, the explosion will be triggered. If null, the explosion is always triggered. |
| `FullDamageScalar` | Scalar applied to the damage dealt by when the container is full. |
| `FullRadiusScalar` | Scalar applied to the explosion radius of when the container is full. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ResourceContainerBlockDestructionExplosionDefinition.def`

```json
{
  "Guid": "dedaeb54-e99c-45a3-9e57-5ad2a33daac4",
  "Explosion": null,
  "ExplosionCenter": "71e91ef6-11a4-4ba2-b034-9c8f77bee482",
  "EmptyRadiusScalar": 0,
  "FullRadiusScalar": 1,
  "EmptyDamageScalar": 0,
  "FullDamageScalar": 1,
  "ExplosionTriggerThreshold": null
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ResourceContainerBlockDestructionExplosionDefinitionObjectBuilder')
search_content('', type_contains='ResourceContainerBlockDestructionExplosionDefinitionObjectBuilder')
```
