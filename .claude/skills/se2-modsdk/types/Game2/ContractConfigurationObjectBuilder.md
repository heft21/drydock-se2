# ContractConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Encounters.ContractConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Encounters`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `ContractCompletedNotificationContent` | Content of fanfare shown when contract is completed |
| `ContractCompletedNotificationTitle` | Title of fanfare shown when contract is completed |

## A real one

`Vanilla\Assets\System\Configurations\ContractConfiguration.def`

```json
{
  "Guid": "ffa30e70-a434-4133-9e4b-ebcb10547d91",
  "ContractCompletedNotificationTitle": "ContractCompletedNotificationTitle",
  "ContractCompletedNotificationContent": "ContractCompletedNotificationContent",
  "DefaultFailureReason": "ContractFailureDefault"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ContractConfigurationObjectBuilder')
search_content('', type_contains='ContractConfigurationObjectBuilder')
```
