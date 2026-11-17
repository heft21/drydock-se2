# BlueprintNotificationsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Blueprints.BlueprintNotificationsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Blueprints`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `GridLoadingFailedNotification` | Blueprint grid failed to load from disk |
| `LoadingFailedNotification` | Blueprint was not found |

## A real one

`Vanilla\Assets\System\Blueprints\BlueprintNotificationsConfiguration.def`

```json
{
  "Guid": "fb6c1d52-14ad-40f6-941b-8336b0978846",
  "LoadingFailedNotification": "499b8f12-d3d6-4de6-ae5d-e23b81fd24e9",
  "GridLoadingFailedNotification": "4f67b733-eadc-4686-9f43-b4ae9069c0fa"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('BlueprintNotificationsConfigurationObjectBuilder')
search_content('', type_contains='BlueprintNotificationsConfigurationObjectBuilder')
```
