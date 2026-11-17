# ConvergeTargetingDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Weapons.ConvergeTargetingDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Weapons`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxConvergenceAngle` | Maximum angle of the projectile direction versus the block forward. If the angle is greater than this, the projectile won't converge at all. |

## A real one

`Vanilla\Assets\Blocks\GatlingCannon\GatlingCannon\200\GatlingCannon200_ConvergeTargetingDefinition.def`

```json
{
  "Guid": "b5f08a2c-e0ea-469e-8a6d-3ae42b4d810e",
  "MaxConvergenceAngle": 30
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ConvergeTargetingDefinitionObjectBuilder')
search_content('', type_contains='ConvergeTargetingDefinitionObjectBuilder')
```
