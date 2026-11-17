# ContractMarkerTrackerConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Contracts.ContractMarkerTrackerConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Contracts`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FinishedMarker` | GPS HUD marker shown on the contract block when a contract is finished but not collected |
| `FinishedMarkerName` | Name of the HUD marker shown on the contract block when a contract is finished but not collected |

## A real one

`Vanilla\Assets\System\Configurations\ContractMarkerTrackerConfiguration.def`

```json
{
  "Guid": "6828bb42-5d8e-491e-bb6c-e7a2cc4e0b29",
  "FinishedMarker": "4b71d10d-a503-4cf7-82aa-1b62b4d40af2",
  "FinishedMarkerName": "ContractFinishedHUDMessage",
  "DelayedSpawnMarker": "4b71d10d-a503-4cf7-82aa-1b62b4d40af2",
  "DelayedSpawnMarkerName": "ContractDelayedSpawnHUDMessage"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ContractMarkerTrackerConfigurationObjectBuilder')
search_content('', type_contains='ContractMarkerTrackerConfigurationObjectBuilder')
```
