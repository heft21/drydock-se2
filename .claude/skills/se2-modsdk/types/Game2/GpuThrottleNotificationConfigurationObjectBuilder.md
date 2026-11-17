# GpuThrottleNotificationConfigurationObjectBuilder

`Game2:Keen.Game2.Client.RuntimeSystems.GpuThrottleNotificationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.RuntimeSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `PowerThrottlingNotification` | Notification shown when the GPU is power-limited (external power brake, or a reduced power budget while on battery) |
| `RecoveryResetInterval` | If throttling stops for at least this long, the next occurrence notifies immediately instead of waiting for the reminder cooldown |
| `ReminderInterval` | Minimum time between repeated notifications while a throttle persists, so a sustained issue reminds without spamming |
| `ThermalThrottlingNotification` | Notification shown when the GPU is throttling because of high temperature |

## A real one

`Vanilla\Assets\System\Configurations\GpuThrottleNotificationConfiguration.def`

```json
{
  "Guid": "b2012129-732f-4331-9ae9-618ab36a068c",
  "ReminderInterval": 3000000000,
  "RecoveryResetInterval": 50000000,
  "PowerThrottlingNotification": "dffca42d-8124-4a81-9ddb-da998b837f5d",
  "PowerCappedNotification": "90f0c34b-08fd-44c5-8883-c8b8a7ec2423",
  "ThermalThrottlingNotification": "f0d822c7-7601-42a7-a0c5-193169f6e5ff"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('GpuThrottleNotificationConfigurationObjectBuilder')
search_content('', type_contains='GpuThrottleNotificationConfigurationObjectBuilder')
```
