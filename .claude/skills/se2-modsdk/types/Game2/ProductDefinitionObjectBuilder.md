# ProductDefinitionObjectBuilder

`Game2:Keen.Game2.Client.UI.Menu.News.ProductDefinitionObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Menu.News`
- definitions using it: **2**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `SteamAppId` | The Steam Application ID associated with this product. |

## A real one

`Vanilla\Assets\MainMenuData\News\ProductDataDefinition\SE1ProductDefinition.def`

```json
{
  "Guid": "ebf71772-e684-4897-9cf0-e1a0fa60359c",
  "SteamAppId": 244850
}
```

Others: `PioneerEditionProductDefinition`

---

Read it with the MCP server rather than by hand:

```
describe_type('ProductDefinitionObjectBuilder')
search_content('', type_contains='ProductDefinitionObjectBuilder')
```
