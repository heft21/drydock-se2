# ToastNotificationDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Notifications.ToastNotificationDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Notifications`
- definitions using it: **36**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Content` | Optional text that's shown beneath the title |
| `Icon` | Optional custom icon for the notification |
| `Timeout` | How long the notification should last. Uses default timeout when not provided |
| `Title` | Title of the notification |

## A real one

`Vanilla\Assets\System\Notifications\NoEnergyNotification.def`

```json
{
  "Guid": "57a87043-2b4f-48c0-aab5-cd1ce4753e0c",
  "Title": "EnergyEmptyTitle",
  "Content": "EnergyEmptyText",
  "Timeout": null,
  "Icon": null
}
```

Others: `LowEnergyNotification`, `LowHealthNotification`

---

Read it with the MCP server rather than by hand:

```
describe_type('ToastNotificationDefinitionObjectBuilder')
search_content('', type_contains='ToastNotificationDefinitionObjectBuilder')
```
