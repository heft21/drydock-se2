# FanfareDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.HUD.Notifications.Fanfare.FanfareDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.HUD.Notifications.Fanfare`
- definitions using it: **9**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `OnOpenAudio` | Audio that is played as the fanfare starts opening. |
| `Timeout` | Length of time the fanfare should be displayed |
| `Title` | The title of the fanfare notification, represented by a localized key. |

## A real one

`Vanilla\Assets\UI\HUD\DeathFanfare.def`

```json
{
  "Guid": "8ceaa088-f2b5-4e64-9e7b-8ac6c4295f78",
  "Title": "DeathFanFareTitle",
  "Text": "RespawnPendingText",
  "Background": "{G}8b8acffd-9c06-49e3-9d76-86e03e6aa4be",
  "Timeout": null
}
```

Others: `FanfareExample`, `NewItemFanfare`

---

Read it with the MCP server rather than by hand:

```
describe_type('FanfareDefinitionObjectBuilder')
search_content('', type_contains='FanfareDefinitionObjectBuilder')
```
