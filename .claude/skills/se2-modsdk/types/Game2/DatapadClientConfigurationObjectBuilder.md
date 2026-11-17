# DatapadClientConfigurationObjectBuilder

`Game2:Keen.Game2.Client.WorldObjects.Datapads.DatapadClientConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.WorldObjects.Datapads`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `DatapadDiscoveredNotification` | Toast notification to display when the player loots a datapad he hasnt discovered yet |

## A real one

`Vanilla\Assets\Items\Datapads\System\DatapadClientConfiguration.def`

```json
{
  "Guid": "e82d9dee-0f90-40cb-a8ac-885659c0b562",
  "DatapadDiscoveredNotification": "4d0e13d8-febe-478c-8872-cb30414ccc74"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('DatapadClientConfigurationObjectBuilder')
search_content('', type_contains='DatapadClientConfigurationObjectBuilder')
```
