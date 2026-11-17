# GyroscopeDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.WorldObjects.CubeBlocks.Movement.GyroscopeDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.WorldObjects.CubeBlocks.Movement`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxTorque` | Max amplitude of the rotational force that this gyroscope can contribute to the grid it belongs to |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\GyroscopeDefinition.def`

```json
{
  "Guid": "3a7afb96-a6ed-4a8a-bf1b-ceb43edc4cca",
  "MaxTorque": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GyroscopeDefinitionObjectBuilder')
search_content('', type_contains='GyroscopeDefinitionObjectBuilder')
```
