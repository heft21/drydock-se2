# PCUSessionComponentConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.PCU.PCUSessionComponentConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.PCU`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MaxPlayerPCU` | The maximum PCU across the entire world |

## A real one

`Vanilla\Assets\System\Configurations\PCUSessionComponentConfiguration.def`

```json
{
  "Guid": "182d8cd3-df6e-43fc-92d0-fb3eb4ed9aac",
  "MaxGlobalPCU": 400000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PCUSessionComponentConfigurationObjectBuilder')
search_content('', type_contains='PCUSessionComponentConfigurationObjectBuilder')
```
