# PCUNotificationConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.PCU.PCUNotificationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.PCU`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `LimitReachedNotification` | Notification that is displayed when the user has used all of their PCU |
| `ReturnedNotification` | Notification that is displayed when PCU is returned to the owner by destructions |
| `WarningNotification` | Notification that is displayed when the amount of PCU used is above or equal to the |
| `WarningRatio` | The ratio at which a notification will be sent saying that the user is reaching their PCU limit |

## A real one

`Vanilla\Assets\System\Configurations\PCUNotificationConfiguration.def`

```json
{
  "Guid": "560c890a-6047-4179-93aa-fe8c96e2628c",
  "LimitReachedNotification": "3333c0fc-293c-4237-aeeb-fc05b21820b6",
  "WarningNotification": "9bbff281-e747-42ca-b3a9-d6206c65acd3",
  "ReturnedNotification": "4f04a48e-cfbf-4f1b-90cf-bc1968ede7ff",
  "WarningRatio": 0.9,
  "HudRevealDuration": 30000000,
  "HudMinDisplayRatio": 0.8
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PCUNotificationConfigurationObjectBuilder')
search_content('', type_contains='PCUNotificationConfigurationObjectBuilder')
```
