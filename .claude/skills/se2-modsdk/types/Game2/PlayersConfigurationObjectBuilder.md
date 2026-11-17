# PlayersConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.MapScreen.PlayersConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.MapScreen`
- definitions using it: **1**

## Fields

No XML documentation ships for this type. Read the example below and the vanilla files that use it.

## A real one

`Vanilla\Assets\System\GameSessions\PlayersConfiguration.def`

```json
{
  "Guid": "3eefb6d9-fc65-4901-b4d7-893155ef8e68",
  "PingSuccessThreshold": 600000,
  "PingWarningThreshold": 3000000,
  "PingTextKey": "PlayerScreenPing"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('PlayersConfigurationObjectBuilder')
search_content('', type_contains='PlayersConfigurationObjectBuilder')
```
