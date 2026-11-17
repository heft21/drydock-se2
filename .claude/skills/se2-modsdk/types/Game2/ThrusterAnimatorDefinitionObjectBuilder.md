# ThrusterAnimatorDefinitionObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.CubeBlocks.Movement.ThrusterAnimatorDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.CubeBlocks.Movement`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FlameLength` | Length of the thruster's flame |

## A real one

`Vanilla\Assets\Templates\Blocks\BaseDefinitions\ThrusterAnimatorDefinition.def`

```json
{
  "Guid": "97cca095-2b55-4f81-84a2-34a1ac16c9ab",
  "FlameLength": 0
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ThrusterAnimatorDefinitionObjectBuilder')
search_content('', type_contains='ThrusterAnimatorDefinitionObjectBuilder')
```
