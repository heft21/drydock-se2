# ProgressionNotificationsConfigurationObjectBuilder

`Game2:Keen.Game2.Client.GameSystems.Progression.ProgressionNotificationsConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.GameSystems.Progression`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `UnlockedGroupDefinition` | Fan fare shown when a is unlocked |

## A real one

`Vanilla\Assets\System\Configurations\ProgressionNotificationsConfiguration.def`

```json
{
  "Guid": "9b839b78-d63d-4ae1-b564-dcaddb3eb8e7",
  "UnlockedGroupDefinition": "b84c4cb7-5b8c-4519-bad6-55c203da1811"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('ProgressionNotificationsConfigurationObjectBuilder')
search_content('', type_contains='ProgressionNotificationsConfigurationObjectBuilder')
```
