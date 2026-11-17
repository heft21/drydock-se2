# BlockRewardGroupDefinitionObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Colonization.Rewards.BlockRewardGroupDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Colonization.Rewards`
- definitions using it: **31**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Name` | Friendly name of this reward group, displayed by UI when unlocked |

## A real one

`Vanilla\Assets\Templates\BaseDefinitions\Rewards\BlockRewardGroupDefinition.def`

```json
{
  "Guid": "32c7dec7-2087-4de5-9d3e-c71e3a7c8be7",
  "Name": "",
  "Blocks": []
}
```

Others: `DummyBlockSchematic_BlockRewardGroupDefinition`, `LCDT1_BlockRewardGroupDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('BlockRewardGroupDefinitionObjectBuilder')
search_content('', type_contains='BlockRewardGroupDefinitionObjectBuilder')
```
