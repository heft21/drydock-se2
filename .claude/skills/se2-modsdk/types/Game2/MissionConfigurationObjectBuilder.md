# MissionConfigurationObjectBuilder

`Game2:Keen.Game2.Simulation.GameSystems.Missions.MissionConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Simulation.GameSystems.Missions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `MissionGPSType` | GPS type created by missions |
| `TriggerPrefab` | Prefab used to represent a single trigger |

## A real one

`Vanilla\Assets\System\Configurations\MissionConfiguration.def`

```json
{
  "Guid": "e59251a0-a083-4d76-8d3a-5f1e230ba3ba",
  "TriggerPrefab": "9de949f7-c7c8-4a13-b189-1ee69456120d",
  "MissionGPSType": "3d5ca81c-5453-4012-869e-e7c07080b5d3",
  "DebugStateTitle": "ContractsMissionTooltip"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MissionConfigurationObjectBuilder')
search_content('', type_contains='MissionConfigurationObjectBuilder')
```
