# FastTravelAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.MapScreen.FastTravel.FastTravelAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.MapScreen.FastTravel`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `Decoration` | Decoration of the fast travel |
| `FastTravelIcon` | Icon for fast travel |

## A real one

`Vanilla\Assets\UI\Screens\FastTravel\FastTravelAvaloniaConfiguration.def`

```json
{
  "Guid": "5ca791ce-800d-4f66-8be7-7db117af2d39",
  "Decoration": "{G}3aaf7c5c-9f77-454f-a5a8-8fa3c5b363a2",
  "FastTravelIcon": "{G}1b14aab2-f119-4100-b6d2-46087513ae3a"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('FastTravelAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='FastTravelAvaloniaConfigurationObjectBuilder')
```
