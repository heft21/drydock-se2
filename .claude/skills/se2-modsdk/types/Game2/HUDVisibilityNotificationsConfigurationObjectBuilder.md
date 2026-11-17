# HUDVisibilityNotificationsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.HUDVisibilityNotificationsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `FullStateNotification` | Toast notification for the Full state (all HUD visible). |
| `MinimalStateNotification` | Toast notification for the Minimal state (Flight HUD hidden). |

## A real one

`Vanilla\Assets\System\Notifications\HUD\HUDVisibilityNotificationsConfiguration.def`

```json
{
  "Guid": "e46e323d-2254-482f-9cb5-38640099612c",
  "MinimalStateNotification": "6b60cb5f-8354-4cb7-b551-32b39828075f",
  "FullStateNotification": "18e7f58c-1987-419a-ad44-80783ce15072"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('HUDVisibilityNotificationsConfigurationObjectBuilder')
search_content('', type_contains='HUDVisibilityNotificationsConfigurationObjectBuilder')
```
