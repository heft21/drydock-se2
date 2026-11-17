# PCUNotificationServerConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.PCU.PCUNotificationServerConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.PCU`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ReturnNotificationCooldown` | How long it takes from the last block destruction for the PCU Return notification to be finalized and sent to the owner |

## A real one

`Vanilla\Assets\System\Configurations\PCUNotificationServerConfiguration.def`

```json
{
  "Guid": "dfab9823-0080-4e23-9345-dbd2d8529599",
  "ReturnNotificationCooldown": 1000000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PCUNotificationServerConfigurationObjectBuilder')
search_content('', type_contains='PCUNotificationServerConfigurationObjectBuilder')
```
