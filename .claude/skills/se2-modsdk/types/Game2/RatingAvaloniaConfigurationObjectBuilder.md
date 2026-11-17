# RatingAvaloniaConfigurationObjectBuilder

`Game2:Keen.Game2.Client.UI.Rating.RatingAvaloniaConfigurationObjectBuilder`

- bundle: **Game2**
- namespace: `Keen.Game2.Client.UI.Rating`
- definitions using it: **1**

## Fields

Straight from the SDK's own XML documentation — this is the only authoritative description of what each field means.

| field | meaning |
|---|---|
| `StarCount` | Gets the number of stars available for rating |
| `StarHighlightedIcon` | Representation of a highlighted star icon used for rating. |
| `StarIcon` | Representation of a star icon used for rating. |

## A real one

`Vanilla\Assets\MainMenuData\UI\RatingAvaloniaConfiguration.def`

```json
{
  "Guid": "4011a730-2252-49ab-afb3-0af43275f178",
  "StarCount": 5,
  "StarIcon": "{G}887f6acc-d512-49ae-ac5d-870c87a33dbe",
  "StarHighlightedIcon": "{G}175ee2f7-34ae-4d62-a24b-4db356d154cf"
}
```

---

Read it with the MCP server rather than by hand:

```
describe_type('RatingAvaloniaConfigurationObjectBuilder')
search_content('', type_contains='RatingAvaloniaConfigurationObjectBuilder')
```
