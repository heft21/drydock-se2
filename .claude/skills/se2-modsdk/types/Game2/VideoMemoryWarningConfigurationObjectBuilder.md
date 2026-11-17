# VideoMemoryWarningConfigurationObjectBuilder

`Game2:Keen.Game2.Client.RuntimeSystems.VideoMemoryWarningConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.RuntimeSystems`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LowMemoryNotification` | Notification shown when the available video memory is low |
| `MinimumIntervalBetweenNotifications` | Minimum time interval in seconds between two consecutive notifications |

## A real one

`Vanilla\Assets\UI\HUD\VideoMemoryWarningConfiguration.def`

```json
{
  "Guid": "77b21760-9830-4ea8-8227-e6030c1d7ae7",
  "MinimumIntervalBetweenNotifications": 60,
  "LowMemoryNotification": "4df6fde1-f228-4535-8b20-216065fc031c"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('VideoMemoryWarningConfigurationObjectBuilder')
search_content('', type_contains='VideoMemoryWarningConfigurationObjectBuilder')
```
