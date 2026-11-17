# ContractTargetDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.ContractTargetDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Name` | Display name of the tag. |

## A real one

`Vanilla\Assets\Colonization\VS2-0\Contracts\SpaceBased\Verdure\Fields\LostAsteroidBase\VerdureFieldTarget.def`

```json
{
  "Guid": "c62226ce-1973-451b-b69c-1d570d95452c",
  "Name": "Verdure Field Target"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ContractTargetDefinitionObjectBuilder')
search_content('', type_contains='ContractTargetDefinitionObjectBuilder')
```
