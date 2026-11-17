# OwnershipSessionDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Ownership.OwnershipSessionDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Ownership`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `RequestTimeoutTime` | Expiration time of ownership transfer requests, in seconds |

## A real one

`Vanilla\Assets\System\Session\OwnershipSessionDefinition.def`

```json
{
  "Guid": "986b2519-39ac-42df-9e9b-3beb361eb8cb",
  "RequestTimeoutTime": 600
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('OwnershipSessionDefinitionObjectBuilder')
search_content('', type_contains='OwnershipSessionDefinitionObjectBuilder')
```
