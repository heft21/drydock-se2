# AtmosphereNotificationConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Atmosphere.AtmosphereNotificationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Atmosphere`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `AtmosphericThrusterDensityLimit` | Atmospheric density at which notification warning should be displayed for Atmospheric Thrusters |
| `AtmosphericThrusterWarningAudio` | One-shot sound that is played when atmospheric thrusters on the user-controlled grid are out of their working environment. |
| `AtmosphericThrusterWarningNotification` | Notification that is displayed when the atmospheric density around the user controlled grid hits limit for atmospheric thrusters |
| `IonThrusterDensityLimit` | Atmospheric density at which notification warning should be displayed for Ion Thrusters |
| `IonThrusterWarningAudio` | One-shot sound that is played when ion thrusters on the user-controlled grid are out of their working environment. |
| `IonThrusterWarningNotification` | Notification that is displayed when the atmospheric density around the user controlled grid hits limit for ion thrusters |
| `LimitThreshold` | Atmospheric density variance from actual limit where density begins to be monitored |
| `MessageDuration` | How long the notifications should be visible |
| `NotificationInterval` | How long to wait for the notifications to be shown again |

## A real one

`Vanilla\Assets\System\Configurations\AtmosphereNotificationConfiguration.def`

```json
{
  "Guid": "6b55e5ab-0309-4acd-b61a-66a735e83e0d",
  "MessageDuration": 100000000,
  "NotificationInterval": 150000000,
  "AtmosphericThrusterDensityLimit": 0.6,
  "IonThrusterDensityLimit": 0.2,
  "LimitThreshold": 0.1,
  "AtmosphericThrusterWarningNotification": "b99155b9-459c-4786-9404-17fcbc7560cf",
  "IonThrusterWarningNotification": "3c6e5334-f614-4171-90e5-a1d821ae83e7"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('AtmosphereNotificationConfigurationObjectBuilder')
search_content('', type_contains='AtmosphereNotificationConfigurationObjectBuilder')
```
