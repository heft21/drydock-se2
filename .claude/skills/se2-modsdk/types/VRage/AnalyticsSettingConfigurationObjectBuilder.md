# AnalyticsSettingConfigurationObjectBuilder

`VRage:Keen.VRage.Analytics.AnalyticsSettingConfigurationObjectBuilder`

- bundle: **VRage**
- namespace: `Keen.VRage.Analytics`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AlwaysActiveEvents` | Events that are always enabled, regardless of active mapping |
| `AnalyticsSettingsValues` | Settings default values |
| `BatchSizeSettingName` | Name of the property as defined in Opicka |
| `ExpirationIntervalSettingName` | Name of the property as defined in Opicka |
| `HeartbeatIntervalSettingName` | Name of the property as defined in Opicka |
| `TimeSpentThreshold` | For events that have the TimeSpent property, this is the threshold to be surpassed for an event to be valid. |

## A real one

`Engine\Assets\Configurations\Setup\AnalyticsSettingConfiguration.def`

```json
{
  "Guid": "cd5e7a42-160b-40a0-9e29-4e16a48465af",
  "AlwaysActiveEvents": [
    {
      "Key": "3795a8ee-8a3b-41b2-ab02-176b2d035574",
      "Value": "SessionStart"
    },
    {
      "Key": "04186079-5d55-42c5-b614-d88528be3152",
      "Value": "WorldEnd"
    },
    {
      "Key": "da009ea8-d055-4e6a-870b-fe241cad49a9",
      "Value": "WorldStart"
    },
    {
      "Key": "baccda12-70e1-47b2-a4d9-3b6945452e9e",
      "Value": "Heartbeat"
    },
    {
      "Key": "102969e4-8fee-4247-8203-9248c54eabdf",
      "Value": "SessionEnd"
    }
  ],
  "BatchSizeSettingName": "BulkBatchSizeDefault",
  "HeartbeatIntervalSettingName": "HeartBeatIntervalDefault",
  "ExpirationIntervalSettingName": "ExpirationIntervalDefault",
  "AnalyticsSettingsValues": {
    "BatchSizeBulk": 500,
    "EventExpirationInterval": 0,
    "HeartbeatInterval": 5
  },
  "TimeSpentThreshold": 1
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AnalyticsSettingConfigurationObjectBuilder')
search_content('', type_contains='AnalyticsSettingConfigurationObjectBuilder')
```
