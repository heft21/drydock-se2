# PermissionNotificationsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Permissions.PermissionNotificationsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Permissions`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `UnauthorizedBlockPlacementNotification` | Notification displayed when the user attempts to perform a block placer operation on a grid without valid permissions For instance: adding or removing a block from an NPC grid |
| `UnauthorizedCopyNotification` | Notification displayed when the user attempts to copy a grid without valid permissions |
| `UnauthorizedCutNotification` | Notification displayed when the user attempts to cut a grid without valid permissions |
| `UnauthorizedPartialCopyNotification` | Notification displayed when the user attempts to partial-copy a grid without valid permissions |

## A real one

`Vanilla\Assets\System\Notifications\Permissions\PermissionNotificationsConfiguration.def`

```json
{
  "Guid": "5e06f9ff-7a3d-4f6b-a9ff-185b45757029",
  "UnauthorizedBlockPlacementNotification": "6945e6e6-1a29-45c1-86df-dc9f05e44b28",
  "UnauthorizedCopyNotification": "8b9b803c-5052-4799-8e67-a5c69ba11106",
  "UnauthorizedPartialCopyNotification": "66307c49-c7e4-43ef-9ec5-9721aacd3a46",
  "UnauthorizedCutNotification": "48aba985-31f3-4f5a-8cea-0df12ffff1f6"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PermissionNotificationsConfigurationObjectBuilder')
search_content('', type_contains='PermissionNotificationsConfigurationObjectBuilder')
```
