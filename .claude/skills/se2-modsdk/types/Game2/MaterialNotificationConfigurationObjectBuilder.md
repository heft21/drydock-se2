# MaterialNotificationConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Notification.MaterialNotificationConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Notification`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `BackpackIcon` | Icon for representing backpack |
| `MaxStackCount` | Represents the maximum count of items that can be stacked together. |
| `MissionObjectiveCloseDelay` | Time delay before a parent mission objective closed, specified in milliseconds. |
| `Timeout` | Specifies the duration before a notification automatically times out. |
| `TooltipCloseDelay` | Time delay before a tooltip is automatically closed, specified in milliseconds. |

## A real one

`Vanilla\Assets\UI\HUD\MaterialNotificationConfiguration.def`

```json
{
  "Guid": "50647dd0-5f86-46b4-bf22-cb1830f36ba2",
  "BackpackIcon": "{G}4c242a22-9886-417b-a4d9-c386ac4c2349",
  "MaxStackCount": 2,
  "Timeout": 24999999,
  "TooltipCloseDelay": 5000000,
  "MissionObjectiveCloseDelay": 7500000
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('MaterialNotificationConfigurationObjectBuilder')
search_content('', type_contains='MaterialNotificationConfigurationObjectBuilder')
```
