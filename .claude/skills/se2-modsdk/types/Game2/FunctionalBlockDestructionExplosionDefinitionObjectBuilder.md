# FunctionalBlockDestructionExplosionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Explosions.FunctionalBlockDestructionExplosionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Explosions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DamageScalar` | Scalar applied to the explosion radius of when the reactor is running. |
| `RadiusScalar` | Scalar applied to the explosion radius of when the reactor is running. |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\Reactors_FunctionalBlockDestructionExplosionDefinition.def`

```json
{
  "Guid": "899c59ce-b70b-4248-84b9-d059e7706ae3",
  "Explosion": "0c9bc035-c704-4793-b8d1-69f005423604",
  "ExplosionCenter": "71e91ef6-11a4-4ba2-b034-9c8f77bee482",
  "RadiusScalar": 1,
  "DamageScalar": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FunctionalBlockDestructionExplosionDefinitionObjectBuilder')
search_content('', type_contains='FunctionalBlockDestructionExplosionDefinitionObjectBuilder')
```
