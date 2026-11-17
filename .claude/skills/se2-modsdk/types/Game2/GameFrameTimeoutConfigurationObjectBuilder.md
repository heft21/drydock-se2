# GameFrameTimeoutConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.GameTimes.GameFrameTimeoutConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.GameTimes`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Budget` | Cancel non-parallel operations when the frame time is greater than the budget. |

## A real one

`Vanilla\Assets\System\Configurations\GameFrameTimeoutConfiguration.def`

```json
{
  "Guid": "06ebb07e-a69e-4ce0-bd5a-035fadd88d0c",
  "Budget": 100000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GameFrameTimeoutConfigurationObjectBuilder')
search_content('', type_contains='GameFrameTimeoutConfigurationObjectBuilder')
```
